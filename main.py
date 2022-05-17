from tkinter import *
from tkinter import messagebox
import random
import json


window = Tk()
window.geometry("500x400")
window.title("GUI Program")
window.config(bg="white")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
all_passwords = []


def save():
    email_input = email_username_entry.get()
    web_input = web_entry.get()
    password_input = password_entry.get()
    new_data = {
        web_input: {
            "email": email_input,
            "password": password_input,
        }
    }
    if len(web_input and email_input) > 0 and len(password_input) == 8 and password_input not in all_passwords:
        is_ok = messagebox.askyesno(title="TITLE", message=f"Details were saved \nWebsite : {web_input}\nEmail : {email_input} \nPassword : {password_input} \nIs it okey to save?")
        if is_ok:
            try:
                with open("file.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open('file.json', mode='w') as file:
                    json.dump(new_data, file, indent=4)

            else:
                data.update(new_data)
                with open("file.json", mode="w") as file:
                    json.dump(data, file, indent=4)
            finally:
                web_entry.delete(0, END)
                password_entry.delete(0, END)

    elif len(web_input and email_input) > 0 and len(password_input) == 0:
        messagebox.showwarning(title='Warning', message='Info was missed')
    elif len(web_input and email_input) > 0 and len(password_input) != 8 and password_input in all_passwords:
        messagebox.showwarning(title='Warning', message='This password already exists!')
    elif len(web_input and email_input) > 0 and len(password_input) != 8:
        messagebox.showwarning(title='Warning', message='Password must contain 8 symbols')
    else:
        messagebox.showwarning(title="Warning", message="Info was missed")


canvas = Canvas(height=200, width=200, bg="white", highlightthickness=0)
logo_image = PhotoImage(file="Qulf.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(column=1, row=0)


# Labels
web_lab = Label(text="Website:", pady=5, bg='white').grid(row=1, column=0)
email_username = Label(text="Email/Username:", bg='white').grid(row=2, column=0)
password = Label(text="Password:", bg='white', padx=5).grid(row=3, column=0)


# Entries
web_entry = Entry(width=35, borderwidth=5)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
email_username_entry = Entry(width=35, borderwidth=5)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.insert(0, "tolaganov03@list.ru")
password_entry = Entry(width=21, borderwidth=5)
password_entry.grid(row=3, column=1)


def creating_random_password():
    collecting_password = ''
    for i in range(0, 8):
        random_letter = random.choice(letters)
        collecting_password += random_letter
        i += 1
    if len(collecting_password) == 8:
        password_entry.delete(0, END)
        password_entry.insert(0, collecting_password)


#Buttons
generate_password = Button(text="Generate Password", width=15, command=creating_random_password).grid(row=3, column=2)
add = Button(text="Add", width=34, command=save).grid(row=4, column=1, columnspan=2)


window.mainloop()