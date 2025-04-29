from tkinter import *

print('Чтобы нарисовать, зажмите левую кнопку мыши и нарисуйте круг')
print('Чтобы изменить цвет кисти, нажмите на один из цветов')

window = Tk()
canvas = Canvas(window, width=750, height=500, bg='white')
canvas.pack()

lastX, lastY = 0, 0
color = 'black'

def store_position(event):
    global lastX, lastY
    lastX = event.x
    lastY = event.y

def onClick(event):
    store_position(event)

def onDrag(event):
    canvas.create_line(lastX, lastY, event.x, event.y, fill=color, width=3)
    store_position(event)

canvas.bind('<Button-1>', onClick)
canvas.bind('<B1-Motion>', onDrag)


red_id = canvas.create_rectangle(10, 10, 30, 30, fill='red')
blue_id = canvas.create_rectangle(10, 35, 30, 55, fill='blue')
black_id = canvas.create_rectangle(10, 60, 30, 80, fill='black')
white_id = canvas.create_rectangle(10, 85, 30, 105, fill='white')

def setColourRed(event):
    global color
    color = 'red'

def setColourBlue(event):
    global color
    color = 'blue'

def setColourBlack(event):
    global color
    color = 'black'

def setColourWhite(event):
    global color
    color = 'white'

canvas.tag_bind(red_id, '<Button-1>', setColourRed)
canvas.tag_bind(blue_id, '<Button-1>', setColourBlue)
canvas.tag_bind(black_id, '<Button-1>', setColourBlack)
canvas.tag_bind(white_id, '<Button-1>', setColourWhite)

window.mainloop()