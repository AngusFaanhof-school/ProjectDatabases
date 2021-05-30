import tkinter as tk
import json

import database_module.select as select
from database import db

f = open("forms/table_fields.json", "r")
fields = json.load(f)


def add_table_cell(root, text, row, column):
    entry = tk.Entry(root)
    entry.insert(0, text)
    entry.grid(row=row, column=column)
    entry.config(state='disabled')


def all_users(root):
    field_list = list(fields["user"].keys())
    users = select.get_all("user", db)
    users_frame = tk.Frame(root)

    for column in range(len(field_list)):
        add_table_cell(users_frame, field_list[column], 0, column)

    for row in range(len(users)):
        for column in range(len(field_list)):
            add_table_cell(users_frame, users[row][field_list[column]], row+1, column)

    return users_frame


def all_teachers(root):
    field_list = ["user.First_name", "user.Last_name"] + list(fields["teachers"].keys())
    teachers = select.get_all("teachers", db)
    teacher_frame = tk.Frame(root)

    for column in range(len(field_list)):
        text = field_list[column]
        if "." in text:
            text = text.split(".")[1]
        add_table_cell(teacher_frame, text, 0, column)

    for row in range(len(teachers)):
        user = select.get_specific("user", teachers[row]["Teacher_id"], db)
        for column in range(len(field_list)):
            if "." in field_list[column]:
                text = user[field_list[column].split(".")[1]]
            elif field_list[column] == "Studycounselor":
                text = "Yes" if teachers[row][field_list[column]] else "No"
            else:
                text = teachers[row][field_list[column]]
            add_table_cell(teacher_frame, text, row+1, column)

    return teacher_frame


def all_admins(root):
    field_list = ["user.First_name", "user.Last_name"] + list(fields["administrator"].keys())
    admins = select.get_all("administrator", db)
    admin_frame = tk.Frame(root)

    for column in range(len(field_list)):
        text = field_list[column]
        if "." in text:
            text = text.split(".")[1]
        add_table_cell(admin_frame, text, 0, column)

    for row in range(len(admins)):
        user = select.get_specific("user", admins[row]["Admin_id"], db)
        for column in range(len(field_list)):
            if "." in field_list[column]:
                text = user[field_list[column].split(".")[1]]
            else:
                text = admins[row][field_list[column]]
            add_table_cell(admin_frame, text, row+1, column)

    return admin_frame


def all_students(root):
    field_list = ["user.First_name", "user.Last_name", "study.study_name", "teacher.Teacher_id"] + list(fields["students"].keys())
    field_list.remove("Study_id")
    field_list.remove("Counselor_id")

    students = select.get_all("students", db)
    student_frame = tk.Frame(root)

    for column in range(len(field_list)):
        text = field_list[column]
        if "." in text:
            text = text.split(".")[1]
        add_table_cell(student_frame, text, 0, column)

    for row in range(len(students)):
        user = select.get_specific("user", students[row]["Student_id"], db)
        study = select.get_specific("study", students[row]["Study_id"], db)
        teacher = select.get_specific("user", students[row]["Counselor_id"], db)

        for column in range(len(field_list)):
            if "user." in field_list[column]:
                text = user[field_list[column].split(".")[1]]
            elif "study." in field_list[column]:
                text = study[field_list[column].split(".")[1]]
            elif "teacher." in field_list[column]:
                text = teacher["First_name"] + " " + teacher["Last_name"]
            else:
                text = students[row][field_list[column]]
            add_table_cell(student_frame, text, row+1, column)

    return student_frame


def teacher_students(root, teacher_id):
    student_fields = ["Student_id", "Student_name", "Study_id", "Start_year"]
    teacher_students = select.get_all_from_field_with_value("students", "Counselor_id", teacher_id, db)

    student_frame = tk.Frame(root)

    for column in range(len(student_fields)):
        text = student_fields[column]
        add_table_cell(student_frame, text, 0, column)

    for row in range(len(teacher_students)):
        for column in range(len(student_fields)):
            if student_fields[column] == "Study_id":
                text = select.get_specific("study", teacher_students[row][student_fields[column]], db)["study_name"]
            elif student_fields[column] == "Student_name":
                student = select.get_specific("user", teacher_students[row]["Student_id"], db)
                text = student["First_name"] + " " + student["Last_name"]
            else:
                text = teacher_students[row][student_fields[column]]
            add_table_cell(student_frame, text, row+1, column)

    return student_frame


def all_studies(root):
    field_list = list(fields["study"].keys())
    studies = select.get_all("study", db)
    studies_frame = tk.Frame(root)

    for column in range(len(field_list)):
        add_table_cell(studies_frame, field_list[column], 0, column)

    for row in range(len(studies)):
        for column in range(len(field_list)):
            add_table_cell(studies_frame, studies[row][field_list[column]], row+1, column)

    return studies_frame


def all_courses(root):
    field_list = ["study.study_name", "teacher.Teacher_id"] + list(fields["course"].keys())
    field_list.remove("Study_id")
    field_list.remove("Teacher_id")

    courses = select.get_all("course", db)
    course_frame = tk.Frame(root)

    for column in range(len(field_list)):
        text = field_list[column]
        if "." in text:
            text = text.split(".")[1]
        add_table_cell(course_frame, text, 0, column)

    for row in range(len(courses)):
        study = select.get_specific("study", courses[row]["Study_id"], db)
        teacher = select.get_specific("user", courses[row]["Teacher_id"], db)

        for column in range(len(field_list)):
            if "study." in field_list[column]:
                text = study[field_list[column].split(".")[1]]
            elif "teacher." in field_list[column]:
                text = teacher["First_name"] + " " + teacher["Last_name"]
            else:
                text = courses[row][field_list[column]]
            add_table_cell(course_frame, text, row+1, column)

    return course_frame


def teacher_courses(root, teacher_id):
    coures_fields = ["Course_name", "Course_Description", "Study_id", "course_id"]
    teacher_courses = select.get_all_from_field_with_value("course", "Teacher_id", teacher_id, db)

    course_frame = tk.Frame(root)

    for column in range(len(coures_fields)):
        text = coures_fields[column]
        add_table_cell(course_frame, text, 0, column)

    for row in range(len(teacher_courses)):
        for column in range(len(coures_fields)):
            if coures_fields[column] == "Study_id":
                text = select.get_specific("study", teacher_courses[row][coures_fields[column]], db)["study_name"]
            else:
                text = teacher_courses[row][coures_fields[column]]
            add_table_cell(course_frame, text, row+1, column)

    return course_frame


def all_exams(root):
    field_list = ["course.Course_name"] + list(fields["exams"].keys())
    field_list.remove("Course_id")

    exams = select.get_all("exams", db)
    exam_frame = tk.Frame(root)

    for column in range(len(field_list)):
        text = field_list[column]
        if "." in text:
            text = text.split(".")[1]
        add_table_cell(exam_frame, text, 0, column)

    for row in range(len(exams)):
        course = select.get_specific("course", exams[row]["Course_id"], db)

        for column in range(len(field_list)):
            if "course." in field_list[column]:
                text = course[field_list[column].split(".")[1]]
            elif field_list[column] == "Resit":
                text = "Yes" if exams[row][field_list[column]] else "No"
            else:
                text = exams[row][field_list[column]]
            add_table_cell(exam_frame, text, row+1, column)

    return exam_frame


def all_results(root):
    field_list = ["exams.Exam_id", "students.Student_id"] + list(fields["results"].keys())
    field_list.remove("Student_id")
    field_list.remove("Exam_id")

    results = select.get_all("results", db)
    result_frame = tk.Frame(root)

    for column in range(len(field_list)):
        text = field_list[column]
        if "." in text:
            text = text.split(".")[1]
        add_table_cell(result_frame, text, 0, column)

    for row in range(len(results)):
        exam = select.get_specific("exams", results[row]["Exam_id"], db)
        student = select.get_specific("user", results[row]["Student_id"], db)

        for column in range(len(field_list)):
            if "exams." in field_list[column]:
                text = exam[field_list[column].split(".")[1]]
            elif "students." in field_list[column]:
                text = student["First_name"] + " " + student["Last_name"]
            elif field_list[column] == "Passed":
                text = "Yes" if results[row][field_list[column]] else "No"
            else:
                text = results[row][field_list[column]]
            add_table_cell(result_frame, text, row+1, column)

    return result_frame


def teacher_students_results(root, teacher_id):
    field_list = ["Student_id", "Student_name", "Exam_id", "Grade", "Passed"]

    teacher_students = select.get_all_from_field_with_value("students", "Counselor_id", teacher_id, db)
    teacher_student_ids = [student["Student_id"] for student in teacher_students]

    field_frame = tk.Frame(root)

    for column in range(len(field_list)):
        add_table_cell(field_frame, field_list[column], 0, column)


    teacher_students_results = {}
    for student_id in teacher_student_ids:
        teacher_students_results[student_id] = select.get_all_from_field_with_value("results", "Student_id", student_id, db)

    current_row = 1
    for student in teacher_students_results:
        student_user = select.get_specific("user", student, db)

        for row in range(len(teacher_students_results[student])):
            for column in range(len(field_list)):
                if field_list[column] == "Student_name":
                    text = student_user["First_name"] + " " + student_user["Last_name"]
                elif field_list[column] == "Passed":
                    text = "Yes" if teacher_students_results[student][row][field_list[column]] else "No"
                else:
                    text = teacher_students_results[student][row][field_list[column]]
                add_table_cell(field_frame, text, current_row, column)
            current_row += 1

    return field_frame


def student_courses(root, student_id):
    field_list = ["course_id", "Course_name", "Course_Description", "Teacher_name", "Credits"]

    study = select.get_specific("students", student_id, db)["Study_id"]
    courses = select.get_all_from_field_with_value("course", "Study_id", study, db)

    field_frame = tk.Frame(root)

    for column in range(len(field_list)):
        add_table_cell(field_frame, field_list[column], 0, column)

    for row in range(len(courses)):
        teacher = select.get_specific("user", courses[row]["Teacher_id"], db)
        for column in range(len(field_list)):
            if field_list[column] == "Teacher_name":
                text = "{} {}".format(teacher["First_name"], teacher["Last_name"])
            else:
                text = courses[row][field_list[column]]
            add_table_cell(field_frame, text, row+1, column)


    return field_frame


def student_results(root, student_id):
    field_list = ["Exam_id", "Grade", "Passed"]

    field_frame = tk.Frame(root)

    results = select.get_all_from_field_with_value("results", "Student_id", student_id, db)

    for column in range(len(field_list)):
         add_table_cell(field_frame, field_list[column], 0, column)

    for row in range(len(results)):
        for column in range(len(field_list)):
            if field_list[column] == "Passed":
                text = "Yes" if results[row][field_list[column]] else "No"
            else:
                text = results[row][field_list[column]]
            add_table_cell(field_frame, text, row+1, column)

    return field_frame


def student_study_counselor(root, student_id):
    field_list = ["teacher_name", "Phone_number", "email"]

    field_frame = tk.Frame(root)

    counselor = select.get_specific("students", student_id, db)["Counselor_id"]
    teacher = select.get_specific("user", counselor, db)

    for column in range(len(field_list)):
        add_table_cell(field_frame, field_list[column], 0, column)


    for column in range(len(field_list)):
        if field_list[column] == "teacher_name":
            text = "{} {}".format(teacher["First_name"], teacher["Last_name"])
        else:
            text = teacher[field_list[column]]
        add_table_cell(field_frame, text, 1, column)

    return field_frame
