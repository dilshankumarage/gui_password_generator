from tkinter import *
from tkinter import messagebox
import random
# ---------------------------- UI SETUP ------------------------------- #
FONT_NAME = "Arial"

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")

    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Please verify the details entered: "
                                                          f"\nEmail: {email}\nPassword: {password}")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

        # Clear fields after saving
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    #new_list = [expression for item in iterable if condition]
    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    # Clear any existing text
    password_entry.delete(0, END)
    # Insert the new password
    password_entry.insert(0, password)

# Window setup
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Logo
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")  # Make sure logo.png exists in the same folder
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Website Label + Entry
website_label = Label(text="Website:", font=(FONT_NAME, 10, "bold"))
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

# Email/Username Label + Entry
email_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"))
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "dilshan@email.com") #default email suggested if user uses the same mail

# Password Label + Entry
password_label = Label(text="Password:", font=(FONT_NAME, 10, "bold"))
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, padx=(0, 25))

# Buttons (Generate Password and Add)
generate_button = Button(text="Generate", command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
