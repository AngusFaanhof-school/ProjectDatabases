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
        Firstname = StringVar()
        Surname = StringVar()
        Dob = StringVar()
        Age = StringVar()
        Mobile = StringVar()
        Post_Code = StringVar()
        Grades = StringVar()



        #Creates frame and some buttons,labels  for the main window etc. 
        Basic_Frame = Frame(self.root, bg = "#0000ff")
        Basic_Frame.grid()

        Title_Frame = Frame(Basic_Frame, bd = 2, padx = 54, pady = 8, bg= "#FFFFFF", relief = GROOVE)
        Title_Frame.pack(side=TOP)
        
        self.Title_label = Label(Title_Frame, font = ('arial', 40, 'bold'), text = "Administration system", bg = "white")
        self.Title_label.grid()
        
        ButtonFrame = Frame(Basic_Frame, bd=2, width = 1350, height = 70, padx=18, pady=10, bg="white", relief = GROOVE)
        ButtonFrame.pack(side=BOTTOM)
        
        DataFrame = Frame(Basic_Frame, bd = 1, width = 1300, height = 400, padx=20, pady = 20, relief = GROOVE, bg="blue")
        DataFrame.pack(side = BOTTOM)
        
        LeftDataFrame = LabelFrame(DataFrame, bd = 1, width =1000, height = 600, padx = 20, relief = RIDGE,bg="white", font = ('arial', 20, 'bold'), text = "student info\n")
        LeftDataFrame.pack(side = LEFT)

        RightDataFrame = LabelFrame(DataFrame, bd = 1, width = 450, height =300, padx =31, pady=3, relief = GROOVE, bg = "white", font = ('arial', 20, 'bold'), text = "student details\n")
        RightDataFrame.pack(side = RIGHT)


        



        


if __name__=='__main__':
    root = Tk()
    MainWindow = Student(root)
    root.mainloop()

    

    

    















