from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_value = website_input.get().lower()
    email_value = email_input.get()
    password_value = password_input.get()

    new_data = {
        website_value: {
            "email": email_value,
            "password": password_value
        }
    }

    if len(website_value) == 0 or len(email_value) == 0 or len(password_value) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)
            website_input.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def search_password():
    website_value = website_input.get().lower()

    if len(website_value) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave Website field empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="Start with storing some values.")
        else:
            if website_value in data:
                email_value = data[website_value]["email"]
                password_value = data[website_value]["password"]
                messagebox.showinfo(title=website_value.title(),
                                    message=f"Email: {email_value} \nPassword: {password_value}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {website_value.title()} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_input = Entry()
website_input.config(width=37)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text="Search", command=search_password)
search_button.grid(row=1, column=2)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry()
email_input.config(width=56)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "john@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry()
password_input.config(width=37)
password_input.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
