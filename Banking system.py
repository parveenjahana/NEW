from tkinter import*

from tkinter import ttk
from tkinter import messagebox
from time import gmtime,strftime
from PIL import Image,ImageTk
root=Tk()
root.geometry("1700x1700")
root.config(bg="white")
bg_image=Image.open("C:\\Users\\jahan\\Downloads\\bank.jpg")
bg_image=bg_image.resize((1500,1500),Image.LANCZOS)
bg_photo=ImageTk.PhotoImage(bg_image)
bg_Label=Label(root,image=bg_photo)
bg_Label.place(x=0,y=0)
l0=Label(root,text="SOUTH INDIAN BANKING SYSTEM",bg="yellow",fg="red",padx=1000,pady=9)
l0.config(font=("arial",30,"bold"))
l0.pack()
def login():

 root1=Tk()
 root1.geometry("1700x1700")
 root1.config(bg="yellow")
 l1=Label(root1,text="enter name",fg="red",bg="yellow")
 l1.place(x=100,y=200)
 l1.config(font=("arial",25))
 t1=Entry(root1)
 t1.place(x=350,y=200)  

 l2=Label(root1,text="Enter name ",fg="red",bg="yellow")
 l2.place(x=100,y=300)
 l2.config(font=("arial",25))
 t2=Entry(root1)
 t2.place(x=350,y=300)

 l3=Label(root1,text="Enter openning credit",fg="red",bg="yellow")
 l3.place(x=100,y=400)
 l3.config(font=("arial",25))
 t3=Entry(root1)
 t3.place(x=350,y=400)

 l4=Label(root1,text="Enter pin",fg="red",bg="yellow")
 l4.place(x=100,y=500)
 l4.config(font=("arial",25))
 t4=Entry(root1)
 t4.place(x=350,y=500)
 def credit():
     root3=Tk()
     root3.geometry("1700x1700")
     root3.config(bg="yellow")
     b1=Button(root3,text="credi t amount in your account",fg="red",bg="white")
     b1.config(font=("arial",30))
     b1.place(x=100,y=100)
     b2=Button(root3,text="debit amount in your account",fg="red",bg="white")
     b2.config(font=("arial",30))
     b2.place(x=100,y=300)
     b3=Button(root3,text="check balance",fg="red",bg="white")
     b3.config(font=("arial",30))
     b3.place(x=800,y=100)
     b4=Button(root3,text="view transaction",fg="red",bg="white")
     b4.config(font=("arial",30))
     b4.place(x=800,y=300)
     b4=Button(root3,text="logout",fg="red",bg="yellow")
     b4.config(font=("arial",30))
     b4.place(x=400,y=500)
 b2=Button(root1,text="submit",fg="red",bg="white",padx=20,pady=8,command=credit)
 b2.config(font=("arial",30))
 b2.place(x=400,y=600)

b1=Button(root,text="login",fg="red",bg="yellow",padx=20,pady=8,command=login)
b1.config(font=("arial",30))
b1.place(x=500,y=220)
def create():
    root2=Tk()
    root2.geometry("1700x1700")
    root2.config(bg="yellow")
    l1=Label(root2,text="enter name",fg="red",bg="yellow")
    l1.place(x=100,y=200)
    l1.config(font=("arial",25))
    t1=Entry(root2)
    t1.place(x=500,y=200)
    
    l2=Label(root2,text="enter account number",fg="red",bg="yellow")
    l2.place(x=100,y=300)
    l2.config(font=("arial",25))
    t2=Entry(root2)
    t2.place(x=500,y=300)
    b3=Button(root2,text="submit",fg="red",bg="white")
    b3.config(font=("arial",30))
    b3.place(x=400,y=600)
    b4=Button(root2,text="home",fg="red",bg="white")
    b4.config(font=("arial",30))
    b4.place(x=700,y=600)
b2=Button(root,text="create new account",fg="red",bg="yellow",command=create)
b2.place(x=360,y=500)
b2.config(font=("arial",30))
root.mainloop()



    

 
            
