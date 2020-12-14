from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql


class login:
    def __init__(self, root):
        self.root = root
        self.root.title( "Login Form" )
        self.root.geometry( "1915x1080" )

        self.bg = ImageTk.PhotoImage( file="img/Wallpapers-HD-Nature.jpg" )
        bg = Label( self.root, image=self.bg ).place(relwidth=1,relheight=1)

        self.left = ImageTk.PhotoImage( file="img/login-.jpg" )
        left = Label( self.root, image=self.left ).place( x=80, y=144, width=450, height=550 )

        frame1 = Frame( self.root, bg="white" )
        frame1.place( x=530, y=144, width=750, height=550 )

        title = Label( frame1, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white",
                       fg="#08A3D2" ).place( x=150, y=50 )

        email = Label( frame1, text="EMAIL-ADDRESS", font=("times new roman", 20, "bold"), bg="white",
                       fg="gray" ).place( x=150, y=150 )
        self.txt_email = Entry( frame1, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_email.place( x=150, y=190,width=350,height=35 )

        password = Label( frame1, text="ENTER PASSWORD", font=("times new roman", 20, "bold"), bg="white",
                       fg="gray" ).place( x=150, y=250 )
        self.txt_password = Entry( frame1, font=("times new roman", 15, "bold"), bg="lightgray")
        self.txt_password.place( x=150, y=290,width=350,height=35 )

        btn_reg=Button(frame1,text="Register new Account ",command=self.register_window,font=("times new roman",15),bd=0,bg="white",fg="#B00857",cursor="hand2").place(x=150,y=340)
        btn_forget=Button(frame1,text="Forget Password ? ",command=self.forget_window,font=("times new roman",15),bd=0,bg="white",fg="#B00857",cursor="hand2").place(x=350,y=340)

        btn_login = Button( frame1, text="Login",command=self.login, font=("times new roman", 20, "bold"), bg="#B00857", fg="white",cursor="hand2" ).place(
            x=150, y=400 ,width=185,height=40)

    def register_window(self):
        self.root.destroy()
        import regester

    def reset(self):
        self.cmb_question.current(0)
        self.txt_newpassword.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_email.delete(0,END)
    
    def change_password(self):
        if self.cmb_question.get()=="Select" or self.txt_answer.get()=="" or self.txt_newpassword.get()=="": 
            messagebox.showerror("Error","All fields are Required !",parent=self.root2)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
                cur=con.cursor()
                cur.execute("select * from member1  where email=%s and question=%s and answer=%s",(self.txt_email.get(),self.cmb_question.get(),self.txt_answer.get()))
                row=cur.fetchone() 
                if row==None:
                    messagebox.showerror("Error","Please Select correct security Question Or Enter Correct Answer !!",parent=self.root2)
                else:
                    cur.execute("update member1 set password=%s where email=%s",(self.txt_newpassword.get(),self.txt_email.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success"," Your Password has been Changed !!  Please Login with new Password",parent=self.root2)
                    
                    self.reset()
                    self.root2.destroy()
            except Exception as es:
                 messagebox.showerror( "Error", f"Error due to: {str( es )}", parent=self.root )





    def forget_window(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error","Please enter your  Email Address to reset your password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
                cur=con.cursor()
                cur.execute("select * from member1 where email=%s",self.txt_email.get())
                row=cur.fetchone() 
                if row==None:
                    messagebox.showerror("Error","Please enter your valid Email Address to reset your password",parent=self.root)
                else: 
                    con.close()
                    self.root2=Toplevel()
                    self.root2.title("Forget Password")
                    self.root2.geometry("500x550+530+144")
                    self.root2.focus_force()
                    self.root2.grab_set()
                    self.root2.config(bg="white")

                    t=Label(self.root2,text="Forget Password ",font=("times new roman",20,"bold"),bg="white",fg="red").place(x=0,y=10,relwidth=1)

                    lbl_question = Label( self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white",
                                        fg="gray" ).place( x=125, y=100 )
                    self.cmb_question =ttk.Combobox(self.root2, font=("times new roman", 15), state="readonly" )
                    self.cmb_question['values'] = ("Select", "Your first pet name", "Your Favourite sports", "Your best friend name")
                    self.cmb_question.place( x=125, y=140, width=250 )
                    self.cmb_question.current( 0 )

                    lbl_answer = Label( self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",
                                        fg="gray" ).place( x=125, y=190 )
                    self.txt_answer = Entry( self.root2, font=("times new roman", 19, "bold"), bg="lightgray" )
                    self.txt_answer.place( x=125, y=230, width=250 )

                    lbl_newpassword = Label( self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white",
                                        fg="gray" ).place( x=125, y=280 )
                    self.txt_newpassword = Entry( self.root2, font=("times new roman", 19, "bold"), bg="lightgray" )
                    self.txt_newpassword.place( x=125, y=320, width=250 )

                    btn_changepass=Button(self.root2,text="Change Password",font=("times new roman",18,"bold"),command=self.change_password,bg="green",fg="black",cursor="hand2").place(x=150,y=400)
                   

            except Exception as es:
                messagebox.showerror( "Error", f"Error due to: {str( es )}", parent=self.root )

        
            
    def login(self):
        if self.txt_email.get()=="" or  self.txt_password.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="emp1")
                cur=con.cursor()
                cur.execute("select * from member1  where email=%s and password=%s",(self.txt_email.get(),self.txt_password.get()))
                row=cur.fetchone() 
                if row==None:
                    messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
                else:
                    messagebox.showinfo("Success","WELCOME !",parent=self.root)
                    self.root.destroy()
                    import selector
                    con.close()

            except Exception as es:
                messagebox.showerror( "Error", f"Error due to: {str( es )}", parent=self.root )



root=Tk()
ob=login(root)
root.mainloop()