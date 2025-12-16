import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    global password_entry
    random_password = []
    for _ in range(4):
        random_capital = chr(random.randint(65, 90))
        random_small = chr(random.randint(97, 122))
        random_number = str(random.randint(0,9))
        random_password.append(random_small)

        random_password.append(random_capital)
        random_password.append(random_number)
    result = "".join(random_password)
    password_entry.delete(0,END)
    password_entry.insert(0,result)
    pyperclip.copy(result)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data= {
        website: {
            "email" : email,
            "password" : password
        }
    }
    if len(email)!=0 and len(password)!=0:
        try:
            with open("data.json","r") as dt:
                data = json.load(dt)

        except (FileNotFoundError, json.JSONDecodeError):
            with open("data.json", "w") as dt:
                json.dump(new_data, dt, indent=4)
        else:
            data.update(new_data)
            with open("data.json","w") as dt:
                json.dump(data, dt,indent=4)
        finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
    else:
        messagebox.showinfo(message="Invalid Credentials Please write something")
# ------------------------------Search------------------------------------#
def search():

        global website_entry
        web_to_find = website_entry.get()
        try:
            with open("data.json") as df:
                data = json.load(df)

                email = data[web_to_find]['email']
                password = data[web_to_find]['password']
                messagebox.showinfo(message=f"Email: {email} \nPassword: {password}")
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="Please add some data to me and try..")
        except KeyError:
            messagebox.showinfo(title="Error",message="Data doesn't exist..")
            website_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(140, 100, image=logo)
canvas.image = logo
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


website_entry = Entry(width=38)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)


search_btn = Button(text="Search" , width=13 , command=search)
search_btn.grid(row=1,column=2)
generate_password_btn = Button(text="Generate Password" , width=13,command=generate_password)
generate_password_btn.grid(row=3,column=2)
add_btn = Button(text="Add" , width=36,command=save_password)
add_btn.grid(row=4,column=1,columnspan=2)

window.mainloop()
