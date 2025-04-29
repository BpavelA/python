import tkinter

window = tkinter.Tk()
button = tkinter.Button(window, text='Только не нажимай меня!', width=40)
button.pack(padx=20, pady=20)

clickCounter = 0

def onClick(event):
    global clickCounter
    clickCounter += 1
    if clickCounter == 1:
        button.configure(text='Нет, нет, нет! Не делай этого!')
    elif clickCounter == 2:
        button.configure(text='Если ещё раз нажмёшь меня, я исчезну!')
    else:
        button.pack_forget()

button.bind('<ButtonRelease-1>', onClick)


# дальше запускается цикл событий, без цикла программы выйдет немедленно
# причина, по которой вам не нужно вызывать mainloop в режиме ожидания, 
# заключается в том, что IDLE делает это за вас. 
# Во всех остальных случаях необходимо вызывать mainloop.
window.mainloop() 