PROGRAM_INFO = '''
Лабораторная работа №15
\"Имитация восьмиразрядного сумматора\"

Требования:
Разработать приложение калькулятор (8-разрядный сумматор)
Ввод с клавиатуры и с помощью программного интерфеса
Предусмотреть:
1. Повтор заданных действий
2. Очистка полей
3. Информация о программе и авторе

'''

AUTHOR_INFO = '''
Автор: Недолужко Денис
Группа: ИУ7-23Б
'''

import tkinter as tk
from tkinter import messagebox

import EightBitAdder
from style import *

class Application:
    activeOparator = "plus"
    lastOperation = None
    showBinNum = False

    def __init__(self, root):
        self.root = root
        self.root.title("Восьмиразрядный сумматор")
        self.root.config(bg = "white")

        # Menu
        mainMenu = tk.Menu(self.root)
        mainMenu.config(bg = MENU_BG_COLOR)

        actionMenu = tk.Menu(
            self.root,
            bg = MENU_BG_COLOR,
            fg = MENU_FG_COLOR
            )
        actionMenu.add_command(
            label = "Показать двоичные числа",
            command = self.setShowBinNum
            )
        
        mainMenu.add_cascade(label = "Действия", menu = actionMenu)

        helpMenu = tk.Menu(
            self.root,
            bg = MENU_BG_COLOR,
            fg = MENU_FG_COLOR
            )
        helpMenu.add_command(
            label = "О программе",
            command = self.showProgramInfo
            )
        helpMenu.add_command(
            label = "О авторе",
            command = self.showAuthorInfo
            )

        mainMenu.add_cascade(label = "Справка", menu = helpMenu)        
        
        self.root.config(menu = mainMenu)

        # Entry

        self.ent1 = tk.Entry(
            self.root,
            width = 9,
            justify = tk.RIGHT,
            font = ("Helvetica", 24),
            borderwidth = 0,
            )
        self.ent1.focus_set()
        self.ent1.pack(fill = tk.BOTH)

        self.ent2 = tk.Entry(
            self.root,
            width = 9,
            justify = tk.RIGHT,
            font = ("Helvetica", 24),
            borderwidth = 0,
            )
        self.ent2.pack(fill = tk.BOTH)

        # Buttons

        self.frameButtons = tk.Frame(self.root, bg = "white")
        self.frameButtons.pack()

        btnData = (
            ('C', "delAll",  self.clickDelAll),
            ('±', "plusMin", self.clickPlusMin),
            ('↺', "repeat",  self.clickRepeat),
            ('+', "plus",    self.clickPlus),
            ('-', "minus",   self.clickMinus),
            ('←', "delOne",  self.clickDelOne),
            ('7', "seven",   self.clickSeven),
            ('8', "eight",   self.clickEight),
            ('9', "nine",    self.clickNine),
            ('4', "four",    self.clickFour),
            ('5', "five",    self.clickFive),
            ('6', "six",     self.clickSix),
            ('1', "one",     self.clickOne),
            ('2', "two",     self.clickTwo),
            ('3', "three",   self.clickThree),
            ('0', "zero",    self.clickZero),
            ('=', "equal",   self.clickEqual)
            )

        self.btn = {}

        for row in range((len(btnData) + 1) // 3):
            for column in range(3):
                if row * 3 + column + 1 > len(btnData):
                    break
                self.btn[btnData[row * 3 + column][1]] = tk.Button(
                    self.frameButtons,
                    bg = "white",
                    width = BUTTON_WIDTH,
                    height = BUTTON_HEIGHT,
                    text = btnData[row * 3 + column][0],
                    font = ("Helvetica", 24),
                    command = btnData[row * 3 + column][2],
                    borderwidth = 0
                    )
                self.btn[btnData[row * 3 + column][1]].grid(
                    row = row, column = column)

        self.btn["equal"]["bg"] = EQUAL_BTN_BG_COLOR
        self.setActiveOparator("plus")

    def setActiveOparator(self, operatorName):
        self.activeOparator = operatorName
        if operatorName == "plus":
            self.btn["plus"].config(
                bg = ACTIVE_OPERATOR_BTN_BG_COLOR,
                fg = ACTIVE_OPERATOR_BTN_FG_COLOR
            )
            self.btn["minus"].config(
                bg = INACTIVE_OPERATOR_BTN_BG_COLOR,
                fg = INACTIVE_OPERATOR_BTN_FG_COLOR
            )
        else:
            self.btn["minus"].config(
                bg = ACTIVE_OPERATOR_BTN_BG_COLOR,
                fg = ACTIVE_OPERATOR_BTN_FG_COLOR
            )
            self.btn["plus"].config(
                bg = INACTIVE_OPERATOR_BTN_BG_COLOR,
                fg = INACTIVE_OPERATOR_BTN_FG_COLOR
            )

    def showProgramInfo(self):
        window = tk.Toplevel(self.root, bg = ADD_WINDOW_BG_COLOR)
        window.title("О программе")
        tk.Label(window, text = PROGRAM_INFO, bg = ADD_WINDOW_BG_COLOR).pack()

    def showAuthorInfo(self):
        window = tk.Toplevel(self.root, bg = ADD_WINDOW_BG_COLOR)
        window.title("О авторе")
        tk.Label(window, text = AUTHOR_INFO, bg = ADD_WINDOW_BG_COLOR).pack()

    # Commands of buttons

    def clickDelAll(self):
        entFocus = self.root.focus_get()
        if entFocus == None:
            messagebox.showerror(text = "Не выбрано поле ввода")
        else:
            entFocus.config(textvariable = tk.StringVar(value = ""))

    def clickPlusMin(self):
        entFocus = self.root.focus_get()
        if entFocus == None:
            messagebox.showerror(text = "Не выбрано поле ввода")
        else:
            s = entFocus.get()
            if len(s) > 0:
                if s[0] == '-':
                    s = s[1:]
                elif s[0] == '+':
                    s = '-' + s[1:]
                else:
                    s = '-' + s
            else:
                s = '-'
            entFocus.config(textvariable = tk.StringVar(value = s))
            
    def clickRepeat(self):
        if self.lastOperation == None:
            messagebox.showerror(message="Не было произведено действий ранее") 
            return

        valueEnt1 = self.ent1.get()
        if isinteger(valueEnt1):
            self.setActiveOparator(self.lastOperation["operator"])
            num1 = int(valueEnt1)
            num2 = self.lastOperation["num2"]
            
            res = self.calc(num1, num2)
                
            answerStringVar = tk.StringVar(value=str(res))
            self.ent1.config(textvariable = answerStringVar)

            emptyStringVar = tk.StringVar(value="")
            self.ent2.config(textvariable = emptyStringVar)

    def clickPlus(self):
        self.setActiveOparator("plus")

    def clickMinus(self):
        self.setActiveOparator("minus")

    def clickDelOne(self):
        entFocus = self.root.focus_get()
        if entFocus == None:
            messagebox.showerror(text = "Не выбрано поле ввода")
        else:
            entFocus.delete(len(entFocus.get()) - 1)

    def clickSeven(self):
        self.addNumToEntry('7')

    def clickEight(self):
        self.addNumToEntry('8')

    def clickNine(self):
        self.addNumToEntry('9')

    def clickFour(self):
        self.addNumToEntry('4')

    def clickFive(self):
        self.addNumToEntry('5')

    def clickSix(self):
        self.addNumToEntry('6')

    def clickOne(self):
        self.addNumToEntry('1')

    def clickTwo(self):
        self.addNumToEntry('2')

    def clickThree(self):
        self.addNumToEntry('3')

    def clickZero(self):
        self.addNumToEntry('0')

    def clickEqual(self):
        valueEnt1 = self.ent1.get()
        valueEnt2 = self.ent2.get()
        
        if not( isinteger(valueEnt1) and isinteger(valueEnt2) ):
            messagebox.showerror(message = "Числа не опознаны")
        else:
            num1 = int(valueEnt1)
            num2 = int(valueEnt2)

            self.lastOperation = {
                "operator": self.activeOparator,
                "num2": num2,
            }

            res = self.calc(num1, num2)
            
            answerStringVar = tk.StringVar(value=str(res))
            self.ent1.config(textvariable = answerStringVar)

            emptyStringVar = tk.StringVar(value="")
            self.ent2.config(textvariable = emptyStringVar)


    def addNumToEntry(self, num):
        entFocus = self.root.focus_get()
        if entFocus == None:
            messagebox.showerror(text = "Не выбрано поле ввода")
        else:
            entFocus.insert(len(entFocus.get()), num)

    def calc(self, num1, num2):
        if self.activeOparator == "minus":
            num2 *= -1
        
        binNum1 = EightBitAdder.decToBin(num1)
        binNum2 = EightBitAdder.decToBin(num2)

        binRes = EightBitAdder.sum(binNum1, binNum2)

        if self.showBinNum == True:
            self.showNumbers(binNum1, binNum2, binRes)

        decRes = EightBitAdder.binToDec(binRes)
        
        return decRes

    def setShowBinNum(self):
        if self.showBinNum == False:
            self.showBinNum = True
            self.window = tk.Toplevel(self.root)
            self.window.title("Двоичные числа")
            self.lbl = tk.Label(
                self.window,
                text = "Здесь будут отображаться\n двоичные числа",
                font = ("Courier New", 14),
                bg = "white",
                )
            self.lbl.pack()
        else:
            self.showBinNum = False
            self.window.destroy()

    def showNumbers(self, num1, num2, res):
        try:
            self.lbl.config(text = 
            '''
Первое число: {:^4d} = {:s}
Второе число: {:^4d} = {:s}

Результат:    {:^4d} = {:s}
            '''.format(
                EightBitAdder.binToDec(num1),
                str(num1),
                EightBitAdder.binToDec(num2),
                str(num2),
                EightBitAdder.binToDec(res),
                str(res)
                )
            )
        except Exception as e:
            print(e)
def isinteger(a):
    try:
        int(a)
        return True
    except:
        return False


if __name__ == "__main__":
    print("This is package file")
