import tkinter as tk
from database import db

from database_module.auth import login, get_role
from admin_dashboard import AdminDashboard
from teacher_dashboard import TeacherDashboard
from student_dashboard import StudentDashboard

session = {
    "username": "",
    "auth": ""
}

root = tk.Tk()
current_frame = tk.Frame(root)

def succes_login():
    global current_frame
    current_frame.pack_forget()
    if session["auth"] == "Administrator":
        dashboard = AdminDashboard(root)
    elif session["auth"] == "Teacher":
        dashboard = TeacherDashboard(root, session["username"])
    elif session["auth"] == "Student":
        dashboard = StudentDashboard(root, session["username"])
    current_frame = dashboard.get_frame()
    current_frame.pack()


def get_login_frame():
    error_msg = tk.StringVar()
    error_msg.set("")

    tk.Label(current_frame, text="User Name").grid(row=0, column=0)
    username = tk.StringVar()
    tk.Entry(current_frame, textvariable=username).grid(row=0, column=1)

    tk.Label(current_frame,text="Password").grid(row=1, column=0)
    password = tk.StringVar()
    tk.Entry(current_frame, textvariable=password, show='*').grid(row=1, column=1)

    def login_try():
        error_msg.set("")
        if login(username.get(), password.get(), db):
            session["username"] = username.get()
            session["auth"] = get_role(username.get(), db)
            succes_login()
        else:
            error_msg.set("Wrong username or password")

    tk.Label(current_frame, textvariable=error_msg).grid(row=3, column=0)
    tk.Button(current_frame, text="Login", command=login_try).grid(row=4, column=0)

    return current_frame

get_login_frame().pack()

root.mainloop()