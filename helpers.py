import json
import re

from database import db
from database_module.select import get_fields
from database_module.helpers import get_fields_overview

cursor = db.cursor()
cursor.execute("show tables")
tables = [table[0] for table in cursor.fetchall()]

def update_fields():
    table_fields = {}

    for table in tables:
        fields = get_fields_overview(table, db)
        table_fields[table] = {}

        for field in fields:
            temp = {}
            field_type = field[1].decode('utf-8')

            if "char" in field_type:
                temp["type"] = "string-" +  re.findall('[0-9]+', field_type)[0]
            elif field_type == "tinyint(4)":
                     temp["type"] = "bool"
            elif "int" in field_type:
                temp["type"] = "int-" +  re.findall('[0-9]+', field_type)[0]
            else:
                temp["type"] = field_type

            temp["null"] = False if field[2] == "NO" else True
            temp["key"] = field[3]
            temp["text"] = "{FILL}"
            table_fields[table][field[0]] = temp

    with open("forms/table_fields.json", "w") as f:
        json.dump(table_fields, f)

update_fields()