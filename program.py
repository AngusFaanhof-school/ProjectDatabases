import tkinter as tk
from database import db

from database_module.auth import login, get_role
from database_module.helpers import get_full_name
from admin_dashboard import AdminDashboard
from teacher_dashboard import TeacherDashboard
from student_dashboard import StudentDashboard

root = tk.Tk()

session = {
    "username": "",
    "auth": "",
    "full_name": tk.StringVar()
}

current_frame = tk.Frame(root)

def clear_root():
    global current_frame
    current_frame.destroy()
    current_frame = tk.Frame(root)


current_user_frame = tk.Frame(root)
tk.Label(current_user_frame, textvariable=session["full_name"]).pack(side=tk.LEFT)

def succes_login():
    global current_frame
    current_user_frame.pack(anchor=tk.NE)
    clear_root()
    if session["auth"] == "Administrator":
        dashboard = AdminDashboard(current_frame)
    elif session["auth"] == "Teacher":
        dashboard = TeacherDashboard(current_frame, session["username"])
    elif session["auth"] == "Student":
        dashboard = StudentDashboard(current_frame, session["username"])
    session["full_name"].set(get_full_name(session["username"], db))
    dashboard.get_frame().pack()
    current_frame.pack()


def get_login_frame():
    login_frame = tk.Frame(current_frame)
    error_msg = tk.StringVar()
    error_msg.set("")

    tk.Label(login_frame, text="User Name").grid(row=0, column=0)
    username = tk.StringVar()
    tk.Entry(login_frame, textvariable=username).grid(row=0, column=1)

    tk.Label(login_frame,text="Password").grid(row=1, column=0)
    password = tk.StringVar()
    tk.Entry(login_frame, textvariable=password, show='*').grid(row=1, column=1)

    def login_try():
        error_msg.set("")
        if login(username.get(), password.get(), db):
            session["username"] = username.get()
            session["auth"] = get_role(username.get(), db)
            succes_login()
        else:
            error_msg.set("Wrong username or password")

    tk.Label(login_frame, textvariable=error_msg, fg="red").grid(row=3, column=1)
    tk.Button(login_frame, text="Login", command=login_try).grid(row=4, column=0)

    return login_frame

def log_out():
    global current_frame
    current_user_frame.pack_forget()
    session["username"] = ""
    session["auth"] = ""
    session["full_name"].set("")
    clear_root()
    get_login_frame().pack()
    current_frame.pack()

tk.Button(current_user_frame, text="Logout", command=log_out).pack(side=tk.RIGHT)

get_login_frame().pack()
current_frame.pack()

root.minsize(500, 500)

root.mainloop()