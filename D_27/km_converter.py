from tkinter import *

def main():
    window = Tk()
    window.title('Km to Miles')
    #window.minsize(width=200, height=100)
    #window.resizable(False, False)
    window.config(padx=20, pady=20)

    miles_input = Entry(width=10)
    miles_input.grid(row=0, column=1)

    miles_label = Label(text='Miles')
    miles_label.grid(row=0, column=2)

    is_equal_label = Label(text='is equal to')
    is_equal_label.grid(row=1, column=0)

    km_result_label = Label(text=0)
    km_result_label.grid(row=1, column=1)

    km_label = Label(text='KM')
    km_label.grid(row=1, column=2)

    calculate_button = Button(text='Calculate')
    calculate_button.grid(row=2, column=1)

    window.mainloop()


if __name__ == '__main__':
    main()