import tkinter as tk

from form import Form
import fields

root = tk.Tk()

def get_vars():
    for field in user_form.vars.keys():
        print(f"{field}: {user_form.vars[field].get()}")

user_form = Form(fields.user, root, get_vars, "USER")
user_form.frame.pack()

root.mainloop()