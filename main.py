from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    pass


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_text = website_input.get()
    email_text = email_input.get()
    password_text = password_input.get()

    is_ok = messagebox.askokcancel(title=website_text, message=f'These are the details entered: \nEmail: {email_text} '
                                                       f'\nPassword: {password_text} \nIs it ok to save?')

    if is_ok:
        with open('data.txt', mode='a') as file:
            file.writelines(f'{website_text} | {email_text} | {password_text}\n')
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

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=35)
# email_input.insert() --> insert commonly used email to pre-populate the text field whenever the app is running
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# Buttons

generate_button = Button(text='Generate Password', command=generate)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
