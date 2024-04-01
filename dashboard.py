from tkinter import*
from PIL import Image,ImageTk
from employee import Employee
from product import ProductClass
class IMS:
    def __init__(self, root) :
        self.root = root
        self.root.geometry("1100x700+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        #title
        self.icon_title = Image.open("images/logo2.png")
        self.icon_title=self.icon_title.resize((200,200),Image.ANTIALIAS)
        self.icon_title=ImageTk.PhotoImage(self.icon_title)
        title= Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#004d4d",fg="white",anchor="w",padx=25).place(x=0,y=0,relwidth=1,height=150)

        #clock
        self.lbl_clock= Label(self.root,text="Welcome to Inventory Management System\t\t Date: 17-04-2023\t\t Phone:467-232-4545",font=("times new roman",15),bg="#006699",fg="white")
        self.lbl_clock.place(x=0,y=150,relwidth=1,height=50)

        #image content
        self.EmpLogo=Image.open("images/emp2.png")
        self.EmpLogo=self.EmpLogo.resize((300,200),Image.ANTIALIAS)
        self.EmpLogo=ImageTk.PhotoImage(self.EmpLogo)
        lbl_emplogo = Label(self.root,image=self.EmpLogo)
        lbl_emplogo.place(x=200,y=300,height=120,width=300)
        
        #self.lbl_emp=Label(self.root,text="Employees\n[0]",bd=5,relief=RIDGE,bg="#66194d",fg="white",font=("times new roman",20))
        #self.lbl_emp.place(x=200,y=300,height=120,width=300)
        self.btn_emp =Button(self.root,text="Employee",command=self.employee,font=("times new roman",15,"bold"),bg="#9494b8",fg="black",bd=3,cursor="hand2")
        self.btn_emp.place(x=200,y=470,height=40,width=300)

        self.Prdlogo=Image.open("images/pro.jpg")
        self.Prdlogo=self.Prdlogo.resize((400,400),Image.ANTIALIAS)
        self.Prdlogo=ImageTk.PhotoImage(self.Prdlogo)
        lbl_prologo = Label(self.root,image=self.Prdlogo)
        lbl_prologo.place(x=600,y=300,height=120,width=300)
        #self.lbl_product=Label(self.root,text="Products\n[0]",bd=5,relief=RIDGE,bg="#66194d",fg="white",font=("times new roman",20))
        #self.lbl_product.place(x=600,y=300,height=120,width=300)
        self.btn_emp =Button(self.root,text="Products",command=self.product,font=("times new roman",15,"bold"),bg="#9494b8",fg="black",bd=3,cursor="hand2")
        self.btn_emp.place(x=600,y=470,height=40,width=300)
        
        #footer
        self.footer= Label(self.root,text="IMS - Inventory Management System",font=("times new roman",15),bg="#006699",fg="white").pack(side=BOTTOM,fill=X)

#function
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Employee(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=ProductClass(self.new_win)
        


if __name__=="__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()