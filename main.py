from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_image)
canvas.pack()

website_input = Entry()
website_input.pack()

email_username_input = Entry()
email_username_input.pack()

password_input = Entry()
password_input.pack()

generate_button = Button(text='generate')
generate_button.pack()

add_button = Button(text='add')
add_button.pack()

window.mainloop()
