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
        # form_frame = tk.LabelFrame(self.root, text=self.header, relief=tk.RIDGE)
        # bd=1, width=1000, height=600, padx=20, relief=tk.RIDGE, bg="white", font=('arial', 20, 'bold')
        self.root.geometry("1000x1200")
        form_frame = tk.LabelFrame(self.root, text=self.header, bd=1, width=1000, height=600, padx=20, relief=tk.RIDGE, bg="white", font=('arial', 20, 'bold'))

        def is_integer(inp):
            return inp.isdigit()

        current_row = 0

        for field in self.fields.keys():
            field_frame = tk.Frame(form_frame)

            # tk.Label(field_frame, text=self.fields[field]["text"]).pack(side=tk.LEFT)
            tk.Label(field_frame, font=('arial', 20, 'bold'), text=self.fields[field]["text"], padx=2, pady=2, bg="white").grid(row=current_row, column=0, sticky=tk.W)

            if self.fields[field]["type"] == "string":
                string_variable = tk.StringVar()
                self.vars[field] = string_variable

                tk.Entry(field_frame, font=('arial', 20, 'bold'), textvariable=string_variable).grid(row=current_row, column=1)
                # self.txtStdID.grid(row = 0, column = 1 )


                # tk.Entry(field_frame, textvariable=string_variable).pack(side=tk.RIGHT)

            # elif "enum" in self.fields[field]["type"]:
            #     options = self.fields[field]["type"].replace("enum-", "").split("/")
            #     options_variable = tk.StringVar()
            #     options_variable.set(options[0])
            #     self.vars[field] = options_variable

            #     tk.OptionMenu(field_frame, options_variable, *options).pack(side=tk.RIGHT)

            # elif self.fields[field]["type"] == "date":
            #     date_variable = tk.StringVar()
            #     self.vars[field] = date_variable

            #     DateEntry(field_frame, textvariable=date_variable, date_pattern="dd/mm/y").pack(side=tk.RIGHT)

            # elif self.fields[field]["type"] == "int":
            #     int_variable = tk.StringVar()
            #     self.vars[field] = int_variable

            #     validation = field_frame.register(is_integer)

            #     tk.Entry(field_frame, textvariable=int_variable, validate="key", validatecommand=(validation, '%S')).pack(side=tk.RIGHT)

            current_row += 1

            field_frame.pack()

        tk.Button(form_frame, text="save", command=self.submit_function).pack()
        self.frame = form_frame


        # self.lblStdID = Label(LeftDataFrame, font = ('arial', 20, 'bold'), text = "Student ID", padx =2, pady=2, bg="white")
        # self.lblStdID.grid(row=0, column=0, sticky=W)
        # self.txtStdID = Entry(LeftDataFrame, font = ('arial', 20, 'bold'), textvariable = StdID, width = 39)
        # self.txtStdID.grid(row = 0, column = 1 )