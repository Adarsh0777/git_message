from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import messagebox
import pymysql


class register:
    def __init__(self, root):
        self.root = root
        self.root.title( "Regestratioin Form" )
        self.root.geometry( "1915x1080" )

        self.bg = ImageTk.PhotoImage( file="img/black_background_red_color_paint_explosion_burst_9844_1920x1080.jpg" )
        bg = Label( self.root, image=self.bg ).place( relwidth=1, relheight=1 )

        self.left = ImageTk.PhotoImage( file="img/iStock-492878594.jpg" )
        left = Label( self.root, image=self.left ).place( x=80, y=144, width=450, height=550 )

        frame1 = Frame( self.root, bg="white" )
        frame1.place( x=530, y=144, width=750, height=550 )

        title = Label( frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white",
                       fg="green" ).place( x=60, y=30 )

        lbl_fname = Label( frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white",
                           fg="gray" ).place( x=60, y=100 )
        self.txt_fname = Entry( frame1, font=("times new roman", 15, "bold"), bg="lightgray" )
        self.txt_fname.place( x=60, y=130, width=250 )

        lbl_lname = Label( frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white",
                           fg="gray" ).place( x=450, y=100 )
        self.txt_lname = Entry( frame1, font=("times new roman", 15, "bold"), bg="lightgray" )
        self.txt_lname.place( x=450, y=130, width=250 )

        lbl_contact = Label( frame1, text="Contact No:", font=("times new roman", 15, "bold"), bg="white",
                             fg="gray" ).place( x=60, y=170 )
        self.txt_contact = Entry( frame1, font=("times new roman", 15, "bold"), bg="lightgray" )
        self.txt_contact.place( x=60, y=200, width=250 )

        lbl_email = Label( frame1, text="E-Mail", font=("times new roman", 15, "bold"), bg="white", fg="gray" ).place(
            x=450, y=170 )
        self.txt_email = Entry( frame1, font=("times new roman", 15, "bold"), bg="lightgray" )
        self.txt_email.place( x=450, y=200, width=250 )

        lbl_question = Label( frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white",
                              fg="gray" ).place( x=60, y=240 )
        self.cmb_question =ttk.Combobox( frame1, font=("times new roman", 15), state="readonly" )
        self.cmb_question['values'] = ("Select", "Your first pet name", "Your Favourite sports", "Your best friend name")
        self.cmb_question.place( x=60, y=270, width=250 )
        self.cmb_question.current( 0 )

        lbl_answer = Label( frame1, text="Security Answer", font=("times new roman", 15, "bold"), bg="white",
                            fg="gray" ).place( x=450, y=240 )
        self.txt_answer = Entry( frame1, font=("times new roman", 15, "bold"), bg="lightgray" )
        self.txt_answer.place( x=450, y=270, width=250 )

        lbl_password = Label( frame1, text="Enter Password", font=("times new roman", 15, "bold"), bg="white",
                              fg="gray" ).place( x=60, y=310 )
        self.txt_password = Entry( frame1, font=("times new roman", 15, "bold"), bg="lightgray" )
        self.txt_password.place( x=60, y=340, width=250 )

        lbl_cpassword = Label( frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white",
                               fg="gray" ).place( x=450, y=310 )
        self.txt_cpassword = Entry( frame1, font=("times new roman", 15, "bold"), bg="lightgray" )
        self.txt_cpassword.place( x=450, y=340, width=250 )
        self.chk_var = IntVar()
        chk = Checkbutton( frame1, text="I agree with the terms and condition", variable=self.chk_var, onvalue=1,
                           offvalue=0, bg="white", font=("times new roman", 15) ).place( x=60, y=400 )

        reg_btn = Button( frame1, text="Register Now", font=("times new roman", 15, "bold"), bd=0, bg="green",
                          fg="white", cursor="hand2", command=self.register_data ).place( x=60, y=460, width=250,
                                                                                          height=40 )
        signin_btn = Button( self.root, text="Sign In",command=self.loginn_window, font=("times new roman", 15, "bold"), bd=0, bg="blue",
                             fg="white", cursor="hand2" ).place( x=230, y=172, width=180, height=50 )

    def loginn_window(self):
        self.root.destroy()
        import login
    def clear(self):
        self.txt_fname.delete(0,END),
        self.txt_lname.delete( 0, END ),
        self.txt_contact.delete( 0, END ),
        self.txt_email.delete( 0, END ),
        self.cmb_question.current( 0),
        self.txt_answer.delete( 0, END ),
        self.txt_password.delete( 0, END ),
        self.txt_cpassword.delete(0,END)



    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or self.cmb_question.get() == "Select" or self.txt_answer.get() == "" or self.txt_password.get() == "" or self.txt_cpassword.get() == "":
            messagebox.showerror( "Error", "Sorry all fields are required !!", parent=self.root )
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror( "Error", "Sorry Password is Missmatch !!", parent=self.root )
        elif self.chk_var.get() == 0:
            messagebox.showerror( "Error", "Please Agree with our terms and conditions !!", parent=self.root )

        else:
            try:
                con = pymysql.connect( host="localhost", user="root", password="", database="emp1" )
                cur = con.cursor()
                cur.execute("select * from member1 where email=%s",self.txt_email.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","User Alresdy exist Please Log in !",parent=self.root)
                else:
                    cur.execute(" insert into member1 (f_name, l_name, contact, email, question, answer, password) values(%s,%s,%s,%s,%s,%s,%s)",
                        (self.txt_fname.get(),
                         self.txt_lname.get(),
                         self.txt_contact.get(),
                         self.txt_email.get(),
                         self.cmb_question.get(),
                         self.txt_answer.get(),
                         self.txt_password.get()
                         ))

                    con.commit()
                    con.close()
                    messagebox.showinfo( "Success", "Regestration successfull !!", parent=self.root )
                    self.clear()
            except Exception as es:
                messagebox.showerror( "Error", f"Error due to: {str( es )}", parent=self.root )


root = Tk()
ob = register( root )
root.mainloop()
