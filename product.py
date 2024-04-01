from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk, messagebox
import sqlite3
class ProductClass:
    def __init__(self, root) :
        self.root = root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        
        self.var_pid=IntVar()
        self.var_category = StringVar()
        self.var_supplier = StringVar()
        self.var_product = StringVar()
        self.var_quantity = StringVar()
        self.var_price = StringVar()
        self.var_status = StringVar()
        self.var_searchType=StringVar()
        self.var_searchTxt=StringVar()

        #--------------------------------------
        productFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        productFrame.place(x=10,y=10,width=450,height=460)
        #tittle
        title =Label(productFrame,text="Product Details",font=("times new roman",25),bg="#9d9de1",fg="white").pack(side=TOP,fill=X)

        lb_pid =Label(productFrame,text="Product ID",font=("times new roman",20),bg="white",fg="#9d9de1").place(x=30,y=50)

        lb_category =Label(productFrame,text="Category",font=("times new roman",20),bg="white",fg="#9d9de1").place(x=30,y=90)
        lb_supplier =Label(productFrame,text="Supplier",font=("times new roman",20),bg="white",fg="#9d9de1").place(x=30,y=145)
        lb_product =Label(productFrame,text="Products",font=("times new roman",20),bg="white",fg="#9d9de1").place(x=30,y=195)
        lb_quantity =Label(productFrame,text="Quantity",font=("times new roman",20),bg="white",fg="#9d9de1").place(x=30,y=245)
        lb_price =Label(productFrame,text="Price",font=("times new roman",20),bg="white",fg="#9d9de1").place(x=30,y=295)
        lb_status =Label(productFrame,text="Status",font=("times new roman",20),bg="white",fg="#9d9de1").place(x=30,y=360)

        txt_pid =Entry(productFrame,textvariable=self.var_pid,font=("times new roman",15),bg="#d0d0e1").place(x=180,y=50,width=200)

        cb_category = ttk.Combobox(productFrame, textvariable=self.var_category,values=("Dairy","Fruits","Vegetables","Snacks"),state='readonly',justify=CENTER).place(x=180,y=95)
        cb_supplier = ttk.Combobox(productFrame, textvariable=self.var_supplier,values=("Basant","Jasneet","Vishal","Neha"),state='readonly',justify=CENTER).place(x=180,y=140)
        txt_product =Entry(productFrame,textvariable=self.var_product,font=("times new roman",15),bg="#d0d0e1").place(x=180,y=185,width=200)
        txt_quantity =Entry(productFrame,textvariable=self.var_quantity,font=("times new roman",15),bg="#d0d0e1").place(x=180,y=245,width=200)
        txt_price =Entry(productFrame,textvariable=self.var_price,font=("times new roman",15),bg="#d0d0e1").place(x=180,y=305,width=200)
        txt_status =ttk.Combobox(productFrame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER).place(x=180,y=365)

        #buttons
        btn_add = Button(productFrame,text="Save",command=self.add_506,bg="#9d9de1",fg="black",cursor="hand2").place(x=30,y=410,width=80,height=40)
        btn_update = Button(productFrame,text="Update",command=self.UpdateData_506,bg="#9d9de1",fg="black",cursor="hand2").place(x=130,y=410,width=80,height=40)
        btn_del = Button(productFrame,text="Delete",command=self.delete_506,bg="#9d9de1",fg="black",cursor="hand2").place(x=230,y=410,width=80,height=40)
        btn_clear = Button(productFrame,text="Clear",command=self.clear_506,bg="#9d9de1",fg="black",cursor="hand2").place(x=330,y=410,width=80,height=40)

         #search
        searchFrame = LabelFrame(self.root,text="Search Employee",bg="white",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE)
        searchFrame.place(x=480,y=10,width=600,height=70)

        #options
        cmd_search = ttk.Combobox(searchFrame, textvariable=self.var_searchType,values=("Select","Category","Supplier","name"),state='readonly',justify=CENTER)
        cmd_search.place(x=10,y=10,width=180)
        cmd_search.current(0)

        txt_search = Entry(searchFrame,textvariable=self.var_searchTxt,bg="#d0d0e1").place(x=200,y=10)
        btn_search = Button(searchFrame,text="Search",command=self.searchData,bg="#9d9de1",fg="white",cursor="hand2").place(x=410,y=10,width=150,height=25)


#Tree view emp details
        p_frame = Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=480,y=100,width=600,height=370)
        scroll1=Scrollbar(p_frame,orient=VERTICAL)
        scroll2=Scrollbar(p_frame,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(p_frame,columns=("pid","Category","Supplier","Name","Price","Quantity","Status"),yscrollcommand=scroll1.set,xscrollcommand=scroll2.set)
        scroll1.pack(side=RIGHT,fill=Y)
        scroll2.pack(side=BOTTOM,fill=X)
        scroll2.config(command=self.ProductTable.xview)
        scroll1.config(command=self.ProductTable.yview)

        self.ProductTable.heading("pid",text="P_id")
        self.ProductTable.heading("Category",text="Category")
        self.ProductTable.heading("Supplier",text="Supplier")
        self.ProductTable.heading("Name",text="Name")
        self.ProductTable.heading("Price",text="Price")
        self.ProductTable.heading("Quantity",text="Quantity")
        self.ProductTable.heading("Status",text="Status")
        self.ProductTable["show"]="headings"

        self.ProductTable.column("pid",width=50)
        self.ProductTable.column("Category",width=95)
        self.ProductTable.column("Supplier",width=95)
        self.ProductTable.column("Name",width=95)
        self.ProductTable.column("Price",width=80)
        self.ProductTable.column("Quantity",width=80)
        self.ProductTable.column("Status",width=80)



        self.ProductTable.pack(fill=BOTH,expand=1)
        self.ProductTable.bind("<ButtonRelease-1>",self.getData_506)
        
        self.footer= Label(self.root,text="IMS - Inventory Management System",font=("times new roman",15),bg="#006699",fg="white").pack(side=BOTTOM,fill=X)

        self.visble_data()


####-----ADD---
    def add_506(self):
        con = sqlite3.connect(database=r'Inventory_file.db')
        cr=con.cursor()
        try:
            if self.var_category.get()=="" or self.var_supplier.get()=="" or self.var_product.get()=="" :
                messagebox.showerror("Error","Field is requied",parent=self.root)
            else:
                cr.execute("select * from product_792 where Name=?", (self.var_product.get(),))
                fetch = cr.fetchone()
                if fetch!=None:
                    messagebox.showerror("Error","Product already present, Try again",parent=self.root)
                else:
                    cr.execute("Insert into product_792(pid,Category,Supplier,Name,Price,Quantity,Status) values(?,?,?,?,?,?,?)",(
                        self.var_pid.get(),
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_product.get(),
                        self.var_quantity.get(),
                        self.var_price.get(),
                        self.var_status.get(),
                    ))
                    con.commit();
                    messagebox.showinfo("Success","Product Added successfully",parent=self.root)
                    self.visble_data()
        except Exception as e:
            messagebox.showerror("Error",f"Error because: {str(e)}",parent=self.root)

    def visble_data(self):
        con = sqlite3.connect(database=r'Inventory_file.db')
        cr=con.cursor()
        try:
            cr.execute("select * from product_792")
            rows= cr.fetchall()
            self.ProductTable.delete(*self.ProductTable.get_children())
            for i in rows:
                self.ProductTable.insert('',END,values=i)
        except Exception as e:
            messagebox.showerror("Error",f"Error because: {str(e)}",parent=self.root)

    def getData_506(self,evv):
        gett = self.ProductTable.focus()
        contentt = (self.ProductTable.item(gett))
        row = contentt['values']
        #print(row)
        self.var_pid.set(row[0])
        self.var_category.set(row[1])
        self.var_supplier.set(row[2])
        self.var_product.set(row[3])
        self.var_quantity.set(row[4])
        self.var_price.set(row[5])
        self.var_status.set(row[6])

    def UpdateData_506(self):
        con = sqlite3.connect(database=r'Inventory_file.db')
        cr=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Product id is requied",parent=self.root)
            else:
                cr.execute("select * from product_792 where pid=?", (self.var_pid.get(),))
                fetch = cr.fetchone()
                if fetch==None:
                    messagebox.showerror("Error","Product Id is not Valid!!",parent=self.root)
                else:
                    cr.execute("update product_792 set Category=?,Supplier=?,Name=?,Price=?,Quantity=?,Status=? where pid=?",(
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_product.get(),
                        self.var_price.get(),
                        self.var_quantity.get(),
                        self.var_status.get(),
                        self.var_pid.get(),
                    ))
                    con.commit();
                    messagebox.showinfo("Success","Product Updated successfully",parent=self.root)
                    self.visble_data()
        except Exception as e:
            messagebox.showerror("Error",f"Error because: {str(e)}",parent=self.root)

    def delete_506(self):
        con = sqlite3.connect(database=r'Inventory_file.db')
        cr=con.cursor()
        try:
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Product id is requied",parent=self.root)
            else:
                cr.execute("select * from product_792 where pid=?", (self.var_pid.get(),))
                fetch = cr.fetchone()
                if fetch==None:
                    messagebox.showerror("Error","Product Id is not Valid!!",parent=self.root)
                else:
                    ask = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if ask == True:
                        cr.execute("delete from product_792 where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Product Deleted successfully",parent=self.root)
                        self.clear_506()
        except Exception as e:
            messagebox.showerror("Error",f"Error because: {str(e)}",parent=self.root)
    
    def clear_506(self):
        self.var_category.set("")
        self.var_supplier.set("")
        self.var_product.set("")
        self.var_quantity.set("")
        self.var_price.set("")
        self.var_status.set("")
        self.var_pid.set("")
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
                cr.execute("select * from product_792 where "+self.var_searchType.get()+" like '%"+self.var_searchTxt.get()+"%'")
                rows= cr.fetchall()
                if len(rows)!=0:
                    self.ProductTable.delete(*self.ProductTable.get_children())
                    for i in rows:
                        self.ProductTable.insert('',END,values=i)
                else:
                    messagebox.showerror("Error","Record not found!!!",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Error because: {str(e)}",parent=self.root)

if __name__=="__main__":
    root = Tk()
    obj = ProductClass(root)
    root.mainloop()