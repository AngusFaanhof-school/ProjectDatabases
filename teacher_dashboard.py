import tkinter as tk

import show

from inserts import field_dict
from insert_form import Form

class TeacherDashboard:
    def __init__(self, root, teacher_id):
        self.root = root
        self.current_form = None
        self.form_frame = tk.Frame(root)
        self.main = tk.Frame(root)
        self.teacher_id = teacher_id

    def back(self):
        self.form_frame.pack_forget()
        self.current_form.pack_forget()
        self.main.pack()

    def get_frame(self):
        tk.Button(self.form_frame, text="Back", command=self.back).pack()

        def add_result():
            self.main.pack_forget()
            self.current_form = Form("results", field_dict["results"]["pk"], field_dict["results"]["function"], self.form_frame, field_dict["results"]["fk"], self.teacher_id).get_frame()
            self.current_form.pack()
            self.form_frame.pack()

        tk.Label(self.main, text="Add").grid(row=0, column=0)
        tk.Button(self.main, text="Add result", command=add_result).grid(row=1, column=0)

        def update_window2(func):
            self.main.pack_forget()
            self.current_form = func(self.form_frame)
            self.current_form.pack()
            self.form_frame.pack()

        def update_window_tid(func):
            self.main.pack_forget()
            self.current_form = func(self.form_frame, self.teacher_id)
            self.current_form.pack()
            self.form_frame.pack()

        def show_courses():
            update_window_tid(show.teacher_courses)

        def show_all_students():
            update_window2(show.all_students)

        def show_teacher_students():
            update_window_tid(show.teacher_students)

        def show_teacher_students_results():
            update_window_tid(show.teacher_students_results)

        tk.Label(self.main, text="Show").grid(row=0, column=1)
        tk.Button(self.main, text="Show courses", command=show_courses).grid(row=1, column=1)
        tk.Button(self.main, text="Show all students", command=show_all_students).grid(row=2, column=1)
        tk.Button(self.main, text="Show study councelor students", command=show_teacher_students).grid(row=3, column=1)
        tk.Button(self.main, text="Show study councelor students results", command=show_teacher_students_results).grid(row=4, column=1)

        return self.main
