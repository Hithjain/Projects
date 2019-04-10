from tkinter import *
import sqlite3
from tkinter import messagebox


root = Tk()
root.geometry('600x600')
root.title("Registration Form")


Fullname=StringVar()
Email=StringVar()
var = IntVar()
c=StringVar()
var1= IntVar()



def database():
   name1=Fullname.get()
   email=Email.get()
   gender=var.get()
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('data.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student1 (Fullname TEXT,Email TEXT,Gender TEXT,Year TEXT,Preference TEXT)')
   cursor.execute('INSERT INTO Student1 (Fullname,Email,Gender,Year,Preference) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog))
   conn.commit()
   messagebox.showinfo("Thanks","Thanks for Registering!!")
   exit()
   
   
             
label_0 = Label(root, text="Zodiac Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname,width=50)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Email, width=50)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="Year",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['F.E','S.E','T.E','B.E'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your year') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Preference",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
var3=IntVar()
var4=IntVar()
Checkbutton(root, text="Marketing", variable=var1).place(x=235,y=330)
Checkbutton(root, text="Technical", variable=var2).place(x=320,y=330)
Checkbutton(root, text="Creative", variable=var3).place(x=400,y=330)
Checkbutton(root, text="Publicity", variable=var4).place(x=480,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

root.mainloop()
