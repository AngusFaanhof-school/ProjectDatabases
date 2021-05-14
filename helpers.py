import json

from database.database import db, TABLES
from database.select import get_form_fields_from_table

def update_fields():
    table_fields = {}

    for table in TABLES:
        table_fields[table] = get_form_fields_from_table(table, db)

    with open("forms/table_fields.json", "w") as f:
        json.dump(table_fields, f)

    # print(table_fields)

update_fields()