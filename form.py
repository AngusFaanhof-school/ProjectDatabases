import tkinter as tk
from tkcalendar import DateEntry

class Form:
    def __init__(self, fields, root, submit_function, header=None):
        self.fields = fields
        self.vars = {}
        self.root = root
        self.header = header
        self.submit_function = submit_function

        self.init_frame()

    def init_frame(self):
        form_frame = tk.Frame(self.root)

        def is_integer(inp):
            return inp.isdigit()
                    
        if self.header:
            tk.Label(form_frame, text=self.header).pack()
        
        for field in self.fields.keys():
            field_frame = tk.Frame(form_frame)

            tk.Label(field_frame, text=self.fields[field]["text"]).pack(side=tk.LEFT)

            if self.fields[field]["type"] == "string":
                string_variable = tk.StringVar()
                self.vars[field] = string_variable

                tk.Entry(field_frame, textvariable=string_variable).pack(side=tk.RIGHT)

            elif "enum" in self.fields[field]["type"]:
                options = self.fields[field]["type"].replace("enum-", "").split("/")
                options_variable = tk.StringVar()
                options_variable.set(options[0])
                self.vars[field] = options_variable

                tk.OptionMenu(field_frame, options_variable, *options).pack(side=tk.RIGHT)

            elif self.fields[field]["type"] == "date":
                date_variable = tk.StringVar()
                self.vars[field] = date_variable

                DateEntry(field_frame, textvariable=date_variable, date_pattern="dd/mm/y").pack(side=tk.RIGHT)

            elif self.fields[field]["type"] == "int":
                int_variable = tk.StringVar()
                self.vars[field] = int_variable

                validation = field_frame.register(is_integer)

                tk.Entry(field_frame, textvariable=int_variable, validate="key", validatecommand=(validation, '%S')).pack(side=tk.RIGHT)
            

            field_frame.pack()

        tk.Button(form_frame, text="save", command=self.submit_function).pack()
        self.frame = form_frame
