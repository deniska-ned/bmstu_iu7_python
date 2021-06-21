import tkinter as tk
import tkinter.messagebox as mbx
from style import *
from math import pi

F_TOL = 1e-5

class MathFun:
    @staticmethod
    def getDistance(p1, p2):
        return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

    @staticmethod
    def getCircleCoor(p1, p2, p3):
        if p1.y - p2.y != 0:
            isp1p2vertical = False
            k1 = - (p1.x - p2.x) / (p1.y - p2.y)
            mx1 = (p1.x + p2.x) / 2
            my1 = (p1.y + p2.y) / 2
            b1 = my1 - k1 * mx1
        else:
            mx1 = (p1.x + p2.x) / 2
            isp1p2vertical = True

        if p3.y - p2.y != 0:
            isp2p3vertical = False
            k2 = - (p3.x - p2.x) / (p3.y - p2.y)
            mx2 = (p3.x + p2.x) / 2
            my2 = (p3.y + p2.y) / 2
            b2 = my2 - k2 * mx2
        else:
            mx2 = (p3.x + p2.x) / 2
            isp2p3vertical = True

        if isp1p2vertical:
            x = mx1
            y = k2 * x + b2
            p = Point(x, y)
            return {
               "point": p, 
               "R": MathFun.getDistance(p, p1) 
               } 

        if isp2p3vertical:
            x = mx2
            y = k1 * x + b1
            p = Point(x, y)
            return {
               "point": p,
               "R": MathFun.getDistance(p, p1)
               } 
        
        x = - (b2 - b1) / (k2 - k1)
        y = k1 * x + b1
        p = Point(x, y)
        return {
            "point": p,
            "R": MathFun.getDistance(p, p1)
        }
   
    @staticmethod
    def findSquareTriangle(p1, p2, p3):
        a = MathFun.getDistance(p1, p2)
        b = MathFun.getDistance(p1, p3)
        c = MathFun.getDistance(p2, p3)

        p = (a + b + c) / 2

        return (p * (p - a) * (p - b) * (p - c))**0.5

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "Point(x: {:d}; y: {:d})".format(self.x, self.y)

    def __repr__(self):
        return "Point({:d}, {:d})".format(self.x, self.y)

class Application:
    canvas_width = 900
    canvas_height = 500

    points = []

    def __init__(self, root):
        self.root = root
        self.root.title("Planimetric task")
        self.root["bg"] = PRIMARY_BACKGROUND_COLOR

        self.UI()

        self.canvas.bind("<Button-1>", self.onCanvasClicked)
        self.canvas.bind("<Enter>", self.onEnterCanvas)
        self.canvas.bind("<Leave>", self.onLeaveCanvas)

    def UI(self):
        pointsFrame = tk.Frame(self.root, bg = PRIMARY_BACKGROUND_COLOR)
        tk.Label(
            pointsFrame,
            text = "Coordinates",
            bg = PRIMARY_BACKGROUND_COLOR,
            font = FONT,
            ).grid(row = 0, column = 0, sticky = "ws")
        self.entPointsCoordinates = tk.Entry(
            pointsFrame,
            bg = PRIMARY_BACKGROUND_COLOR,
            font = FONT,
            )
        self.entPointsCoordinates.grid(row = 0, column = 1)
        tk.Button(
            pointsFrame,
            text = "Draw points",
            bg = PRIMARY_BUTTON_BG_COLOR,
            command = self.onDrawPointsButtonClicked,
            font = FONT,
            ).grid(row = 0, column = 2)
        pointsFrame.pack()
        
        self.canvas = tk.Canvas(
            self.root, 
            width = self.canvas_width, 
            height = self.canvas_height,
            bg = PASSIVE_CANVAS_BG_COLOR
            )
        self.canvas.pack()

        btnFrame = tk.Frame(self.root)
        
        tk.Button(
            btnFrame,
            text = "Find", 
            bg = SECONDARY_BUTTON_BG_COLOR, 
            fg = SECONDARY_BUTTON_FG_COLOR,
            command = self.onFindButtonClicked,
            font = FONT,
            ).grid(row = 0, column = 0)
        tk.Button(
            btnFrame,
            text = "Clear",
            bg = SECONDARY_BUTTON_BG_COLOR, 
            fg = SECONDARY_BUTTON_FG_COLOR,
            command = self.onClearButtonClicked,
            font = FONT,
            ).grid(row = 0, column = 1)

        btnFrame.pack()

    def onCanvasClicked(self, event):
        x = event.x
        y = event.y

        if Point(x, y) not in self.points:
            self.drawPoint(event.x, event.y)
            self.points.append(Point(x, y))

    def onDrawPointsButtonClicked(self):
        s = self.entPointsCoordinates.get()
        try:
            coordinates = list(map(int, s.split()))
        except:
            mbx.showerror(message="Wrong coordinates")
            return

        if coordinates == []:
            mbx.showerror(message="Empty entity")
            return

        if len(coordinates) % 2 != 0:
            mbx.showerror(message="Incorrect len of coordinates")
            return

        for i in range(0, len(coordinates), 2):
            x = coordinates[i]
            y = coordinates[i + 1]

            if Point(x, y) not in self.points:
                self.drawPoint(x, y)
                self.points.append(Point(x, y)) 

        sv = tk.StringVar()
        sv.set("")
        self.entPointsCoordinates["textvariable"] = sv

    def onClearButtonClicked(self):
        self.canvas.delete("all")
        self.points.clear()

    def onFindButtonClicked(self):
        if len(self.points) < 3:
            mbx.showerror(message="At least three points are required")
            return

        searchedPoints = {"points" : (None, None, None), "difference" : None}
        for i in range(len(self.points)):
            for j in range(i + 1, len(self.points)):
                for k in range(j + 1, len(self.points)):
                    p1 = self.points[i]
                    p2 = self.points[j]
                    p3 = self.points[k]

                    if p1 == p2 or p1 == p3 or p2 == p3:
                        continue

                    if p1.x == p2.x == p3.x or p1.y == p2.y == p3.y:
                        continue
                    
                    if p1.x != p2.x and p2.x != p3.x:
                        k1 = (p1.y - p2.y) / (p1.x - p2.x)
                        k2 = (p3.y - p2.y) / (p3.x - p2.x)

                        if abs(k2 - k1) < F_TOL:
                            continue

                    R = MathFun.getCircleCoor(p1, p2, p3)["R"]

                    sCirle = pi * R * R
                    sTriangle = MathFun.findSquareTriangle(p1, p2, p3)
                    
                    if (searchedPoints["difference"] == None or 
                    searchedPoints["difference"] > sCirle - sTriangle):
                        searchedPoints["points"] = (p1, p2, p3)
                        searchedPoints["difference"] = sCirle - sTriangle

        if searchedPoints["difference"] == None:
            mbx.showerror(message = "Answer is not found")
            return

        points = searchedPoints["points"]
        self.drawTriangle(*points)

        someData = MathFun.getCircleCoor(*points)
        centerPoint = someData["point"]
        R = someData["R"]
        self.drawCircle(centerPoint, R)

    def onEnterCanvas(self, event):
        self.canvas["bg"] = ACTIVE_CANVAS_BG_COLOR

    def onLeaveCanvas(self, event):
        self.canvas["bg"] = PASSIVE_CANVAS_BG_COLOR

    def drawPoint(self, x, y):
        self.canvas.create_oval(x - 1, y - 1, x + 1, y + 1, fill = POINT_COLOR)

    def drawCircle(self, point, R):
        x = point.x
        y = point.y
        self.canvas.create_oval(x - R, y - R, x + R, y + R)

    def drawTriangle(self, p1, p2, p3):
        self.canvas.create_line(p1.x, p1.y, p2.x, p2.y, fill = TRIANGLE_COLOR)
        self.canvas.create_line(p1.x, p1.y, p3.x, p3.y, fill = TRIANGLE_COLOR)
        self.canvas.create_line(p3.x, p3.y, p2.x, p2.y, fill = TRIANGLE_COLOR)

if __name__ == "__main__":
    print("This is package file\n")
