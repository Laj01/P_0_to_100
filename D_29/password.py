from tkinter import *

## UI elements ## 
window = Tk()
window.title('Password generator')
window.resizable(False, False)
window.config(padx=20, pady=20)

website_label = Label(text='Website :')
website_label.grid(column=0, row=1)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)

username_label = Label(text='Email/Username :')
username_label.grid(column=0, row=2)

username_entry = Entry(width=50)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text='Password :')
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_btn = Button(text='Generate Password')
generate_btn.grid(column=2, row=3)

add_btn = Button(text='Add', width=43)
add_btn.grid(column=1, row=4, columnspan=2)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)




window.mainloop()
