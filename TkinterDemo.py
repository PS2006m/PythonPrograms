from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def create_conn():
    return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="python_3"
        )
def insert_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("Insert Status","All Fields are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="Insert into student_t(fname,lname,email,mobile) values (%s,%s,%s,%s)"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get())
        cursor.execute(query,args)
        conn.commit()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Insert Status","Data Inserted Succesfully")

def search_data():
     e_fname.delete(0,'end')
     e_lname.delete(0,'end')
     e_email.delete(0,'end')
     e_mobile.delete(0,'end')
     
     if e_id.get()=="":
         msg.showinfo("Search Status","All fields are mandatory")
     else:
        conn=create_conn()
        cursor=conn.cursor()
        query="Select * from student_t where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            e_fname.insert(0,row[0][1])
            e_lname.insert(0,row[0][2])
            e_email.insert(0,row[0][3])
            e_mobile.insert(0,row[0][4])
        else:
            msg.showinfo("Search Status","No Data Found")
        conn.close()

def update_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" or e_id.get()=="":
        msg.showinfo("Insert Status","All Fields are Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="Update student_t set fname=%s,lname=%s,email=%s,mobile=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get())
        cursor.execute(query,args)
        conn.commit()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Update Status","Data Updated Succesfully")
        conn.close()

def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","All fields are mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="Delete from student_t where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Delete Status","Data Delete Succesfully")
        conn.close()
        

root=Tk()
root.geometry("300x370")
root.title("My Tkinter Example")
root.resizable(width=False,height=True)

l_id=Label(root,text="ID")
l_id.place(x=50,y=50)

l_fname=Label(root,text="FIRST NAME")
l_fname.place(x=50,y=100)

l_lname=Label(root,text="LAST NAME")
l_lname.place(x=50,y=150)

l_email=Label(root,text="EMAIL")
l_email.place(x=50,y=200)

l_mobile=Label(root,text="MOBILE")
l_mobile.place(x=50,y=250)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

insert=Button(root,text="INSERT",bg="black",fg="white",font=("Arial",10),command=insert_data)
insert.place(x=20,y=300)

search=Button(root,text="SEARCH",bg="black",fg="white",font=("Arial",10),command=search_data)
search.place(x=80,y=300)

update=Button(root,text="UPDATE",bg="black",fg="white",font=("Arial",10),command=update_data)
update.place(x=148,y=300)

delete=Button(root,text="DELETE",bg="black",fg="white",font=("Arial",10),command=delete_data)
delete.place(x=214,y=300)

root.mainloop()
