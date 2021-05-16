from tkinter import *
import tkinter.messagebox
import tkinter.ttk as tkrtk
from tkinter import ttk



class Student_tab1:
    #Constructor and allows me to initialize the attributes of this class.
    def __init__(self,root):
        self.root = root
        self.root.title(" Student Login")
        self.root.geometry("1350x800")
        self.root.config(bg = "white")
        self.CreateTAB()
    
    
    def CreateTAB(self):
        notebook = ttk.Notebook(self.root)
        self.TabControl0 = ttk.Frame(notebook)
        self.TabControl1 = ttk.Frame(notebook)
        notebook.add(self.TabControl0, text = "Student Login", )
        notebook.add(self.TabControl1, text = "Student Details", state = "disabled")
        notebook.grid()
        
        def Student_Login():
            u = (self.Username.get())
            p= (self.Password.get())
            if (u == str("abcdef") and p ==str(1234567)):
                self.Username.set("")
                self.Password.set("")
                self.textUsername.focus()
                self.StudentLogin_Window

                
            else:
                tkinter.messagebox.askyesno("Student Login ","You have entered the wrong details. Try again.")
                self.Username.set("")
                self.Password.set("")
                self.textUsername.focus()
       

        self.LoginFrame = Frame(self.TabControl0, relief = RIDGE)
        self.LoginFrame.pack()

        self.Username = StringVar()
        self.Password = StringVar()

        self.lblTitle = Label(self.LoginFrame, text = '\t Student Administrative Login System\t\n', font = ('arial', 30, 'bold'))
        self.lblTitle.grid(row = 0, columnspan=2, pady = 20)
        
        self.LoginFrame1 = LabelFrame(self.LoginFrame, font = ('arial', 20, 'bold'), relief = GROOVE, bd =5)
        self.LoginFrame1.grid(row=1, column=1)

        self.LoginFrame2 = LabelFrame(self.LoginFrame, font = ('arial', 20, 'bold'), relief = GROOVE, bd =5)
        self.LoginFrame2.grid(row = 2, column =1 )



        self.labelUsername = Label(self.LoginFrame1, text = "Username ", font = ('arial', 20, 'bold'), bd =22)
        self.labelUsername.grid(row = 0, column = 0)

        self.textUsername = Entry(self.LoginFrame1, font = ('arial', 20, 'bold'), bd = 7, textvariable = self.Username, width = 34)
        self.textUsername.grid(row = 0, column = 1, padx = 119)

        self.lblPassword = Label(self.LoginFrame1, text = "Password ", font = ('arial', 20, 'bold'), bd =22 )
        self.lblPassword.grid(row = 1, column  = 0)

        self.textPassword = Entry(self.LoginFrame1, font = ('arial', 20, 'bold'), bd = 7, textvariable = self.Password, width = 34 )
        self.textPassword.grid(row = 1, column = 1, columnspan = 2, pady= 30)


        self.btnLogin = Button(self.LoginFrame2, text = 'Login', width = 17, font = ('arial', 20, 'bold'),command = Student_Login)
        self.btnLogin.grid(row = 3, column = 0 , pady = 20, padx = 8)


    def StudentLogin_Window(self):
        self.TabWindow = Toplevel(self.root)
        self.app = Student_Tab2(self.TabWindow)


class Student_Tab2:

    def __init__(self,root):
        self.root = root
        self.root.title(" Student Details")
        self.root.geometry("1350x800")
        self.root.config(background = "white")
        
        self.UI()

    def UI(self):
        notebook = ttk.Notebook(self.root)
        self.TabControl1 = ttk.Frame(notebook)

        notebook.add(self.TabControl1, text = 'Student ')
        notebook.grid()
    
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
        Basic_Frame = Frame(self.TabControl1, bg = "#0000ff") # Have to call the tab control so that the frame fits into the right tab.
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

      


        self.BtnExit = Button(ButtonFrame, text ='Exit', font =('arial', 20, 'bold'), height= 1, width = 10, bd =4, command  = To_Exit )
        self.BtnExit.grid(row = 0, column = 6)

      



if __name__ == '__main__':
    root = Tk()
    application  = Student_tab1(root)
    root.mainloop()




