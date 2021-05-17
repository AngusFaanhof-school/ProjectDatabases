def get_fields(table, db):
    fields = []

    cursor = db.cursor()

    cursor.execute(f"desc {table}")
    result = cursor.fetchall()

    for field in result:
        fields.append(field[0])

    return fields


def get_all(table, db):
    data = []
    fields = get_fields(table, db)

    cursor = db.cursor()
    cursor.execute(f"select * from {table}")

    result = cursor.fetchall()

    for entry in result:
        temp_obj = {}

        for field_index in range(0, len(entry)):
            temp_obj[fields[field_index]] = entry[field_index]

        data.append(temp_obj)

    return data


def get_specific(table, id, db):
    fields = get_fields(table, db)

    specific_obj = {}

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

    if type(id) != type((1,)):
        id = (id, )

    cursor = db.cursor()

    cursor.execute(f"select * from {table} where {id_field} = {params}", id)

    result = cursor.fetchone()

    if result:
        for field_index in range(0, len(result)):
            specific_obj[fields[field_index]] = result[field_index]

    return specific_obj


def get_all_from_field(table, field, id, db):
    fields = get_fields(table, db)

    objects = []

    cursor = db.cursor()

    cursor.execute(f"select * from {table} where {field} = {id}")

    result = cursor.fetchall()

    if result:
        for r in result:
            temp_obj = {}
            for field_index in range(0, len(r)):
                temp_obj[fields[field_index]] = r[field_index]
            objects.append(temp_obj)

    return objects