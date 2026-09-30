from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    webapp = website_input.get()
    email = email_input.get()
    password = password_output.get()
    with open("data.txt", "a") as file:
        file.write(f"{webapp} | {email} | {password}\n")

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
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")
website_input.focus()

# Email or username input
email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(row=2, column=0)
email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="ew")
email_input.insert(0, "m.yarisahyadi@gmail.com")

# Password generation box
password_label = Label(text="Password: ", bg="white")
password_label.grid(row=3, column=0)
password_output = Entry(width=21)
password_output.grid(row=3, column=1, sticky="ew")
password_gen_label = Button(text="Generate Password", bg="white", highlightthickness=0)
password_gen_label.grid(row=3, column=2, sticky="w")

# Add button
add_button = Button(text="Add", width=36, bg="white", highlightthickness=0, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
