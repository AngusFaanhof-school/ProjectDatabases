def login(user_id, password, db):
    """
    Returns true if a match is found between a user_id and password
    Returns false if the user_id is not found
    """
    cursor = db.cursor()
    cursor.execute('SELECT Password FROM user WHERE id=(%s)', [(user_id)])

    data = cursor.fetchone()

    if not data:
        return False

    real_password = data[0]

    if password != real_password:
        return False

    return True


def get_role(user_id, db):
    """
    Returns the role of a user_id
    Returns none if the user_id has no role
    """
    cursor = db.cursor()
    cursor.execute('SELECT Admin_id FROM administrator WHERE Admin_id=(%s)', [(user_id)])

    if cursor.fetchone():
        return "Administrator"

    cursor.execute('SELECT Teacher_id FROM teachers WHERE Teacher_id=(%s)', [(user_id)])

    if cursor.fetchone():
        return "Teacher"

    cursor.execute('SELECT Student_id FROM students WHERE Student_id=(%s)', [(user_id)])

    if cursor.fetchone():
        return "Student"

    return None