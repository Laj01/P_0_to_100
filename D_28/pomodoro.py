from tkinter import *

#Fonts
FONT_NAME = 'Arial'
FONT_SIZE = 30
FONT_STYLE = 'bold'

#Colors
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

#Timer
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title('Pomodoro')
window.resizable(False, False)
window.config(padx=100, pady=50)

canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image = tomato_img)
canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
canvas.pack()


window.mainloop()