import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox as msbox
import time

from style import *
from array_generation import *

class Application:
    def __init__(self, root):
        self.root = root
        self.root.title("Sorting methods research")

        self.configureUI()

    def configureUI(self):
        self.root.config(bg = PRIMARY_BG_COLOR)

        tk.Label(
            self.root,
            text = "Shell method",
            font = HEADER_FONT,
            bg = PRIMARY_BG_COLOR
            ).grid(row = 0, column = 1)
        tk.Label(
            self.root,
            text = "Input array:",
            font = FONT,
            bg = PRIMARY_BG_COLOR
            ).grid(row = 1, column = 0, sticky='e')
        tk.Label(
            self.root,
            text = "Sorted array:",
            font = FONT,
            bg = PRIMARY_BG_COLOR
            ).grid(row = 2, column = 0, sticky='e')

        self.entInputArray = tk.Entry(self.root, font = FONT)
        self.entInputArray.grid(row = 1, column = 1)
        
        self.lblOutputArray = tk.Label(
            self.root,
            text = "Place for array",
            font = FONT,
            bg = LABEL_OUTPUT_BG_COLOR,
            borderwidth=2,
            relief="groove"
            )
        self.lblOutputArray.grid(row = 2, column = 1, sticky='nesw')

        tk.Button(
            self.root,
            text="Sort",
            font = FONT,
            bg = SORT_BUTTON_BG_COLOR,
            command = self.onSortButtonClicked,
            ).grid(row = 3, column = 1, sticky='nesw')
        tk.Button(
            self.root,
            text="Table",
            font = FONT,
            bg = BUTTON_BG_COLOR,
            command = self.onTableButtonClicked,
            ).grid(row = 4, column = 1, sticky='nesw')
        tk.Button(
            self.root,
            text="Graph",
            font = FONT,
            bg = BUTTON_BG_COLOR,
            command = self.onGraphButtonClicked,
            ).grid(row = 5, column = 1, sticky='nesw')
        
    def onSortButtonClicked(self):
        try:
            arr = list(map(int, self.entInputArray.get().split()))
            if arr == []:
                msbox.showerror(message = "Empty array was entered")
                return
        except:
            msbox.showerror(message = "Not an int array was entered")
        else:
            sortedArr = self.sortShell(arr)
            self.lblOutputArray.config(text = " ".join(map(str, sortedArr)))
        
    def onTableButtonClicked(self):
        rootTable = tk.Toplevel(self.root)
        rootTable.title("Table")
        rootTable.config(bg = PRIMARY_BG_COLOR)

        nValues = (10000, 50000, 100000)

        for i, n in enumerate(nValues):
            tk.Label(
                rootTable,
                text = " "*3 + "N = {:d}".format(n) + " "*3,
                bg = PRIMARY_BG_COLOR,
                font = FONT,
                ).grid(row = 0, column = i + 1)

        array_types = ["Sorted array", "Random array", "Reverse sorted array"]

        for i, array_type in enumerate(array_types):
            tk.Label(
                rootTable,
                text = array_type,
                bg = PRIMARY_BG_COLOR,
                font = FONT,
                ).grid(row = i + 1, column = 0, sticky="e")

        for i, n in enumerate(nValues):
            sortedArray = generage_sorted_array(n)
            randomArray = generage_random_array(n)
            reverseSortedArray = generage_reverse_sorted_array(n)
            
            arrays = [sortedArray, randomArray, reverseSortedArray]

            for j, array in enumerate(arrays):
                startTime = time.process_time()
                self.sortShell(array)
                endTime = time.process_time()
                                
                tk.Label(
                    rootTable,
                    text = "{:.3f} ms".format(1000 * (endTime - startTime)),
                    bg = PRIMARY_BG_COLOR,
                    font = FONT,
                    ).grid(row = j + 1, column = i + 1)
        
    def onGraphButtonClicked(self):
        nValues = range(10000, 100000 + 1, 10000)

        nTimes = []

        for n in nValues:
            array = generage_random_array(n)
            startTime = time.process_time()
            self.sortShell(array)
            endTime = time.process_time()
            nTimes.append(1000*(endTime - startTime))

        plt.title("Dependence of the sort execution time on the array length")
        plt.xlabel("Array length")
        plt.ylabel("Time, ms")

        plt.plot(nValues, nTimes, 'm', label = "Shell sort")
        plt.legend(loc = 0)
        plt.show()

    @staticmethod
    def sortShell(data):
        gap = len(data) // 2
        while gap:
            for i, el in enumerate(data):
                while i >= gap and data[i - gap] > el:
                    data[i] = data[i - gap]
                    i -= gap
                data[i] = el
            gap //= 2
        return data

    
if __name__ == "__main__":
    print("This is package file")
