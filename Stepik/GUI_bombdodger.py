from tkinter import *
from random import randint

gameOver = False
score = 0
squaresToClear = 0

def play_bombdodger():
    create_bombfield(bombfield)
    window = Tk()
    layout_window(window)
    window.mainloop()

bombfield = []

def create_bombfield(bombfield):
    global squaresToClear
    for row in range(0, 10):
        rowList = []
        for column in range(0, 10):
            if randint(1, 100) < 20:
                rowList.append(1)
            else:
                rowList.append(0)
                squaresToClear += 1
        bombfield.append(rowList)

def printfield(bombfield):
    for rowList in bombfield:
        print(rowList)

def layout_window(window):
    for rowNumber, rowList in enumerate(bombfield):
        for columnNumber, columnEntry in enumerate(rowList):
            if randint(1, 100) < 25:
                square = Label(window, text="    ", bg='darkgreen')
            elif randint(1, 100) > 75:
                square = Label(window, text="    ", bg='seagreen')
            else:
                square = Label(window, text="    ", bg='green')
            square.grid(row = rowNumber, column = columnNumber)


play_bombdodger()
#printfield(bombfield)



