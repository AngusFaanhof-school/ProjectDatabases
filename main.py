from tkinter import *
import tkinter.messagebox

def main():
    master = Tk()
    app = Login_System(master)


class Login_System:
    #Constructor and allows me to initialize the attributes of this class.
    def __init__(self,root):
        self.root = root
        self.root.title(" Administrative system")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg = "#0000ff")
        self.frame = Frame(self.root, bg = 'blue')
        self.frame.pack()

        self.Username = StringVar()
        self.password = StringVar()

        self.lblTitle = Label(self.frame, text = 'Student Login', font = ('arial', 50, 'bold'), bg = 'blue' ,fg = 'black')
        self.lblTitle.grid(row = 0, column = 0 , columnspan = 2, pady = 40)
        
        self.btnLogin = Button(self.frame, text = 'Login', width = 17, command = self.new_Window)
        self.btnLogin.grid(row = 3, column = 0 )



    def To_Login(self):
        u = (self.Username.get())
        p= (self.password.get())
        if (u == str(628492) and p ==str(1234567)):
            self.newWindow = Toplevel(self.root)
            self.app = Student(self.newWindow)
        else:
            tkinter.messagebox.askyesno("Student Login ","You have entered the wrong details. Try again.")
            self.Username.set("")
            self.password.set("")
    
    def new_Window(self):
        self.newWindow = Toplevel(self.root)
        self.app = Student(self.newWindow)
        
class Student:
    #Constructor and allows me to initialize the attributes of this class.
    def __init__(self,root):
        self.root = root
        self.root.title(" Administrative system")
        self.root.geometry("1350x750+0+0")
        self.root.config(bg = "#0000ff")


        #Created function if  user wants to Exit the Program
        def To_Exit():
            To_Exit = tkinter.messagebox.askyesno("Student Administrative.", "Confirm if you want to exit.")
            if To_Exit > 0:
                root.destroy()
                return



        #Creating variables and assigning them an empty value
        StdID= StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        DoB =  StringVar()
        Age = StringVar()
        Mobile = StringVar()
        Post_Code = StringVar()
        Grades = StringVar()
        City = StringVar()
        Nationality = StringVar()
        Email_Address = StringVar()









        #Creates frame and some buttons,labels  for the main window etc. Frame works like a container and helps me organise the widgets and listboxes etc.
        Basic_Frame = Frame(self.root, bg = "#0000ff")
        Basic_Frame.grid()

        Title_Frame = Frame(Basic_Frame, bd = 2, padx = 54, pady = 8, bg= "#FFFFFF", relief = GROOVE)
        Title_Frame.pack(side=TOP)

        self.Title_label = Label(Title_Frame, font = ('arial', 40, 'bold'), text = "Administrative system", bg = "white")
        self.Title_label.grid()

        ButtonFrame = Frame(Basic_Frame, bd=2, width = 1350, height = 70, padx=18, pady=10, bg="white", relief = GROOVE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(Basic_Frame, bd = 1, width = 1300, height = 400, padx=20, pady = 20, relief = GROOVE, bg="blue")
        DataFrame.pack(side = BOTTOM)

        LeftDataFrame = LabelFrame(DataFrame, bd = 1, width =1000, height = 600, padx = 20, relief = RIDGE,bg="white", font = ('arial', 20, 'bold'), text = "Student info\n")
        LeftDataFrame.pack(side = LEFT)

        RightDataFrame = LabelFrame(DataFrame, bd = 1, width = 450, height =300, padx =31, pady=3, relief = GROOVE, bg = "white", font = ('arial', 20, 'bold'), text = "Student details\n")
        RightDataFrame.pack(side = RIGHT)

        #Create update, newbuttons here.
        self.lblStdID = Label(LeftDataFrame, font = ('arial', 20, 'bold'), text = "Student ID", padx =2, pady=2, bg="white")
        self.lblStdID.grid(row=0, column=0, sticky=W)
        self.txtStdID = Entry(LeftDataFrame, font = ('arial', 20, 'bold'), textvariable = StdID, width = 39)
        self.txtStdID.grid(row = 0, column = 1 )

        self.lblfna = Label(LeftDataFrame, font = ('arial', 20, 'bold'), text = "Firstname", padx =2, pady=2, bg="white")
        self.lblfna.grid(row=1, column=0, sticky=W)
        self.txtfna = Entry(LeftDataFrame, font = ('arial', 20, 'bold'), textvariable = StdID, width = 39)
        self.txtfna.grid(row = 1, column = 1 )

        self.lblsname = Label(LeftDataFrame, font = ('arial', 20, 'bold'), text = "Surname", padx =2, pady=2, bg="white")
        self.lblsname.grid(row=2, column=0, sticky=W)
        self.txtsname = Entry(LeftDataFrame, font = ('arial', 20, 'bold'), textvariable = StdID, width = 39)
        self.txtsname.grid(row = 2, column = 1 )

        self.lblDob = Label(LeftDataFrame, font = ('arial', 20, 'bold'), text = "DoB", padx =2, pady=2, bg="white")
        self.lblDob.grid(row=3, column=0, sticky=W)
        self.txtDob = Entry(LeftDataFrame, font = ('arial', 20, 'bold'), textvariable = DoB, width = 39)
        self.txtDob.grid(row = 3, column = 1 )

        self.lblage = Label(LeftDataFrame, font = ('arial', 20, 'bold'), text = "Age", padx =2, pady=2, bg="white")
        self.lblage.grid(row=4, column=0, sticky=W)
        self.txtage = Entry(LeftDataFrame, font = ('arial', 20, 'bold'), textvariable = Age, width = 39)
        self.txtage.grid(row = 4, column = 1 )

        self.lblMobile = Label(LeftDataFrame, font = ('arial', 20, 'bold'), text = "Mobile", padx =2, pady=2, bg="white")
        self.lblMobile.grid(row=5, column=0, sticky=W)
        self.txtMobile = Entry(LeftDataFrame, font = ('arial', 20, 'bold'), textvariable = Mobile, width = 39)
        self.txtMobile.grid(row = 5, column = 1 )




        self.btnAddDate = Button(ButtonFrame, font = ('arial', 20, 'bold'), text = "Add New", height = 1,width = 10 ,bd = 4)
        self.btnAddDate.grid(row = 0, column = 0 )


        self.BtnExit = Button(ButtonFrame, text ='Exit', font =('arial', 20, 'bold'), height= 1, width = 10, bd =4, command  = To_Exit )
        self.BtnExit.grid(row = 0, column = 6)


if __name__=='__main__':
    main()
