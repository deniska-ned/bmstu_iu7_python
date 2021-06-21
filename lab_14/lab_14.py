import tkinter as tk
import matplotlib.pyplot as plt
import scipy.optimize as sc
import numpy as np

from tkinter import messagebox, ttk
from time import perf_counter
from math import sin, sqrt, floor, log10, copysign, fabs


errors = [
    "Нет ошибок",
    "Превышено максимальное число итераций",
    "Корень находится на границе отрезка",
    "Деление на 0",
    "Длина отрезка меньше значения точности"
]


funcStr = "sin(x)"


def f(x):
    return eval(funcStr, {'x':x, 'sin': sin})


def yList(x):
    res = []
    for xi in x:
        res.append(f(xi))
    return res


def numToStr(x, digit=7):
    if x == 0:
        return '0'
    if abs(x) >= 10**digit:
        return ('{:.'+str(digit-1)+'e}').format(x)
    if abs(x) >= 10**(digit-1):
        return str(int(x))
    if abs(x) < 0.1:
        return ('{:.'+str(digit-1)+'e}').format(x)
    if abs(x) < 1:
        return ('{:.'+str(digit)+'f}').format(x)
    return str(round(x, -floor(log10(abs(x)))-1 + digit))


class Graph:
    def __init__(self, master, roots, a, b):
        x = np.linspace(a, b, 1000)
        y = yList(x)
        plt.plot(x, y, label = "f(x) = sin(x)")
        plt.title("Graph of function")

        xRoot = []
        for rootInfo in roots:
            xRoot.append(rootInfo["own"]["root"])
        yRoot = yList(xRoot)
        plt.plot(xRoot, yRoot, 'mo', label = "roots")
        plt.legend(loc = 1)
        plt.show()


class Metods:
    @staticmethod
    def ridderOwn(f, a, b, tol = None, maxiter = 10):
        fl = f(a)
        fh = f(b)
        if fl*fh < 0:
            xl = a
            xh = b
            ans = 10**8
            for iterationNumber in range(1, maxiter + 1):
                xm = 0.5 * (xl + xh)
                fm = f(xm)
                s = sqrt(fm*fm - fl*fh)
                if s == 0:
                    return {"root": ans, "iterations": iterationNumber, "codeError": 3}
                xnew = xm + (xm-xl)*copysign(1, fl - fh)*fm/s
                if fabs(xnew-ans) <= tol:
                    return {"root": ans, "iterations": iterationNumber, "codeError": 0}
                ans = xnew
                fnew = f(ans)

                if fnew == 0.0:
                    return {"root": ans, "iterations": iterationNumber, "codeError": 5}
                if copysign(fm,fnew) != fm:
                    xl = xm
                    fl = fm
                    xh = ans
                    fh = fnew
                elif copysign(fl, fnew) != fl:
                    xh = ans
                    fh = fnew
                elif copysign(fh, fnew) != fh:
                    xl = ans
                    fl = fnew
                else:
                    print("Never get here")

                if fabs(xh - xl) <= tol:
                    return {"root": ans, "iterations": iterationNumber, "codeError": 4}
        else:
            if fl == 0:
                return {"root": a, "iterations": 0, "codeError": 2}
            if fh == 0:
                return {"root": b, "iterations": 0, "codeError": 2}
        print("Never get here")
    
    @staticmethod
    def ridderScipy(f, a, b, tol, maxiter):
        startTime = perf_counter()
        codeError = None
        try:
            scipyRes = sc.ridder(
                f, 
                a, 
                b,
                xtol = tol, 
                maxiter = maxiter, 
                full_output = True
                )[1]
        except ZeroDivisionError:
            codeError = 3
        except:
            codeError = 6


        if codeError == None:
            if scipyRes.root in (a, b):
                codeError = 2
            elif scipyRes.iterations > maxiter:
                codeError = 1
            else:
                codeError = 0
        return {
            "root": scipyRes.root,
            "iterations": scipyRes.iterations if scipyRes.root not in (a, b) else 0,
            "codeError": codeError
            }


class TableRoots:
    def __init__(self, master, roots):
        slave = tk.Toplevel(master)
        slave.title("Таблица корней")
        if len(roots) == 0:
            tk.Label(slave, text = "Корней нет").pick()
            return

        tree = ttk.Treeview(slave)
        tree["columns"] = ["№", "Метод", "Отрезок", "Значение X", "Значение f(x)",
         "Число итераций", "Время работы", "Код ошибки"]
        tree["show"] = "headings"
        
        tree.column("№", width = 30, minwidth = 30, stretch = tk.NO)
        tree.column("Метод", width = 80, minwidth = 80, stretch = tk.NO)
        tree.column("Отрезок", width = 80, minwidth = 80, stretch = tk.NO)
        tree.column("Значение X", width = 80, minwidth = 80, stretch = tk.NO)
        tree.column("Значение f(x)", width = 90, minwidth = 90, stretch = tk.NO)
        tree.column("Число итераций", width = 100, minwidth = 100, stretch = tk.NO)
        tree.column("Время работы", width = 100, minwidth = 100, stretch = tk.NO)
        tree.column("Код ошибки", width = 80, minwidth = 80, stretch = tk.NO)

        
        for i in tree["columns"]:
            tree.heading(i, text = i)

        index = iid = 0
        for rootNumber, row in enumerate(roots):
            rows = self.formRows(row, rootNumber + 1)
            tree.insert("", index, iid, value = rows["own"])
            index = iid = index + 1
            tree.insert("", index, iid, value = rows["scipy"])
            index = iid = index + 1
        tree.grid(column = 0, row = 0)
        
        textError = "Коды ошибок:\n"
        for i, error in enumerate(errors):
            textError += str(i) + " - " + error + '\n'
        tk.Label(slave, text = textError, justify = tk.LEFT).grid(row = 0, column = 1)

    def formRows(self, rootInfo, rootNumber):
        row1 = [
            rootNumber,
            "Ridder",
            rootInfo["own"]["interval"],
            numToStr(rootInfo["own"]["root"], 9),
            numToStr(f(rootInfo["own"]["root"]), 1),
            rootInfo["own"]["iterations"],
            "{:.6f} ms".format(rootInfo["own"]["time"]),
            rootInfo["own"]["codeError"]
            ]
        row2 = [
            rootNumber,
            "Ridder (scipy)",
            rootInfo["scipy"]["interval"],
            numToStr(rootInfo["scipy"]["root"], 9),
            numToStr(f(rootInfo["scipy"]["root"]), 1),
            rootInfo["scipy"]["iterations"],
            "{:.6f} ms".format(rootInfo["scipy"]["time"]),
            rootInfo["scipy"]["codeError"]]
        return {"own": row1, "scipy": row2}
        

class Application:
    def __init__(self, master):
        self.master = master
        self.master.title("lab_14")

        #Вывод Label
        tk.Label(master, text = "Уточнение корней").grid(row = 0, column = 1)
        labelTexts = [
            "Функция",
            "Начало интервала",
            "Конец интервала",
            "Шаг разбиения",
            "Точность",
            "Максимальное число итераций"
            ]
        for i, labelText in enumerate(labelTexts):
            tk.Label(master, text = labelText).grid(row = i+1, column = 0)

        #Вывод Entry
        defaultValues = [
            "sin(x)",
            "0",
            "10",
            "1",
            "0.001",
            "10"
            ]

        self.entFunc = tk.Entry(master)
        self.entStart = tk.Entry(master)
        self.entEnd = tk.Entry(master)
        self.entStep = tk.Entry(master)
        self.entTol = tk.Entry(master)
        self.entMaxIter = tk.Entry(master)
        
        dictKeys = ("func", "start", "end", "step", "tol", "maxIter")
        dictValues = (
            self.entFunc, 
            self.entStart, 
            self.entEnd, 
            self.entStep, 
            self.entTol, 
            self.entMaxIter
            )
        lbls = dict(zip(dictKeys, dictValues))
        
        for i, key in enumerate(dictKeys):
            v = tk.StringVar(master, value = defaultValues[i])
            lbls[key].config(textvariable =  v)
            lbls[key].grid(column = 1, row = i + 1)

        #Вывод кнопки
        tk.Button(text = "Найти корни", command = self.onClick).grid(column = 1, row = len(dictKeys) + 1)

    def onClick(self):
        try:
            global funcStr 
            funcStr = self.entFunc.get()
            start = float(self.entStart.get())
            end = float(self.entEnd.get())
            step = float(self.entStep.get())
            tol  = float(self.entTol.get())
            maxIter = int(self.entMaxIter.get())
        except:
            messagebox.showerror(
                title = "Ошибка", 
                message = "Введены некорректные данные"
                )
        else:
            roots = self.searchRoots(
                start,
                end,
                step,
                tol,
                maxIter
                )
            self.displayRoots(roots)
            self.showGraph(roots, start, end)

    def searchRoots(self, start, end, step, tol, maxIter):
        roots = []
        a, b = start, start + step
        if a < end and b > end:
            b = end
        rootNum = 0
        while a < end:
            if f(a)*f(b) <= 0:
                rootNum += 1
            
                timeStart = perf_counter()
                myRes = Metods.ridderOwn(
                    f,
                    a,
                    b,
                    tol = tol,
                    maxiter = maxIter
                    )
                myRes["time"] = 1000*(perf_counter() - timeStart)
                myRes["interval"] = "[{:s}; {:s}]".format(numToStr(a, 3), numToStr(b, 3))

                timeStart = perf_counter()
                scipyRes = Metods.ridderScipy(
                    f,
                    a,
                    b,
                    tol = tol,
                    maxiter = maxIter
                    )
                scipyRes["time"] = 1000*(perf_counter() - timeStart)
                scipyRes["interval"] = "[{:s}; {:s}]".format(numToStr(a, 3), numToStr(b, 3))

                roots.append({"own": myRes, "scipy": scipyRes})


            a, b = a + step, b + step
            if a < end and b > end:
                b = end
        return roots
    
    def displayRoots(self, roots):
        TableRoots(self.master, roots)

    def showGraph(self, roots, start, end):
        Graph(self.master, roots, start, end)

def main():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()


if __name__ == "__main__":
    main()
