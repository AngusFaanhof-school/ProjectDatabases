import tkinter as tk

from database_module.insert import *

from insert_form import Form

field_dict = {
    "administrator": {
        "pk": "Admin_id",
        "fk": ["user"],
        "function": add_administrator
    },
    "course": {
        "pk": "course_id",
        "fk": ["teacher", "study"],
        "function": add_course
    },
    "exams": {
        "pk": "Exam_id",
        "fk": ["course"],
        "function": add_exam
    },
    "results": {
        "pk": ("Exam_id", "Student_id"),
        "fk": ["exam", "student"],
        "function": add_result
    },
    "students": {
        "pk": "Student_id",
        "fk": ["user", "study", "teacher"],
        "function": add_student
    },
    "study": {
        "pk": "Study_id",
        "fk": [],
        "function": add_study
    },
    "teachers": {
        "pk": "Teacher_id",
        "fk": "user",
        "function": add_teacher
    },
    "user": {
        "pk": "id",
        "fk": [],
        "function": add_user
    },
}

# TODO: better datetime for exams

root = tk.Tk()
# field = "results"
# user_form = Form(field, field_dict[field]["pk"], field_dict[field]["function"], root, field_dict[field]["fk"])
# user_form.get_frame().pack()
root.mainloop()