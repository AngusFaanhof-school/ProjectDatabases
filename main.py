#The FrontEnd


from tkinter import *
import tkinter.messagebox

class Student:
    #Constructor and allows me to initialize the attributes of this class. 
    def __init__(self,root):
        self.root = root
        self.root.title(" Administration system")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg = "#0000ff")

        #Creating variables and assigning them an empty value
        first_name = StringVar()
        last_name = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Phone = StringVar()
        postal_Code = StringVar()
        Grades = StringVar()
        Nationality = StringVar()


        #Creates frame and some buttons,labels  for the main window etc. 
        Basic_Frame = Frame(self.root, bg = "#0000ff")
        Basic_Frame.grid()

        Title_Frame = Frame(Basic_Frame, bd = 2, padx = 54, pady = 8, bg= "#FFFFFF", relief = GROOVE)
        Title_Frame.pack(side=TOP)
        
        self.Title_label = Label(Title_Frame, font = ('arial', 40, 'bold'), text = "Administration system", bg = "white")
        self.Title_label.grid()

        

        


if __name__=='__main__':
    root = Tk()
    MainWindow = Student(root)
    root.mainloop()

    

    

    















