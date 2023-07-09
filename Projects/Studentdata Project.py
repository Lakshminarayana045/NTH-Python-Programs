from tkinter import *
from tkinter import ttk
import pymysql
class sims:
    def __init__(self,root):
        self.root=root
        self.root.title("Lucky")
        self.root.geometry('1500x800')
        title1=Label(text='NTH Students Information',
                     font=('Cooper Black',30),
                     bg='green',fg='white',bd=5,relief=GROOVE)
        title1.pack(fill='x')

        #Variables
        self.rollnoVar=StringVar()
        self.fnameVar=StringVar()
        self.lnameVar=StringVar()
        self.courseVar=StringVar()
        self.emailidVar=StringVar()
        self.mobileVar=StringVar()
        self.instituteVar=StringVar()
        
        #Creating Data Entry Frame
        dataEntryFrame=Frame(self.root,bg='cyan',bd=5,relief=GROOVE)
        dataEntryFrame.place(x=8,y=60,width=450,height=735)

        #Creating Date Display frame
        dataDisplayFrame=Frame(self.root,bg='bisque2',bd=5,relief=GROOVE)
        dataDisplayFrame.place(x=460,y=60,width=1070,height=735)

        #Using DataEntryframe
        title2=Label(dataEntryFrame,text='Data Entry Here',font=('Cooper Black',15),bg='cyan',fg='black')
        title2.grid(row=0,columnspan=2,padx=100,pady=10)
        
        #Roll no
        rollNo=Label(dataEntryFrame,text='Roll no:',font=('Britannic',15),bg='cyan',fg='black')
        rollNo.grid(row=1,column=0,sticky='W',padx=5)

        rollnoEntry=Entry(dataEntryFrame,textvariable=self.rollnoVar,font=('Britannic',15))
        rollnoEntry.grid(row=1,column=1,sticky='E',pady=30)

        #First name
        fname=Label(dataEntryFrame,text='First Name:',font=('Britannic',15),bg='cyan',fg='black')
        fname.grid(row=2,column=0,sticky='W',padx=5)

        fnameEntry=Entry(dataEntryFrame,textvariable=self.fnameVar,font=('Britannic',15))
        fnameEntry.grid(row=2,column=1,sticky='E')

        #last name
        lname=Label(dataEntryFrame,text='Last Name:',font=('Britannic',15),bg='cyan',fg='black')
        lname.grid(row=3,column=0,sticky='W',padx=5)

        lnameEntry=Entry(dataEntryFrame,textvariable=self.lnameVar,font=('Britannic',15))
        lnameEntry.grid(row=3,column=1,sticky='E',pady=30)

        #course name
        cname=Label(dataEntryFrame,text='Course Name:',font=('Britannic',15),bg='cyan',fg='black')
        cname.grid(row=4,column=0,sticky='W',padx=5)

        cnameEntry=Entry(dataEntryFrame,textvariable=self.courseVar,font=('Britannic',15))
        cnameEntry.grid(row=4,column=1,sticky='E')

        #Email id
        email=Label(dataEntryFrame,text='Email ID:',font=('Britannic',15),bg='cyan',fg='black')
        email.grid(row=5,column=0,sticky='W',padx=5)

        emailEntry=Entry(dataEntryFrame,textvariable=self.emailidVar,font=('Britannic',15))
        emailEntry.grid(row=5,column=1,sticky='E',pady=30)

        #Mobile
        Mobile=Label(dataEntryFrame,text='Mobile No:',font=('Britannic',15),bg='cyan',fg='black')
        Mobile.grid(row=6,column=0,sticky='W',padx=5)

        MobileEntry=Entry(dataEntryFrame,textvariable=self.mobileVar,font=('Britannic',15))
        MobileEntry.grid(row=6,column=1,sticky='E')

        #Institute
        iname=Label(dataEntryFrame,text='Institute Name:',font=('Britannic',15),bg='cyan',fg='black')
        iname.grid(row=7,column=0,sticky='W',padx=5)

        inameEntry=Entry(dataEntryFrame,textvariable=self.instituteVar,font=('Britannic',15))
        inameEntry.grid(row=7,column=1,sticky='E',pady=30)

        #Creating Button Frame
        btnFrame=Frame(dataEntryFrame,bd=5,relief=GROOVE,bg='pink')
        btnFrame.place(x=30,y=500,width=375,height=150)

        #Using Button and Creating buttons
        addbtn=Button(btnFrame,text='Add',command=self.addingData,font=('Britannic Bold',15),bg='purple',fg='white')
        addbtn.grid(row=0,column=0,padx=12,pady=50)

        updatebtn=Button(btnFrame,text='Update',command=self.updatingData,font=('Britannic Bold',15),bg='blue',fg='yellow')
        updatebtn.grid(row=0,column=1,padx=12,pady=50)

        deletebtn=Button(btnFrame,text='Delete',command=self.deletingData,font=('Britannic Bold',15),bg='green',fg='black')
        deletebtn.grid(row=0,column=2,padx=12,pady=50)

        clearbtn=Button(btnFrame,text='Clear',command=self.clearingData,font=('Britannic Bold',15),fg='maroon')
        clearbtn.grid(row=0,column=3,padx=12,pady=50)

        #Using DataDisplay
        title3=Label(dataDisplayFrame,text='Data Display Here..',font=('Cooper Black',15),bg='bisque2',fg='black')
        title3.place(x=350,y=10)

        tableFrame=Frame(dataDisplayFrame,bg='pink',bd=5,relief=RAISED)
        tableFrame.place(x=20,y=55,width=1000,height=450)

        self.studentsinfo=ttk.Treeview(tableFrame,columns=('rollno','fname','lname','course','emailid','mobile','institute'))

        self.studentsinfo.heading('rollno',text='Roll No')
        self.studentsinfo.heading('fname',text='First Name')
        self.studentsinfo.heading('lname',text='Last Name')
        self.studentsinfo.heading('course',text='Course Name')
        self.studentsinfo.heading('emailid',text='Email ID')
        self.studentsinfo.heading('mobile',text='Mobile')
        self.studentsinfo.heading('institute',text='Institute')

        self.studentsinfo['show']='headings'

        self.studentsinfo.column('rollno',width=100,anchor='center')
        self.studentsinfo.column('fname',width=120,anchor='center')
        self.studentsinfo.column('lname',width=150,anchor='center')
        self.studentsinfo.column('course',width=120,anchor='center')
        self.studentsinfo.column('emailid',width=140,anchor='center')
        self.studentsinfo.column('mobile',width=120,anchor='center')
        self.studentsinfo.column('institute',width=120,anchor='center')
        self.fetchingData()
        
        self.studentsinfo.bind("<ButtonRelease-1>",self.get_cursorrow)
        self.studentsinfo.pack()
    # Adding data
    def addingData(self):
        connection=pymysql.connect(host='localhost',user='root',password='8179',db='pythonprojectdb')
        c=connection.cursor()
        c.execute('insert into studentsdata values(%s,%s,%s,%s,%s,%s,%s)',
                  (self.rollnoVar.get(),self.fnameVar.get(),self.lnameVar.get(),
                   self.courseVar.get(),self.emailidVar.get(),self.mobileVar.get(),
                   self.instituteVar.get()))
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()
    # Clear Form    
    def clearingData(self):
        self.rollnoVar.set('')
        self.fnameVar.set('')
        self.lnameVar.set('')
        self.courseVar.set('')
        self.emailidVar.set('')
        self.mobileVar.set('')
        self.instituteVar.set('')
    # Retrive Data
    def fetchingData(self):
        connection=pymysql.connect(host='localhost',user='root',password='8179',db='pythonprojectdb')
        c=connection.cursor()
        c.execute('select * from studentsdata;')
        data=c.fetchall()
        if len(data)!=0:
            self.studentsinfo.delete(*self.studentsinfo.get_children())
            for i in data:
                self.studentsinfo.insert('',END,value=i)
            connection.commit()
        connection.close()

    def get_cursorrow(self,a):
        cursor_row=self.studentsinfo.focus()
        content=self.studentsinfo.item(cursor_row)
        row=content['values']
        self.rollnoVar.set(row[0])
        self.fnameVar.set(row[1])
        self.lnameVar.set(row[2])
        self.courseVar.set(row[3])
        self.emailidVar.set(row[4])
        self.mobileVar.set(row[5])
        self.instituteVar.set(row[6])
    # Updating data
    def updatingData(self):
        connection=pymysql.connect(host='localhost',user='root',password='8179',db='pythonprojectdb')
        c=connection.cursor()
        c.execute('update studentsdata set fname=%s,lname=%s,course=%s,emailid=%s,mobile=%s,institute=%s where rollno=%s',
                  (self.fnameVar.get(),
                   self.lnameVar.get(),
                   self.courseVar.get(),
                   self.emailidVar.get(),
                   self.mobileVar.get(),
                   self.instituteVar.get(),
                   self.rollnoVar.get()))
        
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()
    # Deleting Data
    def deletingData(self):
        connection=pymysql.connect(host='localhost',user='root',password='8179',db='pythonprojectdb')
        c=connection.cursor()
        c.execute('delete from studentsdata where rollno = %s',self.rollnoVar.get())
        connection.commit()
        self.fetchingData()
        self.clearingData()
        connection.close()
                        
root=Tk()
s=sims(root)

