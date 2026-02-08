from tkinter import *
from tkinter import ttk



class LibraryManagementSystem:
    def __init__(self, root):  
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1540x800+0+0")


        lbltitle = Label(self.root,text="📚LIBRARY MANAGEMENT SYSTEM",bg="powder blue",fg="red",bd=20,relief=RIDGE,font=("Times New Roman", 50, "bold"),padx=2,pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0, y=130,width=1530,height=400)
                        
        
        #========================DataFrameLeft============================
        DataFrameLeft=LabelFrame(frame,text="Library Membership Information",bg="powder blue",fg="red",bd=20,relief=RIDGE,font=("Times New Roman",12, "bold"))
        DataFrameLeft.place(x=0, y=5, width=900,height=350)

        lblMember=Label(DataFrameLeft,bg="powder blue",text="Member Type",fg="Dark blue",font=("arial",15,"bold"),padx=2,pady=4)
        lblMember.grid(row=0,column=0,sticky=W)

        comMember = ttk.Combobox(DataFrameLeft,state="readonly",font=("arial",12,"bold"),width=27)

        comMember["values"] = ("Admin Staff", "Student", "Lecturer")
        comMember.current(0)
        comMember.grid(row=0, column=1)

        lblPRN_NO=Label(DataFrameLeft,bg="powder blue",text="PRN NO:",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblPRN_NO.grid(row=1,column=0,sticky=W)
        txtPRN_NO=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtPRN_NO.grid(row=1,column=1)

        lblTitle=Label(DataFrameLeft,bg="powder blue",text="ID NO:",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtTitle.grid(row=2,column=1)

        lblFirstName=Label(DataFrameLeft,bg="powder blue",text="First Name",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblFirstName.grid(row=3,column=0,sticky=W)
        txtFirstName=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtFirstName.grid(row=3,column=1)

        lblLastName=Label(DataFrameLeft,bg="powder blue",text="Last Name",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblLastName.grid(row=4,column=0,sticky=W)
        txtLastName=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtLastName.grid(row=4,column=1)


        lblAddress1=Label(DataFrameLeft,bg="powder blue",text="Address1",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtAddress1.grid(row=5,column=1)

        lblAddress2=Label(DataFrameLeft,bg="powder blue",text="Address2",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtAddress2.grid(row=6,column=1)

        lblPostCode=Label(DataFrameLeft,bg="powder blue",text="Post Code",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtPostCode.grid(row=7,column=1)

        lblMobile=Label(DataFrameLeft,bg="powder blue",text="Mobile",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtMobile.grid(row=8,column=1)

        lblBookID=Label(DataFrameLeft,bg="powder blue",text="Book ID:",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblBookID.grid(row=0,column=2,sticky=W)
        txtBookID=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtBookID.grid(row=0,column=3)

        lblBookTitle=Label(DataFrameLeft,bg="powder blue",text="Book Title",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtBookTitle.grid(row=1,column=3)

        lblAuther=Label(DataFrameLeft,bg="powder blue",text="Auther Name",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtAuther.grid(row=2,column=3)
        
        lblDateBorrowed=Label(DataFrameLeft,bg="powder blue",text="Date Borrowed:",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDateBorrowed.grid(row=3,column=3)

        lblDateDue=Label(DataFrameLeft,bg="powder blue",text="Date Due:",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDateDue.grid(row=4,column=3)

        lblDaysOnBook=Label(DataFrameLeft,bg="powder blue",text="Days On Book:",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDaysOnBook.grid(row=5,column=3)
        
        lblLateRerunFine=Label(DataFrameLeft,bg="powder blue",text="Late Return Fine:",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblLateRerunFine.grid(row=6,column=2,sticky=W)
        txtLateRerunFine=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtLateRerunFine.grid(row=6,column=3)

        lblDateOverDue=Label(DataFrameLeft,bg="powder blue",text="Date Over Due:",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblDateOverDue.grid(row=7,column=2,sticky=W)
        txtDateOverDue=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtDateOverDue.grid(row=7,column=3)

        lblActualPrice=Label(DataFrameLeft,bg="powder blue",text="Actual Price:",fg="Dark blue",font=("arial",12,"bold"),padx=2,pady=4)
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLeft,font=("arial",12,"bold"),width=29)
        txtActualPrice.grid(row=8,column=3)

        #========================DataFrameRight========================
        DataFrameRight=LabelFrame(frame,text="Book Details",bg="powder blue",fg="red",bd=20,relief=RIDGE,font=("arial",12, "bold"))
        DataFrameRight.place(x=910, y=5, width=560,height=350)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=4)
        self.txtBox.grid(row=0,column=2)

        listScrollbar=Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0,column=1,sticky="ns")

        listBooks=['Python Prograaming','Java Programming','Data Science','Data Analyst','SQL Workbranch','AWS Cloud','DevOps','Structure Interpretation of Computer Programs','The C Programming Language','Hackers',
                   'Design Patterns',' Deopvs Continuous delivery','UNIX and Linux System Administration','High Performance MySQL: Optimization, Backups, and Replication',"Python Programming",
                   "Java Programming",
                   "C Programming",
                   "C++ Programming",
                   "Data Science",
                   "Data Analyst",
                   "SQL Workbench",
                   "MySQL Database",
                   "Oracle Database",
                   "AWS Cloud",
                   "DevOps",
                   "Linux Administration",
                   "UNIX and Linux System Administration",
                   "Docker & Kubernetes",
                   "Git and GitHub",
                   "Software Engineering",
                   "Operating System",
                   "Computer Networks",
                   "Data Structures and Algorithms",
                   "Design Patterns",
                   "Clean Code",
                   "Structure and Interpretation of Computer Programs",
                   "The C Programming Language",
                   "High Performance MySQL",
                   "Ethical Hacking",
                   "Cyber Security"]
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.grid(row=0,column=0,padx=4)
        listScrollbar.config(command=listBox.yview)

        for item in listBooks:
            listBox.insert(END,item)

        #==============================Buttons Frame===================
        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=15,bg="powder blue")
        Framebutton.place(x=0, y=530,width=1530,height=70)

        btnPrescription=Button(Framebutton,text="Add Data",fg="white",bg="blue",font=("arial",12,"bold"),width=23,height=2,padx=0,pady=0)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Framebutton,text="Show Data",fg="white",bg="blue",font=("arial",12,"bold"),width=23,height=2,padx=0,pady=0)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Framebutton,text="Update",fg="white",bg="blue",font=("arial",12,"bold"),width=23,height=2,padx=0,pady=0)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Framebutton,text="Delete",fg="white",bg="blue",font=("arial",12,"bold"),width=24,height=2,padx=0,pady=0)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Framebutton,text="Reset",fg="white",bg="blue",font=("arial",12,"bold"),width=25,height=2,padx=0,pady=0)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Framebutton,text="Exit",fg="white",bg="blue",font=("arial",12,"bold"),width=25,height=2,padx=0,pady=0)
        btnExit.grid(row=0,column=5)

        #====================Information===============================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0, y=600,width=1530,height=195)


        TableFrame=Frame(FrameDetails,relief=RIDGE,bg="powder blue",bd=6)
        TableFrame.place(x=0,y=0,width=1460,height=170)

        xscroll=ttk.Scrollbar(TableFrame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(TableFrame,orient=VERTICAL)

        self.libraryTable=ttk.Treeview(TableFrame,columns=("Member Type","PRN NO:","ID NO:","First Name","Last Name","Address1","Address2","Post Code","Mobile","Book ID:",
                                       "Book Title", "Author Name","Date Borrowed:","Date Due:","Days On Book:","Late Return Fine:","Date Over Due:","Actual Price:"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.libraryTable.xview)
        yscroll.config(command=self.libraryTable.yview)

        self.libraryTable.heading("Member Type",text="Member Type")
        self.libraryTable.heading("PRN NO:",text="PRN NO:")
        self.libraryTable.heading("ID NO:",text="ID NO:")
        self.libraryTable.heading("First Name",text="First Name")
        self.libraryTable.heading("Last Name",text="Last Name")
        self.libraryTable.heading("Address1",text="Address1")
        self.libraryTable.heading("Address2",text="Address2")
        self.libraryTable.heading("Post Code",text="Post Code")
        self.libraryTable.heading("Mobile",text="Mobile")
        self.libraryTable.heading("Book ID:",text="Book ID:")
        self.libraryTable.heading("Book Title",text="Book Title")
        self.libraryTable.heading("Author Name",text="Author Name")
        self.libraryTable.heading("Date Borrowed:",text="Date Borrowed:")
        self.libraryTable.heading("Date Due:",text="Date Due:")
        self.libraryTable.heading("Days On Book:",text="Days On Book:")
        self.libraryTable.heading("Late Return Fine:",text="Late Return Fine:")
        self.libraryTable.heading("Date Over Due:",text="Date Over Due:")
        self.libraryTable.heading("Actual Price:",text="Actual Price:")

        self.libraryTable["show"]="headings"
        self.libraryTable.pack(fill=BOTH,expand=1)


        self.libraryTable.column("Member Type",width=100)
        self.libraryTable.column("PRN NO:",width=100)
        self.libraryTable.column("First Name",width=100)
        self.libraryTable.column("Last Name",width=100)
        self.libraryTable.column("Address1",width=100)
        self.libraryTable.column("Address2",width=100)
        self.libraryTable.column("Post Code",width=100)
        self.libraryTable.column("Mobile",width=100)
        self.libraryTable.column("Book ID:",width=100)
        self.libraryTable.column("Book Title",width=100)
        self.libraryTable.column("Author Name",width=100)
        self.libraryTable.column("Date Borrowed:",width=100)
        self.libraryTable.column("Date Due:",width=100)
        self.libraryTable.column("Days On Book:",width=100)
        self.libraryTable.column("Late Return Fine:",width=100)
        self.libraryTable.column("Date Over Due:",width=100)
        self.libraryTable.column("Actual Price:",width=100)
   #=========================================Connect to Sql Data============================================
         

if __name__ == "__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()




