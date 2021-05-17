import tkinter as tk

from database_module import select
from database import db


def add_temp_field(root, text, row, column):
    entry = tk.Entry(root)
    entry.insert(0, text)
    entry.grid(row=row, column=column)
    entry.config(state='disabled')


def get_student_overview_frame(student_id, root):
    grade_frame = tk.Frame(root)

    student = select.get_specific("user", student_id, db)

    tk.Label(grade_frame, text=f"{student['First_name']} {student['Last_name']}").grid()
    
    results = select.get_all_from_field("results", "Student_id", student_id, db)

    headers = ["Exam", "Grade", "Passed", "Resit"]
    table_headers = ["Exam_id", "Grade", "Passed"]

    for i in range(len(headers)):
        add_temp_field(grade_frame, headers[i], 1, i)

    for i in range(len(results)):
        exam = select.get_specific("exams", results[i]["Exam_id"], db)
        for h in range(len(table_headers)):
            if h == 2:
                add_temp_field(grade_frame, "Yes" if results[i][table_headers[h]] else "No", i+2, h)  
            else:  
                add_temp_field(grade_frame, results[i][table_headers[h]], i+2, h)

            add_temp_field(grade_frame, "Yes" if exam["Resit"] else "No", i+2, len(headers)-1)

    return grade_frame


def get_total_overview_frame(root):
    grade_frame = tk.Frame(root)

    results = select.get_all("results", db)

    headers = ["First name", "Last name", "Exam", "Grade", "Passed", "Resit"]
    table_headers = ["Exam_id", "Grade", "Passed"]

    for i in range(len(headers)):
        add_temp_field(grade_frame, headers[i], 0, i)

    for i in range(len(results)):
        student = select.get_specific("user", results[i]["Student_id"], db)
        exam = select.get_specific("exams", results[i]["Exam_id"], db)

        add_temp_field(grade_frame, student["First_name"], i+1, 0)
        add_temp_field(grade_frame, student["Last_name"], i+1, 1)

        for h in range(len(table_headers)):
            text = results[i][table_headers[h]]
            if h == 2:
                text = "Yes" if results[i][table_headers[h]] else "No"
              
            add_temp_field(grade_frame, text, i+1, h+2)

        add_temp_field(grade_frame, "Yes" if exam["Resit"] else "No", i+1, len(headers)-1)

    return grade_frame