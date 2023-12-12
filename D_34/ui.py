from tkinter import *


THEME_COLOR = '#060636'

class TriviaInterface:
    def __init__(self):
        self.window = Tk()
        self.window.title('App')
        self.window.resizable(False, False)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, text='PLACEHOLDER', fill=THEME_COLOR, font=('Arial', 24, 'italic'))
        self.canvas.grid(column=0, row=1, pady=50, columnspan=2)
        
        self.true_button = Button(text='TRUE', width=20)
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(text='FALSE', width=20)
        self.false_button.grid(column=1, row=2)


        self.window.mainloop()