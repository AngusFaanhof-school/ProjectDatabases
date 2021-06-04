from tkcalendar import DateEntry
import tkinter as tk
import json
import datetime

from database_module.helpers import check_pk
from database_module.select import get_all, get_all_from_field, get_all_from_fields, get_all_from_field_with_value
from database import db


def get_fk_user_dropdown(root):
    rows = get_all("user", db)
    text_options = [row["First_name"] + " " + row["Last_name"] for row in rows]
    ids = [row["id"] for row in rows]

    id_var = tk.StringVar(value=ids[0])
    str_var = tk.StringVar(value=text_options[0])

    def option_change(x):
        id_var.set(ids[text_options.index(x)])

    return tk.OptionMenu(root, str_var, *text_options, command=option_change), id_var


def get_fk_study_dropdown(root):
    rows = get_all("study", db)
    text_options = [row["study_name"] for row in rows]
    ids = [row["Study_id"] for row in rows]

    id_var = tk.StringVar(value=ids[0])
    str_var = tk.StringVar(value=text_options[0])

    def option_change(x):
        id_var.set(ids[text_options.index(x)])

    return tk.OptionMenu(root, str_var, *text_options, command=option_change), id_var


def get_fk_student_dropdown(root):
    student_dict = {}
    student_data = get_all_from_fields("user", ["id", "First_name", "Last_name"], db)
    student_ids = get_all_from_field("students", "Student_id", db)

    for student in student_data:
        if student["id"] in student_ids:
            student_dict[student["First_name"] + " " + student["Last_name"]] = student["id"]

    student_names = list(student_dict.keys())

    id_var = tk.StringVar(value=list(student_dict.values())[0])
    str_var = tk.StringVar(value=student_names[0])

    def option_change(x):
        id_var.set(student_dict[x])

    return tk.OptionMenu(root, str_var, *student_names, command=option_change), id_var


def get_fk_teacher_dropdown(root):
    teacher_dict = {}
    teacher_data = get_all_from_fields("user", ["id", "First_name", "Last_name"], db)
    teacher_ids = get_all_from_field("teachers", "Teacher_id", db)

    for teacher in teacher_data:
        if teacher["id"] in teacher_ids:
            teacher_dict[teacher["First_name"] + " " + teacher["Last_name"]] = teacher["id"]

    teacher_names = list(teacher_dict.keys())

    id_var = tk.StringVar(value=list(teacher_dict.values())[0])
    str_var = tk.StringVar(value=teacher_names[0])

    def option_change(x):
        id_var.set(teacher_dict[x])

    return tk.OptionMenu(root, str_var, *teacher_names, command=option_change), id_var


def get_fk_exam_dropdown(root):
    rows = get_all("exams", db)
    options = [row["Exam_id"]for row in rows]

    var = tk.StringVar(value=options[0])

    return tk.OptionMenu(root, var, *options), var


def get_fk_teacher_exams_dropdown(root, teacher_id):
    rows = get_all_from_field_with_value("course", "Teacher_id", teacher_id, db)
    courses = [row["course_id"] for row in rows]

    exams = []
    for course in courses:
        exams += [row["Exam_id"] for row in get_all_from_field_with_value("exams", "Course_id", course, db)]

    var = tk.StringVar(value=exams[0])
    return tk.OptionMenu(root, var, *exams), var


def get_fk_course_dropdown(root):
    rows = get_all("course", db)
    text_options = [row["Course_name"] for row in rows]
    ids = [row["course_id"] for row in rows]

    id_var = tk.StringVar(value=ids[0])
    str_var = tk.StringVar(value=text_options[0])

    def option_change(x):
        id_var.set(ids[text_options.index(x)])

    return tk.OptionMenu(root, str_var, *text_options, command=option_change), id_var

def get_entry(field_type, root):
    var = tk.StringVar()

    if "int" in field_type:
        length = int(field_type.replace("int-", ""))

        def callback(inp):
            if not str.isdigit(inp) or len(inp)>length:
                return False
            return True
        reg = root.register(callback)

        return tk.Entry(root, validate="key", validatecommand=(reg, '%P'), textvariable=var), var

    elif field_type == "bool":
        var = tk.IntVar()
        var.set(1)

        entry_frame = tk.Frame(root)
        tk.Radiobutton(entry_frame, text="True", variable=var, value=1).pack()
        tk.Radiobutton(entry_frame, text="False", variable=var, value=0).pack()
        return entry_frame, var


    elif "string" in field_type:
        length = int(field_type.replace("string-", ""))

        def callback(inp):
            if len(inp)>length:
                return False
            return True
        reg = root.register(callback)

        return tk.Entry(root, font=('arial', 20, 'bold'), validate="key", validatecommand=(reg, '%P'), textvariable=var), var

    elif "enum" in field_type:
        options = field_type.replace("enum(", "").replace("'", "")[:-1].split(",")
        var.set(options[0])

        return tk.OptionMenu(root, var, *options), var

    elif field_type == "date":
        return DateEntry(root, textvariable=var, date_pattern="dd/mm/y"), var

    elif field_type == "datetime":
        datetime_frame = tk.Frame(root)
        time_var = tk.StringVar()
        DateEntry(datetime_frame, textvariable=var, date_pattern="dd/mm/y").pack()
        tk.Entry(datetime_frame, textvariable=time_var).pack()
        return datetime_frame, [var, time_var]


def get_values(string_vars, table_fields):
    values = {}

    for field in string_vars.keys():
        if table_fields[field]["type"] == "date":
            values[field] = datetime.datetime.strptime(string_vars[field].get(), "%d/%m/%Y")
        elif table_fields[field]["type"] == "datetime":
            try:
                values[field] = datetime.datetime.strptime(string_vars[field][0].get() + string_vars[field][1].get(), "%d/%m/%Y%H:%M:%S")
            except:
                values[field] = ""
        else:
            values[field] = string_vars[field].get()

    return values


def validate_values(values, table_fields):
    for field in table_fields.keys():
        if not table_fields[field]["null"] and values[field] == "":
            return False
    return True


f = open("forms/table_fields.json", "r")
all_table_fields = json.load(f)

class Form:
    def __init__(self, table, pk_field, insert_function, root, fk_fields, teacher_id=None):
        self.table = table
        self.pk_field = pk_field
        self.insert_function = insert_function
        self.root = root
        self.string_vars = {}
        self.table_fields = all_table_fields[table]
        self.fields = list(self.table_fields.keys())
        self.error_msg = tk.StringVar()
        self.fk_fields = fk_fields
        self.teacher_id = teacher_id


    def submit(self):
        self.error_msg.set("")
        self.error_label.config(fg="red")
        values = get_values(self.string_vars, self.table_fields)

        value_list = [values[field] for field in self.fields]

        if not validate_values(values, self.table_fields):
            self.error_msg.set("Please fill in all fields and check the values")
            return

        pk_values = values[self.pk_field] if type(self.pk_field) == type("") else (values[self.pk_field[0]], values[self.pk_field[1]])

        if check_pk(self.table, pk_values, db):
            self.error_msg.set("ID already in use")
            return

        if self.insert_function(value_list, db):
            self.error_msg.set("Submitted successfully")
            self.error_label.configure(fg="Green")


    def get_frame(self):
        fields_frame = tk.Frame(self.root)
        row = 0
        for field in self.fields:
            field_frame = tk.Frame(fields_frame)


            label_text = tk.StringVar()
            label_text.set(all_table_fields[self.table][field]["text"])
            tk.Label(field_frame, textvariable=label_text).grid(row=row, column=0)


            if "user" in self.fk_fields and (field == "Teacher_id" or field == "Student_id" or field == "Admin_id"):
                field_entry = get_fk_user_dropdown(field_frame)
            elif "study" in self.fk_fields and field == "Study_id":
                field_entry = get_fk_study_dropdown(field_frame)
            elif "teacher" in self.fk_fields and (field == "Counselor_id" or field == "Teacher_id"):
                field_entry = get_fk_teacher_dropdown(field_frame)
            elif "course" in self.fk_fields and field == "Course_id":
                field_entry = get_fk_course_dropdown(field_frame)
            elif self.teacher_id and field == "Exam_id":
                field_entry = get_fk_teacher_exams_dropdown(field_frame, self.teacher_id)
            elif "exam" in self.fk_fields and field == "Exam_id":
                field_entry = get_fk_exam_dropdown(field_frame)
            elif "student" in self.fk_fields and field == "Student_id":
                field_entry = get_fk_student_dropdown(field_frame)
            else:
                field_entry = get_entry(self.table_fields[field]["type"], field_frame)

            field_entry[0].grid(row=row, column=1)
            self.string_vars[field] = field_entry[1]

            field_frame.pack()
            row +=1

        self.error_label = tk.Label(fields_frame, textvariable=self.error_msg, fg="red")
        self.error_label.pack()
        tk.Button(fields_frame, text="Submit", command=self.submit).pack()

        return fields_frame

