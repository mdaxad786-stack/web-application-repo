from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        lbltitle=Label(self.root,bd=20,relief=RIDGE,text=" ⛨Hospital Management System",fg="red",bg="white",font=("Time New Roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

#================================Data frame================================
        Dataframe =Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)

#=====================Patient Informatiom Frame============================
        DataframeLeft=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("Time New Roman",12,"bold"),text="Patient Information",fg="red")
        DataframeLeft.place(x=0,y=5,width=960,height=350)

#======================Prescription========================================
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("Time New Roman",12,"bold"),text="Prescription",fg="red")
        DataframeRight.place(x=990,y=5,width=460,height=350)

#=============================Buttons Frame================================
        Buttonframe =Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)

#=============================Details Frame================================
        Detailsframe =Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)

#===========================DataframeLeft==================================
        lblNameTablet =Label(DataframeLeft,text="Name Of Tablets",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        comNametablet =ttk.Combobox(DataframeLeft,font=("arial",12,"bold"), width=33,state="readonly")
        comNametablet["value"]=("Paracetamol (Painkiller Tablet)","Levofloxacin (Antibiotic Tablets)","Benadryl Cough Tablets (Cough Tablets)","Glycomet (Diabetes Tablets)","Amlodipine (Blood Pressure Tablets)","Omeprazole (Gastric Tablet)","Neurobion (Vitamin Tablets)")
        comNametablet.grid(row=0,column=1)

#============================Label Ref=====================================
        lblref =Label(DataframeLeft,font=("arial",12,"bold"),text="Reference No:",padx=2,pady=6)
        lblref.grid(row=1,column=0)
        txtref=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtref.grid(row=1,column=1)

#==========================Label Dose======================================
        lblDose =Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=6)
        lblDose.grid(row=2,column=0)
        txtDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDose.grid(row=2,column=1)

#=======================Label No: Of Tablet===============================
        lblNoOftablet =Label(DataframeLeft,font=("arial",12,"bold"),text="No Of Tablet:",padx=2,pady=6)
        lblNoOftablet.grid(row=3,column=0)
        txtNoOftablet=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtNoOftablet.grid(row=3,column=1)

#=========================Label Lot=======================================
        lblLot =Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0)
        txtLot=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtLot.grid(row=4,column=1)

#=======================Label Issue Date=================================
        lblissueDate =Label(DataframeLeft,font=("arial",12,"bold"),text="Issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0)
        txtissueDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtissueDate.grid(row=5,column=1)

#=========================Label Expiry Date===============================
        lblExpDate =Label(DataframeLeft,font=("arial",12,"bold"),text="Expiry Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0)
        txtExpDate=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtExpDate.grid(row=6,column=1)

#=========================Label Daily Dose================================
        lblDailyDose =Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0)
        txtDailyDose=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtDailyDose.grid(row=7,column=1)
        
#=========================Label Side Effect================================
        lblSideEffect =Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0)
        txtSideEffect=Entry(DataframeLeft,font=("arial",13,"bold"),width=35)
        txtSideEffect.grid(row=8,column=1)

#=========================Label Further Info===============================
        lblFurtherinfo =Label(DataframeLeft,font=("arial",12,"bold"),text="Further Info:",padx=5,pady=6)
        lblFurtherinfo.grid(row=0,column=2)
        txtFurtherinfo=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtFurtherinfo.grid(row=0,column=3)        

#=========================Label BloodPressure==============================
        lblBloodPressure =Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=5,pady=6)
        lblBloodPressure.grid(row=1,column=2)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtBloodPressure.grid(row=1,column=3)        
                
#=========================Label Storage===================================
        lblStorage =Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=5,pady=6)
        lblStorage.grid(row=2,column=2)
        txtStorage=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtStorage.grid(row=2,column=3)        
                        
#=========================Label Medicine==================================
        lblMedicine =Label(DataframeLeft,font=("arial",12,"bold"),text="Medicine:",padx=5,pady=6)
        lblMedicine.grid(row=3,column=2)
        txtMedicine=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtMedicine.grid(row=3,column=3)        
                                
#=========================Label PatientID===================================
        lblPatientID =Label(DataframeLeft,font=("arial",12,"bold"),text="Patient  ID:",padx=5,pady=6)
        lblPatientID.grid(row=4,column=2)
        txtPatientID=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtPatientID.grid(row=4,column=3)

#=========================Label NHS Number===================================
        lblNhsNumber =Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number:",padx=5,pady=6)
        lblNhsNumber.grid(row=5,column=2)
        txtNhsNumber=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtNhsNumber.grid(row=5,column=3)    
               
#=========================Label Patient Name==================================
        lblPatientName =Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=5,pady=6)
        lblPatientName.grid(row=6,column=2)
        txtPatientName=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtPatientName.grid(row=6,column=3)    

#=========================Label Date Of Birth==================================
        lblDateOfBirth =Label(DataframeLeft,font=("arial",12,"bold"),text="Date Of Birth:",padx=5,pady=6)
        lblDateOfBirth.grid(row=7,column=2)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtDateOfBirth.grid(row=7,column=3)

#=========================Label Patient Address================================
        lblPatientAddress =Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=5,pady=6)
        lblPatientAddress.grid(row=8,column=2)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",12,"bold"),width=35)
        txtPatientAddress.grid(row=8,column=3)

#=======================DataFrameRight=========================================
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=46,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)

#===========================Buttons============================================
        btnPrescription=Button(Buttonframe,text="Prescription",fg="white",bg="green",font=("arial",12,"bold"),width=24,height=1,padx=2,pady=2)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData=Button(Buttonframe,text="Data",fg="white",bg="green",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=2)
        btnPrescriptionData.grid(row=0,column=1)

        btnUpdate=Button(Buttonframe,text="Update",fg="white",bg="green",font=("arial",12,"bold"),width=24,height=1,padx=2,pady=2)
        btnUpdate.grid(row=0,column=2)

        btnDelete=Button(Buttonframe,text="Delete",fg="white",bg="green",font=("arial",12,"bold"),width=24,height=1,padx=2,pady=2)
        btnDelete.grid(row=0,column=3)

        btnClear=Button(Buttonframe,text="Clear",fg="white",bg="green",font=("arial",12,"bold"),width=23,height=1,padx=2,pady=2)
        btnClear.grid(row=0,column=4)

        btnExit=Button(Buttonframe,text="Exit",fg="white",bg="green",font=("arial",12,"bold"),width=24,height=1,padx=2,pady=2)
        btnExit.grid(row=0,column=5)

#==============================Table==========================================
#==============================Scroll Bar=====================================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,columns=("nameoftablet","ref","dose","nooftablets","lot","issuedate","expdate","dailydose","storage advice","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)
        self.hospital_table.pack(fill=BOTH,expand=1)
        
       
        self.hospital_table.heading("nameoftablet",text="Name Of Tablet")
        self.hospital_table.heading("ref",text="Reference no:")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No: of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Dose")
        self.hospital_table.heading("storage advice",text="Storage Advice")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="Date Of Birth")
        self.hospital_table.heading("address",text="Address")

        self.hospital_table["show"]="headings"
        self.hospital_table.pack(fill=BOTH,expand=1)

        self.hospital_table.column("nameoftablet",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage advice",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        self.hospital_table.pack(fill=BOTH,expand=1)

        
root=Tk()
ob=Hospital(root)
root.mainloop()



        
