from tkinter import *
from tkinter import messagebox
import random
import pyperclip


## Generate password ##
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


## Save data ##
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Error', message='Some fields are left empty!')
    else:
        is_ok = messagebox.askokcancel(title=website, 
                                    message=f'The following data will be saved:\n'
                                    f'Email: {email}\nPassword: {password}\nCan we save now?')
        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f'{website} | {email} | {password}\n')

            website_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()


## UI elements ## 
window = Tk()
window.title('Password generator')
window.resizable(False, False)
window.config(padx=20, pady=20)

website_label = Label(text='Website :')
website_label.grid(column=0, row=1)

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_label = Label(text='Email/Username :')
email_label.grid(column=0, row=2)

email_entry = Entry(width=50)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'somebody@email.com')

password_label = Label(text='Password :')
password_label.grid(column=0, row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3)

generate_btn = Button(text='Generate Password', command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text='Add', width=43, command=save)
add_btn.grid(column=1, row=4, columnspan=2)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)


window.mainloop()