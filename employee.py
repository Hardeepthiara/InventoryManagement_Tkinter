from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3
class Employee:
    def __init__(self, root) :
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        #All variables declare here
        self.var_searchType = StringVar()
        self.var_searchTxt = StringVar()

        self.var_empid = StringVar()
        self.var_gender = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_pass = StringVar()
        self.var_utype = StringVar()
        self.var_salary = StringVar()
        #self.var_add = StringVar()


        #search
        searchFrame = LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        searchFrame.place(x=250,y=20,width=600,height=70)

        #options
        cmd_search = ttk.Combobox(searchFrame, textvariable=self.var_searchType,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER)
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)

        txt_search = Entry(searchFrame,textvariable=self.var_searchTxt,bg="#d0d0e1").place(x=200,y=10)
        btn_search = Button(searchFrame,text="Search",command=self.searchData,bg="#9d9de1",fg="black",cursor="hand2").place(x=400,y=10,width=150,height=25)
        #tittle
        title =Label(self.root,text="Employee Details",font=("times new roman",15),bg="#9d9de1",fg="white").place(x=50,y=100,width=1000)
        #content
        #row1
        empid =Label(self.root,text="Emp ID",font=("times new roman",15),bg="white").place(x=50,y=150)
        gender =Label(self.root,text="Gender",font=("times new roman",15),bg="white").place(x=350,y=150)
        contact =Label(self.root,text="Contact",font=("times new roman",15),bg="white").place(x=750,y=150)
        
        txt_empid =Entry(self.root,textvariable=self.var_empid,font=("times new roman",15),bg="#d0d0e1").place(x=150,y=150,width=180)
        txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER)
        txt_gender.place(x=500,y=150,width=180)
        txt_gender.current(0) 
        txt_contact =Entry(self.root,textvariable=self.var_contact,font=("times new roman",15),bg="#d0d0e1").place(x=850,y=150,width=180)
        
        #row 2
        name =Label(self.root,text="Name",font=("times new roman",15),bg="white").place(x=50,y=190)
        dob =Label(self.root,text="DOB",font=("times new roman",15),bg="white").place(x=350,y=190)
        doj =Label(self.root,text="DOJ",font=("times new roman",15),bg="white").place(x=750,y=190)  
        txt_name =Entry(self.root,textvariable=self.var_name,font=("times new roman",15),bg="#d0d0e1").place(x=150,y=190,width=180)
        txt_dob =Entry(self.root,textvariable=self.var_dob,font=("times new roman",15),bg="#d0d0e1").place(x=500,y=190,width=180)
        txt_doj =Entry(self.root,textvariable=self.var_doj,font=("times new roman",15),bg="#d0d0e1").place(x=850,y=190,width=180)
        
        #row 3
        email =Label(self.root,text="Email",font=("times new roman",15),bg="white").place(x=50,y=230)
        UserType =Label(self.root,text="UserType",font=("times new roman",15),bg="white").place(x=350,y=230)
        password =Label(self.root,text="Password",font=("times new roman",15),bg="white").place(x=750,y=230)
        
        txt_email =Entry(self.root,textvariable=self.var_email,font=("times new roman",15),bg="#d0d0e1").place(x=150,y=230,width=180)
        txt_Utype = ttk.Combobox(self.root, textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER)
        txt_Utype.place(x=500,y=230,width=180)
        txt_Utype.current(0) 
        txt_pass =Entry(self.root,textvariable=self.var_pass,font=("times new roman",15),bg="#d0d0e1").place(x=850,y=230,width=180)
        
        #row4
        add =Label(self.root,text="Address",font=("times new roman",15),bg="white").place(x=50,y=270)
        salary =Label(self.root,text="Salary",font=("times new roman",15),bg="white").place(x=500,y=270)
        
        self.txt_add =Text(self.root,font=("times new roman",15),bg="#d0d0e1")
        self.txt_add.place(x=150,y=270,width=300,height=60)
        txt_sal =Entry(self.root,textvariable=self.var_salary,font=("times new roman",15),bg="#d0d0e1").place(x=600,y=270,width=180)
        #buttons
        btn_add = Button(self.root,text="Save",command=self.add_506,bg="#9d9de1",fg="black",cursor="hand2").place(x=500,y=305,width=110,height=28)
        btn_update = Button(self.root,text="Update",command=self.UpdateData_506,bg="#9d9de1",fg="black",cursor="hand2").place(x=620,y=305,width=110,height=28)
        btn_del = Button(self.root,text="Delete",command=self.delete_506,bg="#9d9de1",fg="black",cursor="hand2").place(x=740,y=305,width=110,height=28)
        btn_clear = Button(self.root,text="Clear",command=self.clear_506,bg="#9d9de1",fg="black",cursor="hand2").place(x=860,y=305,width=150,height=25)

        #Tree view emp details
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1)
        scroll1=Scrollbar(emp_frame,orient=VERTICAL)
        scroll2=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmployeeTable=ttk.Treeview(emp_frame,columns=("empid","name","gender","contact","dob","doj","email","password","utype","address","salary"),yscrollcommand=scroll1.set,xscrollcommand=scroll2.set)
        scroll1.pack(side=RIGHT,fill=Y)
        scroll2.pack(side=BOTTOM,fill=X)
        scroll2.config(command=self.EmployeeTable.xview)
        scroll1.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("empid",text="Emp ID")
        self.EmployeeTable.heading("name",text="Name")
        self.EmployeeTable.heading("gender",text="Gender")
        self.EmployeeTable.heading("contact",text="Contact")
        self.EmployeeTable.heading("dob",text="DOB")
        self.EmployeeTable.heading("doj",text="DOJ")
        self.EmployeeTable.heading("email",text="Email")
        self.EmployeeTable.heading("password",text="Password")
        self.EmployeeTable.heading("utype",text="Usertype")
        self.EmployeeTable.heading("address",text="Address")
        self.EmployeeTable.heading("salary",text="Salary")
        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("empid",width=99)
        self.EmployeeTable.column("name",width=100)
        self.EmployeeTable.column("gender",width=100)
        self.EmployeeTable.column("contact",width=100)
        self.EmployeeTable.column("dob",width=100)
        self.EmployeeTable.column("doj",width=100)
        self.EmployeeTable.column("email",width=100)
        self.EmployeeTable.column("password",width=100)
        self.EmployeeTable.column("utype",width=100)
        self.EmployeeTable.column("address",width=100)
        self.EmployeeTable.column("salary",width=100)
        self.EmployeeTable.pack(fill=BOTH,expand=1)
        self.EmployeeTable.bind("<ButtonRelease-1>",self.getData_506)

        self.visble_data()    #calling select function
#### Database-----ADD---
    def add_506(self):
        con = sqlite3.connect(database=r'Inventory_file.db')
        cr=con.cursor()
        try:
            if self.var_empid.get()=="":
                messagebox.showerror("Error","Employee id is requied",parent=self.root)
            else:
                cr.execute("select * from Employee_506 where empid=?", (self.var_empid.get(),))
                fetch = cr.fetchone()
                if fetch!=None:
                    messagebox.showerror("Error","Emp ID already exists, Try again!",parent=self.root)
                else:
                    cr.execute("Insert into Employee_506(empid,name,gender,contact,dob,doj,email,password,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_empid.get(),
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_email.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_add.get('1.0',END),
                        self.var_salary.get(),
                    ))
                    con.commit();
                    messagebox.showinfo("Success","Emp Added successfully",parent=self.root)
                    self.visble_data()
        except Exception as e:
            messagebox.showerror("Error",f"Error because: {str(e)}",parent=self.root)


    def visble_data(self):
        con = sqlite3.connect(database=r'Inventory_file.db')
        cr=con.cursor()
        try:
            cr.execute("select * from Employee_506")
            rows= cr.fetchall()
            self.EmployeeTable.delete(*self.EmployeeTable.get_children())
            for i in rows:
                self.EmployeeTable.insert('',END,values=i)
        except Exception as e:
            messagebox.showerror("Error",f"Error because: {str(e)}",parent=self.root)

    def getData_506(self,evv):
        gett = self.EmployeeTable.focus()
        contentt = (self.EmployeeTable.item(gett))
        row = contentt['values']
        #print(row)
        self.var_empid.set(row[0])
        self.var_name.set(row[1])
        self.var_gender.set(row[2])
        self.var_contact.set(row[3])
        self.var_dob.set(row[4])
        self.var_doj.set(row[5])
        self.var_email.set(row[6])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
        self.txt_add.delete('1.0',END)
        self.txt_add.insert(END,row[9])
        self.var_salary.set(row[10])

    def UpdateData_506(self):
        con = sqlite3.connect(database=r'Inventory_file.db')
        cr=con.cursor()
        try:
            if self.var_empid.get()=="":
                messagebox.showerror("Error","Employee id is requied",parent=self.root)
            else:
                cr.execute("select * from Employee_506 where empid=?", (self.var_empid.get(),))
                fetch = cr.fetchone()
                if fetch==None:
                    messagebox.showerror("Error","Employee Id is not Valid!!",parent=self.root)
                else:
                    cr.execute("update Employee_506 set name=?,gender=?,contact=?,dob=?,doj=?,email=?,password=?,utype=?,address=?,salary=? where empid=?",(
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_email.get(),
                        self.var_pass.get(),
                        self.var_utype.get(),
                        self.txt_add.get('1.0',END),
                        self.var_salary.get(),
                        self.var_empid.get(),

                    ))
                    con.commit();
                    messagebox.showinfo("Success","Employee Updated successfully",parent=self.root)
                    self.visble_data()
        except Exception as e:
            messagebox.showerror("Error",f"Error because: {str(e)}",parent=self.root)

    def delete_506(self):
        con = sqlite3.connect(database=r'Inventory_file.db')
        cr=con.cursor()
        try:
            if self.var_empid.get()=="":
                messagebox.showerror("Error","Employee id is requied",parent=self.root)
            else:
                cr.execute("select * from Employee_506 where empid=?", (self.var_empid.get(),))
                fetch = cr.fetchone()
                if fetch==None:
                    messagebox.showerror("Error","Employee Id is not Valid!!",parent=self.root)
                else:
                    ask = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if ask == True:
                        cr.execute("delete from Employee_506 where empid=?",(self.var_empid.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Employee Deleted successfully",parent=self.root)
                        self.clear_506()
        except Exception as e:
            messagebox.showerror("Error",f"Error because: {str(e)}",parent=self.root)
    
    def clear_506(self):
        self.var_empid.set("")
        self.var_name.set("")
        self.var_gender.set("Select")
        self.var_contact.set("")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_email.set("")
        self.var_pass.set("")
        self.var_utype.set("Admin")
        self.txt_add.delete('1.0',END)
        self.var_salary.set("")
        self.var_searchTxt.set("")
        self.var_searchType.set("Select")
        self.visble_data()

    def searchData(self):
        con = sqlite3.connect(database=r'Inventory_file.db')
        cr=con.cursor()
        try:
            if self.var_searchType.get()=="Select":
                messagebox.showerror("Error","Search by option",parent=self.root)
            elif self.var_searchTxt.get()=="":
                messagebox.showerror("Error","Input should be Required",parent=self.root)
            else:
                cr.execute("select * from Employee_506 where "+self.var_searchType.get()+" like '%"+self.var_searchTxt.get()+"%'")
                rows= cr.fetchall()
                if len(rows)!=0:
                    self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                    for i in rows:
                        self.EmployeeTable.insert('',END,values=i)
                else:
                    messagebox.showerror("Error","Record not found!!!",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Error because: {str(e)}",parent=self.root)

if __name__=="__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()