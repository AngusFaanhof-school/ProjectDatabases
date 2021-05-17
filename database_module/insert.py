import mysql.connector

def insert(statement, data, db):
    cursor = db.cursor()

    try:
        cursor.execute(statement, data)
    except mysql.connector.Error as err:
        if err.errno == 1062:
            return False

    db.commit()
    return True

def add_user(data, db):
    """
    Add a user by supplying a tuple of the values
    Returns False if the id already exists and true if it worked
    Example user_data: (1, "pass", "First", "Last", 2000-01-01, "Dutch", "Street", 1, "1234AB", "City", "0612345678", "name@email.com", "M")
    """

    statement = "INSERT INTO user VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    return insert(statement, data, db)

def add_administrator(data, db):
    """
    Add an administrator by supplying a tuple of the values
    Returns False if the id already exists and true if it worked
    Example data: (1)
    """

    statement = "INSERT INTO administrator VALUES (%s)"

    return insert(statement, data, db)

def add_teacher(data, db):
    """
    Add a teacher by supplying a tuple of the values
    Returns False if the id already exists and true if it worked
    Example data: (1, 20000, 0)
    """

    statement = "INSERT INTO teachers VALUES (%s, %s, %s)"

    return insert(statement, data, db)

def add_student(data, db):
    """
    Add a student by supplying a tuple of the values
    Returns False if the id already exists and true if it worked
    Example data: (1, "11AA", 2017, 1115)
    """

    statement = "INSERT INTO students VALUES (%s, %s, %s, %s)"

    return insert(statement, data, db)

def add_course(data, db):
    # NOTE: update course table to remove redundancy
    """
    Add a course by supplying a tuple of the values
    Returns False if the id already exists and true if it worked
    Example data: ("Math", "introduction", "Mathematical Engineering", 1111, 4, "11AA", "0011A")
    """

    statement = "INSERT INTO course VALUES (%s, %s, %s, %s, %s, %s, %s)"

    return insert(statement, data, db)

def add_exam(data, db):
    """
    Add an exam by supplying a tuple of the values
    Returns False if the id already exists and true if it worked
    Example data: ("6666DM1", "0011A", "A45", 0, "2017-08-02 14:00:00", 2)
    """

    statement = "INSERT INTO exams VALUES (%s, %s, %s, %s, %s, %s)"

    return insert(statement, data, db)

def add_result(data, db):
    """
    Add a result by supplying a tuple of the values
    Returns False if the id already exists and true if it worked
    Example data: ("6666DM1", 6665, 8, 1)
    """

    statement = "INSERT INTO results VALUES (%s, %s, %s, %s)"

    return insert(statement, data, db)

def add_study(data, db):
    """
    Add a study by supplying a tuple of the values
    Returns False if the id already exists and true if it worked
    Example data: ("Business ICT", "for management studies", "Dutch", 4, "11AA")
    """

    statement = "INSERT INTO study VALUES (%s, %s, %s, %s, %s)"

    return insert(statement, data, db)