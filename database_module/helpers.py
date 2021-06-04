def check_pk(table, pk, db):
    cursor = db.cursor()

    id_field = "id"
    params = "%s"

    if table == "results":
        id_field = "(Exam_id, Student_id)"
        params = "(%s, %s)"
    elif table == "administrator":
        id_field = "Admin_id"
    elif table == "course":
        id_field = "Course_id"
    elif table == "exams":
        id_field = "Exam_id"
    elif table == "students":
        id_field = "Student_id"
    elif table == "study":
        id_field = "Study_id"
    elif table == "teachers":
        id_field = "Teacher_id"

    if type(pk) != type((1,)):
        pk = (pk, )

    cursor.execute(f"select * from {table} where {id_field} = {params}", pk)

    if cursor.fetchone():
        return True
    return False


def get_fields_overview(table, db):
    cursor = db.cursor()

    cursor.execute(f"desc {table}")
    return cursor.fetchall()


def get_full_name(id, db):
    cursor = db.cursor()

    cursor.execute("select First_name, Last_name from user where id = %s", (id, ))
    result = cursor.fetchone()

    return " ".join(result)