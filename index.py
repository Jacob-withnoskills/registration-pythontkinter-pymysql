from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql


class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("Registration Form")
        self.root.geometry("1920x1080+0+0")

        ##====image====

        self.bg =ImageTk.PhotoImage(file="index.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        ##====image2====

        self.lef =ImageTk.PhotoImage(file="das.png")
        lef=Label(self.root,image=self.lef).place(x=100,y=100,width=400,height=500)

        #====Frame=======

        frame=Frame(self.root,bg="bisque")
        frame.place(x=480,y=100,width=700,height=500)

        #===Entry=========

        title=Label(frame,text="Register Here",font=("Times New Roman",18,"bold"),bg="bisque",fg="green").place(x=50,y=30)

      
        fname=Label(frame,text="First Name",font=("Times New Roman",18,"bold"),bg="bisque",fg="green").place(x=50,y=100)
        self.txtname=Entry(frame,font=("Times New Roman",18),bg="lightgrey")
        self.txtname.place(x=50,y=130,width=250)

        Lname=Label(frame,text=" Last Name",font=("Times New Roman",18,"bold"),bg="bisque",fg="green").place(x=350,y=100)
        self.txtlname=Entry(frame,font=("Times New Roman",18),bg="lightgrey")
        self.txtlname.place(x=350,y=130,width=250)

        contact=Label(frame,text="Contact_No",font=("Times New Roman",18,"bold"),bg="bisque",fg="green").place(x=50,y=180)
        self.txtcontact=Entry(frame,font=("Times New Roman",18),bg="lightgrey")
        self.txtcontact.place(x=50,y=210,width=250)

        ename=Label(frame,text="Email",font=("Times New Roman",18,"bold"),bg="bisque",fg="green").place(x=350,y=180)
        self.txtename=Entry(frame,font=("Times New Roman",18),bg="lightgrey")
        self.txtename.place(x=350,y=210,width=250)


        answer=Label(frame,text="Security Questions",font=("Times New Roman",18,"bold"),bg="bisque",fg="green").place(x=50,y=250)
        self.cmb_quest=ttk.Combobox(frame,font=("Times New Roman",15),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=280,width=250)
        self.cmb_quest.current(0)
        

        sanswer=Label(frame,text="Answer",font=("Times New Roman",18,"bold"),bg="bisque",fg="green").place(x=350,y=250)
        self.txt_answer=Entry(frame,font=("Times New Roman",18),bg="lightgrey")
        self.txt_answer.place(x=350,y=280,width=250)

        password=Label(frame,text="Password",font=("Times New Roman",18,"bold"),bg="bisque",fg="green").place(x=50,y=330)
        self.password=Entry(frame,font=("Times New Roman",18),bg="lightgrey")
        self.password.place(x=50,y=360,width=250)

        cpassword=Label(frame,text="Confirm Password",font=("Times New Roman",18,"bold"),bg="bisque",fg="green").place(x=350,y=330)
        self.cpassword=Entry(frame,font=("Times New Roman",18),bg="lightgrey")
        self.cpassword.place(x=350,y=360,width=250)

        #===check====

        self.var_chk =IntVar()
        chk=Checkbutton(frame,text="I Agree The Terms & Conditions",variable = self.var_chk,bg="bisque",font=("Times New Roman",12)).place(x=50,y=400)

        self.btn_image=ImageTk.PhotoImage(file="SM.jpg")
        btn=Button(frame,image=self.btn_image,bd=0,cursor='hand2',command=self.register_data).place(x=50,y=430,height=45)

    def register_data(self):
        if self.txtname.get()==""or self.txtlname.get()==""or self.txtcontact.get()==""or self.txtename.get()==""or self.txt_answer.get()=="Select"or self.txt_answer.get()==""or self.password.get()==""or self.cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.password.get() !=  self.cpassword.get():
            messagebox.showerror("Error","Password Does not Match ",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Please","Agree the Terms & Conditions ",parent=self.root)
        else:
            try:
                conn= pymysql.connect(host="localhost",user="root",password="",database="SYSREG") 
                cur=conn.cursor()
                cur.execute("insert into REGSYS (FIRST_NAME,LAST_NAME,CONTACT_NO,EMAIL,SECURITY_QUESTIONS,ANSWER,PASSWORD) values(%s,%s,%s,%s,%s,%s,%s)",
                              (self.txtname.get(),
                              self.txtlname.get(),
                              self.txtcontact.get(),
                              self.txtename.get(),
                              self.cmb_quest.get(),
                              self.txt_answer.get(),
                              self.password.get()
                              ))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","You Successfully registered ",parent=self.root)              
            except Exception as ex:
                messagebox.showerror("Error",f"Error due too: {str(ex)}",parent=self.root)
                
             
root =Tk()
obj = Register(root)
root.mainloop()
