import json
import random
import pyperclip
from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    password_input.delete(0, END)
    letters = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
        "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I",
        "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
        "V", "W", "X", "Y", "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    random_letters = random.sample(letters, 4)
    random_symbols = random.sample(symbols, 4)
    random_numbers = random.sample(numbers, 4)

    random_list = random_letters + random_symbols + random_numbers

    shuffled_list = random.shuffle(random_list)

    password = "".join(random_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ------------------------SEARCH FOR INFORMATION -----------------------#
def search():
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
            # for retrieving information
            website = website_input.get().lower()
        email = data[website]['email']
        password = data[website]['password']
    except KeyError:
        messagebox.showerror(title='Error', message='No Data File Found')
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data File Found')
    else:
        messagebox.showinfo(title=f'{website}', message=f'Email: {email}\nPassword: {password}\n')


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_input.get().lower()
    email_text = email_input.get()
    password_text = password_input.get()
    new_data = {
        website_text: {
            'email': email_text,
            'password': password_text
        }
    }
    if website_text == '' or email_text == '' or password_text == '':
        messagebox.showwarning(message='Please do not leave any of the fields empty!')

    else:
        try:
            with open('data.json', mode='r') as file:
                data = json.load(file)

        except FileNotFoundError:
            with open('data.json', mode='w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', mode='w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)

# Labels

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_label = Label(text='Email/Username:')
email_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

# Text Boxes

website_input = Entry(width=21)
website_input.focus()
website_input.grid(column=1, row=1)

email_input = Entry(width=35)
# email_input.insert() --> insert commonly used email to pre-populate the text field whenever the app is running
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons
search_button = Button(text='Search', width=12, command=search)
search_button.grid(column=2, row=1)

generate_button = Button(text='Generate Password', command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
