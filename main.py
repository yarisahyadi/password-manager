from tkinter import *
from tkinter import messagebox
import random
import json
# import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def find_password():
    website = website_input.get()

    try:
        with open("data.json", "r") as data_file:
            credential_data = json.load(data_file)
            if website in credential_data.keys():
                messagebox.showinfo(message=f"Email/Username: {credential_data[website]['email']}\n"
                f"Password: {credential_data[website]['password']}")
            else:
                messagebox.showinfo(message="No details for the website exists")
    except FileNotFoundError:
        messagebox.showinfo(message="No data file found")

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + [random.choice(symbols) for _ in range(nr_symbols)] + [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_output.delete(0, END)
    password_output.insert(0, password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    webapp = website_input.get()
    email = email_input.get()
    password = password_output.get()
    new_data = {
        webapp: {
            "email":email,
            "password":password
            }
        }

    if webapp == "" or password == "":
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        confirmed = messagebox.askokcancel(title=webapp, message=f"Email/Username: {email}\n Password: {password}\n Proceed to save?")
        if confirmed:
            try:
                with open("data.json", "r") as data_file:
                    data_json = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as new_file:
                    json.dump(new_data, new_file, indent=4)
            else:
                data_json.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data_json, data_file, indent=4)
            finally:
                website_input.delete(0, "end")
                password_output.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

# logo and canvas
lock_image = PhotoImage(file="/Users/myari/Documents/Study/Python/100 Days of Code/[Day 29] password-manager/logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Website input
website_label = Label(text="Website/App: ", bg="white")
website_label.grid(row=1, column=0)
website_input = Entry(width=21)
website_input.grid(row=1, column=1, sticky="ew")
website_input.focus()

# Search button
search_button = Button(width=15, text="Search", bg="white", highlightthickness=0, command=find_password)
search_button.grid(row=1, column=2, sticky="w")

# Email or username input
email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(row=2, column=0)
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="ew")
email_input.insert(0, "m.yarisahyadi@gmail.com")

# Password entry
password_label = Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0)
password_output = Entry(width=21)
password_output.grid(row=3, column=1, sticky="ew")

# Password generator button
password_gen_button = Button(width=15, text="Generate Password", bg="white", highlightthickness=0, command=generate_password)
password_gen_button.grid(row=3, column=2, sticky="w")

# Add button
add_button = Button(text="Add", width=36, bg="white", highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
