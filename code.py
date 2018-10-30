import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
from tkinter import ttk

db=mysql.connect(
     host='localhost',
     user='root',
     passwd='******' ,   
      database="Employee"
)
#***************** Execute only once ********************

''''cursor.execute("create database Employee")
db.commit()'''

#********************This also Execute only once as it create table in database***************************

'''cursor.execute('create table Employee(EmpNo integer primary key,EmpName Varchar(255),JoinDate varchar(255),DesignationCode Varchar(1),Department Varchar(255),Basic integer,HRA integer,IT integer)')

cursor.execute('create table dearness1(DesignationCode varchar(1) primary key,Designation varchar(255),DA integer)')
'''
entry=[]

def clear():
    e11.delete(0,tk.END)
    for en in entry:
        en.destroy()
        
def show():
    try:
        EmpNo=e11.get().strip()
        if len(EmpNo)>=1:
            query='select EmpNo,EmpName,Department,Designation,Basic+HRA+DA-IT as "Salary" from Employee inner join dearness1 on Employee.DesignationCode=dearness1.DesignationCode where EmpNo={}'.format(int(EmpNo))
            cursor.execute(query)
            result=cursor.fetchall()
            l=iter(['EmpNumber','EmpName','Department','Designation','Salary'])
            c=0
            global entry
            if len(result)>=1:
                for i in result:
                    for j in i:
                        label=tk.Label(tab1,text="\n"+next(l)+"  --> "+str(j),fg="black",font=30,width=30)
                        label.grid(row=2+c)
                        c=c+1
                        entry.append(label)
            else:
                messagebox.showerror("ERROR","THERE IS NO EMPLOYEE WITH EmpNo={}".format(EmpNo))
                e11.delete(0,tk.END)
        else:
            messagebox.showwarning("WARNING",'Please Enter Atleast something')
    except:
        messagebox.showwarning("WARNING",'Please Enter EmployeeNumber is Valid format')
        

def save():
    try:
        EmpNo=int(e21.get().strip())
        EmpolyeeName=e22.get().strip()
        JoinDate=e23.get().strip()
        DesignationCode=e24.get()
        Department=e25.get().strip()
        Basic=int(e26.get().strip())
        HRA=int(e27.get().strip())
        IT=int(e28.get().strip())
    
        query="insert into Employee values(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query,(EmpNo,EmpolyeeName,JoinDate,DesignationCode,Department,Basic,HRA,IT))
        
        Designation=e210.get()
        DA=int(e211.get())
        query='insert into dearness1 values(%s,%s,%s)'
        cursor.execute(query,(DesignationCode,Designation,DA))
        db.commit()
        
    except mysql.errors.IntegrityError:
        messagebox.showerror("Error","EmpNo is already Present,please check it")
        cursor.execute( "DELETE FROM Employee WHERE EmpNo = "+e21.get())
        cursor.execute( "DELETE FROM dearness1 WHERE DesignationCode = "+e24.get())
        db.commit()
    
    except ValueError:
        messagebox.showerror("Error","")
        cursor.execute( "DELETE FROM Employee WHERE EmpNo = "+e21.get())
        cursor.execute( "DELETE FROM dearness1 WHERE DesignationCode = "+e24.get())
        db.commit()
        
    except:
        messagebox.showerror('Error',"Please Enter the data in well defined format ,Please check it")
        cursor.execute( "DELETE FROM Employee WHERE EmpNo = "+e21.get())
        cursor.execute( "DELETE FROM dearness1 WHERE DesignationCode = "+e24.get())
        db.commit()
        
        
def clear1():
    e21.delete(0,tk.END)
    e22.delete(0,tk.END)
    e23.delete(0,tk.END)
    e24.delete(0,tk.END)
    e25.delete(0,tk.END)
    e26.delete(0,tk.END)
    e27.delete(0,tk.END)
    e28.delete(0,tk.END)
    e210.delete(0,tk.END)
    e211.delete(0,tk.END)
    
def delete():
    try:
        EmpNo=e31.get().strip()
        cursor.execute("select DesignationCode from Employee where EmpNo ="+EmpNo)
        result=cursor.fetchall()[0][0]
        cursor.execute("delete from Employee where EmpNo ="+EmpNo)
        db.commit()
        cursor.execute("delete from dearness1 where DesignationCode ="+"\'"+result+"\'")
        db.commit()
        messagebox.showinfo("Success","Successfully Deleted EmpNo "+EmpNo)
    except:
        messagebox.showerror("Error","No Employee with "+EmpNo+" number found.")
    
    
        
cursor=db.cursor()
root=tk.Tk()
root.title("DATABASE")
root.minsize(700,400)
root.resizable(0,0)


tabcontrol=ttk.Notebook(root)
tab1=ttk.Frame(tabcontrol)
tab2=ttk.Frame(tabcontrol)
tab3=ttk.Frame(tabcontrol)
tabcontrol.add(tab1,text="   RETRIEVE SECTION   ")
tabcontrol.add(tab2,text="   DATA ADDING SECTION   ")
tabcontrol.add(tab3,text="    DELETE SECTION    ")

tk.Label(tab1,text="Enter the EmployeeNumber (EmpNo)-->\n\n",fg="red",font=25,padx=40,pady=15).grid(row=0)
e11=tk.Entry(tab1,relief='sunken',bd=5)
e11.focus()
e11.grid(row=0,column=1,ipady=5)


tk.Button(tab1,text="RETRIEVE",fg='blue',command=show,font=25,width=40,bg='black',relief="groove").grid(row=1,column=0)
tk.Button(tab1,text="CLEAR",fg='blue',command=clear,font=25,width=40,bg='black',relief="groove").grid(row=1,column=1)

tk.Label(tab2,text="Enter the EmployeeNumber (EmpNo)-->(Integer)\n",fg="red",font=25,padx=20).grid(row=0)
e21=tk.Entry(tab2,relief='sunken',bd=5)
e21.focus()
e21.grid(row=0,column=1)

tk.Label(tab2,text="Enter the EmployeeName-->\n",fg="red",font=25,padx=20).grid(row=1)
e22=tk.Entry(tab2,relief='sunken',bd=5)
e22.grid(row=1,column=1)

tk.Label(tab2,text="Enter the joinig data in a format of DD\MM\YYYY-->\n",fg="red",font=25,padx=20).grid(row=2)
e23=tk.Entry(tab2,relief='sunken',bd=5)
e23.grid(row=2,column=1)

tk.Label(tab2,text="Enter the DesignationCode-->\n",fg="red",font=25,padx=20).grid(row=3)
e24=tk.Entry(tab2,relief='sunken',bd=5)
e24.grid(row=3,column=1)

tk.Label(tab2,text="Enter the Department-->\n",fg="red",font=25,padx=20).grid(row=4)
e25=tk.Entry(tab2,relief='sunken',bd=5)
e25.grid(row=4,column=1)

tk.Label(tab2,text="Enter the basic salary-->(Integer)\n",fg="red",font=25,padx=20,pady=5).grid(row=5)
e26=tk.Entry(tab2,relief='sunken',bd=5)
e26.grid(row=5,column=1)

tk.Label(tab2,text="Enter the HRA-->(Integer)\n",fg="red",font=25,padx=20).grid(row=6)
e27=tk.Entry(tab2,relief='sunken',bd=5)
e27.grid(row=6,column=1)

tk.Label(tab2,text="Enter the IT-->(Integer)\n",fg="red",font=25,padx=20).grid(row=7)
e28=tk.Entry(tab2,relief='sunken',bd=5)
e28.grid(row=7,column=1)


tk.Label(tab2,text="Enter the Designation-->\n",fg="red",font=25,padx=20).grid(row=8)
e210=tk.Entry(tab2,relief='sunken',bd=5)
e210.grid(row=8,column=1)

tk.Label(tab2,text="Enter the DA-->(Integer)\n",fg="red",font=25,padx=20).grid(row=9)
e211=tk.Entry(tab2,relief='sunken',bd=5)
e211.grid(row=9,column=1)

tk.Button(tab2,text="SAVE",fg='blue',command=save,font=25,width=40,bg='black',relief="groove").grid(row=10)
tk.Button(tab2,text="Clear",fg='blue',command=clear1,font=25,width=40,bg='black',relief="groove").grid(row=10,column=1)

tk.Label(tab3,text="Enter the EmployeeNumber (EmpNo)-->\n\n",fg="red",font=30,padx=40,pady=15).grid(row=0)
e31=tk.Entry(tab3,relief='sunken',bd=5)
e31.focus()
e31.grid(row=0,column=1,ipady=3)

tk.Button(tab3,text="DELETE",fg='blue',command=delete,font=25,width=40,bg='black',relief="groove").grid(row=1)


tabcontrol.grid()
root.mainloop()
