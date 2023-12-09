from tkinter import *

#Fonts
FONT_NAME = 'Arial'
FONT_SIZE = 30
FONT_STYLE = 'bold'
CHECK_MARK = '✔'

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
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text='TIMER', fg=GREEN, bg=YELLOW, font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
title_label.grid(column=1, row=0)

start_button = Button(text='Start', highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', highlightthickness=0)
reset_button.grid(column=2, row=2)

check_marks = Label(text=CHECK_MARK, fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=2)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image = tomato_img)
canvas.create_text(102, 130, text='00:00', fill='white', font=(FONT_NAME, FONT_SIZE, FONT_STYLE))
canvas.grid(column=1, row=1)


window.mainloop()