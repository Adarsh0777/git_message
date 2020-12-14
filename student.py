from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student management syatem")
        self.root.geometry("1915x1080")

        title=Label(self.root,text="Student management system",bd=8, relief=GROOVE, font=("times new roman",40,"bold"),bg="dodgerblue1",fg="black")
        title.pack(side=TOP,fill=X)


        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
       
        

        manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="pink1")
    
        manage_Frame.place(x=15,y=80,width=450,height=780)

        m_title=Label(manage_Frame,text="Manage student",font=("times new roman",15,"bold"),bg="dodgerblue1",fg="black")
        m_title.grid(row=0,columnspan=2,pady=30)

        lbl_roll=Label(manage_Frame,text="Roll No:",font=("times new roman",18,"bold"))
        lbl_roll.grid(row=1,column=0,pady=15,padx=15,sticky="w")

        txt_roll=Entry(manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=15,padx=15,sticky="w")

        lbl_name=Label(manage_Frame,text="Name:",font=("times new roman",18,"bold"))
        lbl_name.grid(row=2,column=0,pady=15,padx=15,sticky="w")

        txt_name=Entry(manage_Frame,textvariable=self.name_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=15,padx=15,sticky="w")

        lbl_email=Label(manage_Frame,text="E-Mail:",font=("times new roman",18,"bold"))
        lbl_email.grid(row=3,column=0,pady=15,padx=15,sticky="w")

        txt_email=Entry(manage_Frame,textvariable=self.email_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=15,padx=15,sticky="w")

        lbl_gender=Label(manage_Frame,text="Gender:",font=("times new roman",18,"bold"))
        lbl_gender.grid(row=4,column=0,pady=15,padx=15,sticky="w")

        combo_gender=ttk.Combobox(manage_Frame,textvariable=self.gender_var ,font=("times new roman",16,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,pady=15,padx=15,sticky="w")

        

        lbl_contact=Label(manage_Frame,text="Contact:",font=("times new roman",18,"bold"))
        lbl_contact.grid(row=5,column=0,pady=15,padx=15,sticky="w")

        txt_contact=Entry(manage_Frame,textvariable=self.contact_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=15,padx=15,sticky="w")

        lbl_D0B=Label(manage_Frame,text="D.O.B:",font=("times new roman",18,"bold"))
        lbl_D0B.grid(row=6,column=0,pady=15,padx=15,sticky="w")

        txt_DOB=Entry(manage_Frame,textvariable=self.dob_var,font=("times new roman",18,"bold"),bd=5,relief=GROOVE)
        txt_DOB.grid(row=6,column=1,pady=15,padx=15,sticky="w")

        lbl_Address=Label(manage_Frame,text="Address:",font=("times new roman",18,"bold"))
        lbl_Address.grid(row=7,column=0,pady=15,padx=15,sticky="w")

        self.txt_Address=Text(manage_Frame,width=27,height=4,font=("times new roman",13,"bold"))
        self.txt_Address.grid(row=7,column=1,sticky="w",padx=15,pady=15)

        btn_Frame=Frame(manage_Frame,bd=4,relief=RIDGE,bg="pink1")
        btn_Frame.place(x=8,y=615,width=425)

        addbtn=Button(btn_Frame,text='Add',width=10,height=2,bg="green2",command=self.add_student,cursor="hand2").grid(row=0,column=0,padx=13,pady=13)

        updatebtn=Button(btn_Frame,text='Update',width=10,height=2,bg="yellow",command=self.update_data,cursor="hand2").grid(row=0,column=1,padx=13,pady=13)
        
        deletebtn=Button(btn_Frame,text='Delete',width=10,height=2,bg="red",command=self.delete_data,cursor="hand2").grid(row=0,column=2,padx=13,pady=13)
        
        clearbtn=Button(btn_Frame,text='Clear',width=10,height=2,bg="dodgerblue1",command=self.clear,cursor="hand2").grid(row=0,column=3,padx=13,pady=13)

        



        detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="pink1")
        detail_Frame.place(x=500,y=80,width=1015,height=780)

        lbl_search=Label(detail_Frame,text="Search By:",font=("times new roman",18,"bold"))
        lbl_search.grid(row=0,column=0,pady=25,padx=25,sticky="w")

        combo_search=ttk.Combobox(detail_Frame,textvariable=self.search_by,width=15,font=("times new roman",16,"bold"),state='readonly')
        combo_search['values']=("roll_no","name","contact","dob")
        combo_search.grid(row=0,column=1,pady=25,padx=25,sticky="w")

        txt_search=Entry(detail_Frame,textvariable=self.search_txt,font=("times new roman", 17, "bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=23,padx=23,sticky="w")

        searchbtn=Button(detail_Frame,text='Search',width=15,height=2,bg="yellow",command=self.search_data,cursor="hand2").grid(row=0,column=3,padx=15,pady=15)
        showallbtn=Button(detail_Frame,text='Show All',width=15,height=2,bg="green2",command=self.fetch_data,cursor="hand2").grid(row=0,column=4,padx=15,pady=15)

        
        table_frame=Frame(detail_Frame,bd=4,relief=RIDGE)
        table_frame.place(x=20,y=95,width=960,height=600)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)
    
        self.Student_table=ttk.Treeview(table_frame,columns=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("roll",text="Roll No")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="E-Mail")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B")
        self.Student_table.heading("address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=130)
        self.Student_table.column("name",width=130)
        self.Student_table.column("email",width=130)
        self.Student_table.column("gender",width=130)
        self.Student_table.column("contact",width=130)
        self.Student_table.column("dob",width=130)
        self.Student_table.column("address",width=130)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
    def add_student(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","All Fields are required!!")
        else:
            try:

                con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
                cur=con.cursor()
                cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                                self.name_var.get(),
                                                                                self.email_var.get(),
                                                                                self.gender_var.get(),
                                                                                self.contact_var.get(),
                                                                                self.dob_var.get(),
                                                                                self.txt_Address.get('1.0',END)
                                                                                ))
                con.commit()
                self.fetch_data()
                messagebox.showinfo("Successs","record has been Inserted Successfully!!")
                self.clear()
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"error due to: {str(es)}",parent=self.root)

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
        cur=con.cursor()
        cur.execute("select * from student")
        rows=cur.fetchall()
        if len(rows)!=0:
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                        self.Student_table.insert('',END,values=row)
                con.commit()
        con.close()
        

    def clear(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","Choose record to be cleared!!")
        else:
            self.Roll_No_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.txt_Address.delete("1.0",END)
            messagebox.showinfo("Successs","record has been cleared Successfully!!")
    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])


    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
        cur=con.cursor()
        cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",(
                                                                                                self.name_var.get(),                                                                                       
                                                                                                self.email_var.get(),
                                                                                                self.gender_var.get(),
                                                                                                self.contact_var.get(),
                                                                                                self.dob_var.get(),
                                                                                                self.txt_Address.get('1.0',END),
                                                                                                self.Roll_No_var.get()
                                                                                                ))

        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("Successs","record has been Updated Successfully!!")

    def delete_data(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.dob_var.get()=="":
            messagebox.showerror("Error","Choose record to be deleted!!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
            cur=con.cursor()
            cur.execute("delete from student where roll_no=%s",self.Roll_No_var.get())
            con.commit()
            con.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Successs","record has been deleted Successfully!!")
    def search_data(self):
        if self.search_by.get()=="":
            messagebox.showerror("Error","select any field to be Searched !!")
        else:
            con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
            cur=con.cursor()

            cur.execute("select * from student where "+str(self.search_by.get())+" Like '%"+str(self.search_txt.get())+"%'")
            rows=cur.fetchall()
            if len(rows)==0:

                messagebox.showerror("Error","There is no record that you have searched!")
            elif len(rows)!=0:
                
                self.Student_table.delete(*self.Student_table.get_children())
                for row in rows:
                    self.Student_table.insert('',END,values=row)                
                con.commit()
                con.close()
                messagebox.showinfo("Successs","record has been searched Successfully!!")     
        

root=Tk()
ob=Student(root)
root.mainloop()

