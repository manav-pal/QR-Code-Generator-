from tkinter import*
import qrcode
from PIL import Image, ImageTk
from resizeimage import resizeimage




class Qr_Code:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1000x600+200+50")
        self.root.title("  QR Code of Employee | Developed by shashank")
        self.root.resizable(False, False)
        title = Label(self.root, text="QR Code Generator", font=("times new roman",40), bg="#053246", fg="white", anchor="w").place(x=0, y=0,relwidth=1)
        self.root.iconbitmap('D:\GUI tkinter projects\QR_Generator\Employee_QR/icon.ico.ico')
        #======Employees details are here========
        #======Variables=====
        self.var_emp_code = StringVar()
        self.var_emp_name = StringVar()
        self.var_emp_Department = StringVar()
        self.var_emp_Designation = StringVar()

        emp_Frame = Frame(self.root, bd=2, relief=RIDGE, background="white")
        emp_Frame.place(x=50, y=100, width=500,height=400)
        emp_title = Label(emp_Frame, text="Employee details", font=("goudy old style",20), bg="#043256", fg="white").place(x=0, y=0, relwidth=1)
        lab1_emp_code = Label(emp_Frame, text="Employee id", font=("times new roman",15, 'bold'), bg="white").place(x=50, y=60)
        lab2_emp_code = Label(emp_Frame, text="Name", font=("times new roman",15,'bold'), bg="white").place(x=50, y=120)
        lab3_emp_code = Label(emp_Frame, text="Department", font=("times new roman", 15,'bold'), bg="white").place(x=50, y=180)
        lab4_emp_codde = Label(emp_Frame, text="Designation", font=("times new roman", 15, 'bold'), bg="white").place(x=50, y=260)



        txt1_emp_code = Entry(emp_Frame, font=("times new roman", 15, 'bold'), textvariable=self.var_emp_code, bg="white").place(x=200, y=60)
        txt2_emp_code = Entry(emp_Frame, font=("times new roman", 15, 'bold'), textvariable=self.var_emp_name, bg="white").place(x=200, y=120)
        txt3_emp_code = Entry(emp_Frame, font=("times new roman",  15,  'bold'), textvariable=self.var_emp_Department, bg="white").place(x=200, y=180)
        txt4_emp_code = Entry(emp_Frame, font=("times new roman", 15, 'bold'), textvariable=self.var_emp_Designation, bg="white").place(x=200, y=260)

       #====buttons====

        btn_generate= Button(emp_Frame, text="Generate QR",command=self.generate, font=("times new roman", 15,'bold'), bg="#2196f3", fg="white").place(x=50, y=310, width=200, height=30)   
        btn_clear= Button(emp_Frame, text="Clear", command=self.clear, font=("times new roman", 15,'bold'), bg="#2196f3", fg="white").place(x=270, y=310, width=200, height=30)

        self.mssg=""
        self.lbl_mssg = Label(emp_Frame, text=self.mssg, font=("times new roman", 20), bg="white", fg="green")
        self.lbl_mssg.place(x=0, y=350, relwidth=1)

        #====Employee QR code window=====
        QR_frame = Frame(self.root, bd=2, relief=RIDGE, background="white")
        QR_frame.place(x=650, y=100, width=300, height=300)
        QR_title = Label(QR_frame, text= " Employee QR Code", font=("goudy old style",15,'bold'), bg="#043256", fg="white").place(x=0, y=0, relwidth=1)

        self.qr_code = Label(QR_frame, text="No QR\n Available", font=("times new roman", 20), bg="blue", fg="white")
        self.qr_code.place(x=60, y=80)


    def clear(self):
        self.var_emp_code.set('')
        self.var_emp_name.set('')
        self.var_emp_Department.set('')
        self.var_emp_Designation.set('')
        self.mssg=''
        self.lbl_mssg.config(text=self.mssg, fg="red")

    def generate(self):
        if self.var_emp_code.get()=="" or  self.var_emp_name.get()=="" or  self.var_emp_Department.get()=="" or  self.var_emp_Designation.get()=="":
            self.mssg = "All Fields are required!!!"
            self.lbl_mssg.config(text=self.mssg, fg="red")
        else:
            qr_data = (f"Employee ID:{self.var_emp_code.get()}\n Employee name:{self.var_emp_name.get()}\n Employee Department:{self.var_emp_Department.get()}\n Employee Designation:{self.var_emp_Designation.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)
            qr_code = resizeimage.resize_cover(qr_code, [180,180])
            qr_code.save("Employee_QR/Emp_"+str(self.var_emp_code.get())+'.png')

            #=====QR image update=====
            self.im=ImageTk.PhotoImage(file="Employee_QR/Emp_"+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)

            #====updating notifications=====
            self.mssg = "QR Generates Succesfully!!!"
            self.lbl_mssg.config(text=self.mssg, fg="green")


root = Tk()
obj = Qr_Code(root)
root.mainloop()