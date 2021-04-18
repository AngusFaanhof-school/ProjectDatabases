import tkinter as tk

root = tk.Tk()
root.geometry("900x900")
root.title("Login")


login_frame = tk.Frame(root, borderwidth=2)

username_frame = tk.Frame(login_frame)

username_label = tk.Label(username_frame, text="Username:").pack(side="left")
username = tk.StringVar()
username_entry = tk.Entry(username_frame, textvariable=username).pack(side="right")
username_frame.pack(side="top")


password_frame = tk.Frame(login_frame)

password_label = tk.Label(password_frame, text="password:").pack(side="left")
password = tk.StringVar()
password_entry = tk.Entry(password_frame, textvariable=password).pack(side="right")
password_frame.pack(side="top")

def login():
    print("username: ", username.get())
    print("password: ", password.get())

login_button = tk.Button(login_frame, width=13, height=3, text="Login", command=login).pack()

login_frame.pack()

root.mainloop()