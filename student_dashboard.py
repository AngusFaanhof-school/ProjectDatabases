import tkinter as tk
import show

class StudentDashboard:
    def __init__(self, root, student_id):
        self.root = root
        self.current_form = None
        self.form_frame = tk.Frame(root)
        self.main = tk.Frame(root)
        self.student_id = student_id

    def back(self):
        self.form_frame.pack_forget()
        self.current_form.pack_forget()
        self.main.pack()

    def get_frame(self):
        tk.Button(self.form_frame, text="Back", command=self.back).pack()

        def update_window_tid(func):
            self.main.pack_forget()
            self.current_form = func(self.form_frame, self.student_id)
            self.current_form.pack()
            self.form_frame.pack()

        def show_results():
            update_window_tid(show.student_results)

        def show_courses():
            update_window_tid(show.student_courses)

        def show_study_councelor():
            update_window_tid(show.student_study_counselor)

        tk.Button(self.main, text="Show results", command=show_results).grid(row=1, column=1)
        tk.Button(self.main, text="Show courses", command=show_courses).grid(row=2, column=1)
        tk.Button(self.main, text="Show study councelor", command=show_study_councelor).grid(row=3, column=1)

        return self.main