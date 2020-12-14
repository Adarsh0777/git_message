from tkinter import *
from PIL import Image,ImageTk

class selector:
    def __init__(self,root):
        self.root = root
        self.root.title("Student & Employee")
        self.root.geometry("1915x1080")

        Background = Label( self.root,bg="turquoise1").place( relwidth=1, relheight=1 )

        title=Label(self.root,text="Student & Employee management system",bd=8, relief=GROOVE, font=("times new roman",40,"bold"),bg="#B00857",fg="white")
        title.pack(side=TOP,fill=X)

        

        self.left = ImageTk.PhotoImage( file="img/176-1761112_company-indian-students-images-png.png" )
        left = Label( self.root, image=self.left ).place( x=150, y=180, width=600, height=400 )
        
        self.right = ImageTk.PhotoImage( file="img/Best-Black-Backgrounds-Free-Download-768x432.jpg" )
        right = Label( self.root, image=self.right ).place( x=780, y=180, width=600, height=400 )

        btn_stud=Button(self.root,text="Student Records ",command=self.stud,font=("times new roman",20,"bold"),bg="#B00857",fg="white",cursor="hand2").place(x=300,y=520,width=300,height=50)
        btn_emp= Button(self.root, text="Employee Record",command=self.emp, font=("times new roman", 20, "bold"), bg="#B00857", fg="white",cursor="hand2" ).place( x=935, y=520 ,width=300,height=50)

    def stud(self):
        self.root.destroy()
        import student

    def emp(self):
        self.root.destroy()
        import employee

root=Tk()
ob=selector(root)
root.mainloop()