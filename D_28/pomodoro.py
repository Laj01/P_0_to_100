from tkinter import *


window = Tk()
window.title('Pomodoro')
window.resizable(False, False)
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image = tomato_img)

canvas.pack()


window.mainloop()