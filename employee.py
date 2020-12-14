from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee management system")
        self.root.geometry("1915x1080")
        


        title=Label(self.root,text="Employee management system",font=("times new roman",40,"bold"),bd=4,bg="dodgerblue1",fg="black",relief=GROOVE)
        title.pack(fill=X,side=TOP)

        self.emp_id_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.designation_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.address_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()

        manage_frame=Frame(self.root,bd=4,relief=RIDGE,bg="burlywood")
        manage_frame.place(x=15,y=80,width=450,height=780)

        m_title=Label(manage_frame,text="Manage Employee",font=("times new roman",15,"bold"),bg="dodgerblue1")
        m_title.grid(row=0,columnspan=2,pady=30)
        
        lbl_id=Label(manage_frame,text="Employee Id:",font=("times new roman",16,"bold"))
        lbl_id.grid(row=1,column=0,padx=15,pady=15,sticky="w")

        txt_id=Entry(manage_frame,textvariable=self.emp_id_var,font=("times new roman",16,"bold"),bd=5,relief=RIDGE,)
        txt_id.grid(row=1,column=1,padx=15,pady=15,sticky="w")

        lbl_name=Label(manage_frame,text="Name:",font=("times new roman",16,"bold"))
        lbl_name.grid(row=2,column=0,padx=15,pady=15,sticky="w")

        txt_name=Entry(manage_frame,textvariable=self.name_var,font=("times new roman",16,"bold"),bd=5,relief=RIDGE,)
        txt_name.grid(row=2,column=1,padx=15,pady=15,sticky="w")

        lbl_email=Label(manage_frame,text="E-Mail:",font=("times new roman",16,"bold"))
        lbl_email.grid(row=3,column=0,padx=15,pady=15,sticky="w")

        txt_email=Entry(manage_frame,textvariable=self.email_var,font=("times new roman",16,"bold"),bd=5,relief=RIDGE,)
        txt_email.grid(row=3,column=1,padx=15,pady=15,sticky="w")

        lbl_designation=Label(manage_frame,text="Designation:",font=("times new roman",16,"bold"))
        lbl_designation.grid(row=4,column=0,padx=15,pady=15,sticky="w")

        txt_designation=Entry(manage_frame,textvariable=self.designation_var,font=("times new roman",16,"bold"),bd=5,relief=RIDGE)
        txt_designation.grid(row=4,column=1,padx=15,pady=15,sticky="w")


        lbl_contact=Label(manage_frame,text="Contact:",font=("times new roman",16,"bold"))
        lbl_contact.grid(row=5,column=0,padx=15,pady=15,sticky="w")

        txt_contact=Entry(manage_frame,textvariable=self.contact_var,font=("times new roman",16,"bold"),bd=5,relief=RIDGE,)
        txt_contact.grid(row=5,column=1,padx=15,pady=15,sticky="w")

        lbl_dob=Label(manage_frame,text="D.O.B:",font=("times new roman",16,"bold"))
        lbl_dob.grid(row=6,column=0,padx=15,pady=15,sticky="w")

        txt_dob=Entry(manage_frame,textvariable=self.dob_var,font=("times new roman",16,"bold"),bd=5,relief=RIDGE,)
        txt_dob.grid(row=6,column=1,padx=15,pady=15,sticky="w")

        lbl_Address=Label(manage_frame,text="Address:",font=("times new roman",16,"bold"))
        lbl_Address.grid(row=7,column=0,padx=15,pady=15,sticky="w")

        self.txt_Address=Text(manage_frame,width=27,height=4,font=("times new roman",12,"bold"))
        self.txt_Address.grid(row=7,column=1,sticky="w",padx=15,pady=15)

        btn_Frame=Frame(manage_frame,bd=4,relief=RIDGE,bg="burlywood")
        btn_Frame.place(x=8,y=615,width=425)

        addbtn=Button(btn_Frame,text='Add',width=10,height=2,bg="green2",command=self.add_employee).grid(row=0,column=0,padx=13,pady=13)

        updatebtn=Button(btn_Frame,text='Update',width=10,height=2,bg="yellow",command=self.update_data).grid(row=0,column=1,padx=13,pady=13)
        
        deletebtn=Button(btn_Frame,text='Delete',width=10,height=2,bg="red",command=self.delete_data).grid(row=0,column=2,padx=13,pady=13)
        
        clearbtn=Button(btn_Frame,text='Clear',width=10,height=2,bg="dodgerblue1",command=self.clear).grid(row=0,column=3,padx=13,pady=13)


        

        detail_frame=Frame(self.root,bd=4,relief=RIDGE,bg="burlywood")
        detail_frame.place(x=500,y=80,width=1015,height=780)

        lbl_search=Label(detail_frame,text="Search By:",font=("times new roman",16,"bold"))
        lbl_search.grid(row=0,column=0,pady=25,padx=25,sticky="w")

        combo_search=ttk.Combobox(detail_frame,textvariable=self.search_by,width=15,font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("Id","name","contact","Designation")
        combo_search.grid(row=0,column=1,pady=25,padx=25,sticky="w")

        txt_search=Entry(detail_frame,textvariable=self.search_txt,font=("times new roman", 17, "bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=23,padx=23,sticky="w")

        searchbtn=Button(detail_frame,text='Search',width=15,height=2,bg="yellow",command=self.search_data).grid(row=0,column=3,padx=15,pady=15)
        showallbtn=Button(detail_frame,text='Show All',width=15,height=2,bg="green2",command=self.fetch_data).grid(row=0,column=4,padx=15,pady=15)

        
        table_frame=Frame(detail_frame,bd=4,relief=RIDGE)
        table_frame.place(x=20,y=95,width=960,height=600)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
    
        self.Employee_table=ttk.Treeview(table_frame,columns=("Id","name","email","designation","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.Employee_table.xview)
        scroll_y.config(command=self.Employee_table.yview)

        self.Employee_table.heading("Id",text="Employee-Id")
        self.Employee_table.heading("name",text="Name")
        self.Employee_table.heading("email",text="E-Mail")
        self.Employee_table.heading("designation",text="Designation")
        self.Employee_table.heading("contact",text="Contact")
        self.Employee_table.heading("dob",text="D.O.B")
        self.Employee_table.heading("address",text="Address")
        self.Employee_table['show']='headings'
        self.Employee_table.column("Id",width=130)
        self.Employee_table.column("name",width=130)
        self.Employee_table.column("email",width=130)
        self.Employee_table.column("designation",width=130)
        self.Employee_table.column("contact",width=130)
        self.Employee_table.column("dob",width=130)
        self.Employee_table.column("address",width=130)
        self.Employee_table.pack(fill=BOTH,expand=1)
        self.Employee_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_employee(self):
        if self.emp_id_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.designation_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","All Fields are required!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
            cur=con.cursor()
            cur.execute("insert into employees values(%s,%s,%s,%s,%s,%s,%s)",(self.emp_id_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.designation_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_Address.get('1.0',END)
                                                                            ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Successs","record has been inserted Successfully!!")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
        cur=con.cursor()
        cur.execute("select * from employees")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Employee_table.delete(*self.Employee_table.get_children())
                for row in rows:
                        self.Employee_table.insert('',END,values=row)
                con.commit()
        con.close()
        

    def clear(self):
        if self.emp_id_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.designation_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","Choose record to be cleared!!")
        else:
            self.emp_id_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.designation_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.txt_Address.delete("1.0",END)
            messagebox.showinfo("Successs","record has been cleared Successfully!!")
    def get_cursor(self,mv):
        cursor_row=self.Employee_table.focus()
        contents=self.Employee_table.item(cursor_row)
        row=contents['values']
        self.emp_id_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.designation_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])


    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
        cur=con.cursor()
        cur.execute("update employees set name=%s,email=%s,designation=%s,contact=%s,dob=%s,address=%s where emp_id=%s",(
                                                                                                self.name_var.get(),                                                                                       
                                                                                                self.email_var.get(),
                                                                                                self.designation_var.get(),
                                                                                                self.contact_var.get(),
                                                                                                self.dob_var.get(),
                                                                                                self.txt_Address.get('1.0',END),
                                                                                                self.emp_id_var.get()
                                                                                                ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Successs","record has been Updated Successfully!!")

    def delete_data(self):
        if self.emp_id_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.designation_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","Choose record to be deleted!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
            cur=con.cursor()
            cur.execute("delete from employees where emp_id=%s",self.emp_id_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Successs","record has been deleted Successfully!!")
    def search_data(self):
        if self.search_by.get()=="":
            messagebox.showerror("Error","Select any field to be Searched !!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
            cur=con.cursor()

            cur.execute("select * from employees where "+str(self.search_by.get())+" Like '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)==0:

                messagebox.showerror("Error","There is no record that you have searched!")
            elif len(rows)!=0:
                
                self.Employee_table.delete(*self.Employee_table.get_children())
                for row in rows:
                    self.Employee_table.insert('',END,values=row)                
                con.commit()
                con.close()
                messagebox.showinfo("Successs","Record has been searched Successfully!!")     
        


root=Tk()
ob=employee(root)
root.mainloop()