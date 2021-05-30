import tkinter as tk

from inserts import field_dict
from insert_form import Form
import show


class AdminDashboard:
    def __init__(self, root):
        self.root = root
        self.current_form = None
        self.form_frame = tk.Frame(root)
        self.main = tk.Frame(root)


    def back(self):
        self.form_frame.pack_forget()
        self.current_form.pack_forget()
        self.main.pack()


    def get_frame(self):
        tk.Button(self.form_frame, text="Back", command=self.back).pack()

        def update_window(field):
            self.main.pack_forget()
            self.current_form = Form(field, field_dict[field]["pk"], field_dict[field]["function"], self.form_frame, field_dict[field]["fk"]).get_frame()
            self.current_form.pack()
            self.form_frame.pack()


        tk.Label(self.main, text="Add").grid(row=0, column=0)

        def add_user():
            update_window("user")

        def add_teacher():
            update_window("teachers")

        def add_student():
            update_window("students")

        def add_admin():
            update_window("administrator")

        def add_study():
            update_window("study")

        def add_exam():
            update_window("exams")

        def add_course():
            update_window("course")

        def add_result():
            update_window("results")

        tk.Button(self.main, text="Add user", command=add_user).grid(row=1, column=0)
        tk.Button(self.main, text="Add admin", command=add_admin).grid(row=2, column=0)
        tk.Button(self.main, text="Add teacher", command=add_teacher).grid(row=3, column=0)
        tk.Button(self.main, text="Add student", command=add_student).grid(row=4, column=0)
        tk.Button(self.main, text="Add study", command=add_study).grid(row=5, column=0)
        tk.Button(self.main, text="Add course", command=add_course).grid(row=6, column=0)
        tk.Button(self.main, text="Add exam", command=add_exam).grid(row=7, column=0)
        tk.Button(self.main, text="Add result", command=add_result).grid(row=8, column=0)


        def update_window2(func):
            self.main.pack_forget()
            self.current_form = func(self.form_frame)
            self.current_form.pack()
            self.form_frame.pack()

        def show_users():
            update_window2(show.all_users)

        def show_admins():
            update_window2(show.all_admins)

        def show_teachers():
            update_window2(show.all_teachers)

        def show_students():
            update_window2(show.all_students)

        def show_studies():
            update_window2(show.all_studies)

        def show_courses():
            update_window2(show.all_courses)

        def show_exams():
            update_window2(show.all_exams)

        def show_results():
            update_window2(show.all_results)

        tk.Label(self.main, text="Show").grid(row=0, column=1)
        tk.Button(self.main, text="Show users", command=show_users).grid(row=1, column=1)
        tk.Button(self.main, text="Show admin", command=show_admins).grid(row=2, column=1)
        tk.Button(self.main, text="Show teacher", command=show_teachers).grid(row=3, column=1)
        tk.Button(self.main, text="Show student", command=show_students).grid(row=4, column=1)
        tk.Button(self.main, text="Show study", command=show_studies).grid(row=5, column=1)
        tk.Button(self.main, text="Show course", command=show_courses).grid(row=6, column=1)
        tk.Button(self.main, text="Show exam", command=show_exams).grid(row=7, column=1)
        tk.Button(self.main, text="Show result", command=show_results).grid(row=8, column=1)

        return self.main
