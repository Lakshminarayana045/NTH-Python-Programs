from pandas import *
from numpy import *
from pymysql import *

#===========================================  Series ======================================================================

# Python List
'''
names = ['lucky','madhu','venky']
da = Series(names)
print(da)
'''
# Python Dict
'''
emp = {'name':'Sai', 'salary':20000, 'company':['TCS','Capgemini','Infosys'], 'hTown':'Hyd'}
data = Series(emp)
print(data)
'''
# Numpy Array
'''
name = array(['sai','revi','raju','lucky','venky'])
data = Series(name)
print(data)
'''
#=========================================  DataFrame  =========================================================================

# Python Object
'''
na = ['lucky','madhu','venky']
lo = ['hyd','ong','kdkr']
ge = ['Male','Female','Male']

students = {'Names':na,'Location':lo,'Gender':ge}
num = [10,20,30]

data = DataFrame(students,num)
print(data)
'''

# Database Table
'''
con = connect(host = 'localhost',user = 'root',password = '8179' , db = 'student')
c = con.cursor()
c.execute('select * from emoployeesdata;')
data = c.fetchall()
'''
((101, 'Virat', 'Kohli', 22, 'TCS', 20000, 'Hyderabad', 'Python', 2, 'unmarried'),
 (102, 'Rohit', 'Sharma', 24, 'Wipro', 30000, 'Pune', 'Django', 3, 'unmarried'),
 (103, 'Surya', 'Yadav', 20, 'Infosys', 19000, 'Chennai', 'Python', 1, 'unmarried'),
 (104, 'Sachin', 'Tendulkarm', 25, 'Microsoft', 35000, 'Mumbai', 'Flask', 5, 'married'),
 (105, 'Hardik', 'Panday', 22, 'TCS', 20000, 'Delhi', 'Flask', 1, 'unmarried'),
 (106, 'Rishabh', 'Pant', 23, 'CTS', 23000, 'Mumbai', 'Java', 2, 'unmarried'),
 (107, 'Jasprit', 'Bumrah', 21, 'Microsoft', 26000, 'Hyderabad', 'Flask', 2, 'unmarried'),
 (108, 'Dinesh', 'Karthik', 24, 'CTS', 24000, 'Delhi', 'Java', 3, 'married'),
 (109, 'Sanju', 'Samson', 22, 'Infosys', 22500, 'Chennai', 'Python', 2, 'unmarried'),
 (110, 'MS', 'Dhoni', 25, 'TCS', 30000, 'Chennai', 'Python', 5, 'married'),
 (111, 'Ravindra', 'Jadeja', 24, 'lnfosys', 29000, 'Mumbai', 'Django', 4, 'married'),
 (112, 'Kuldeep', 'Yadav', 30, 'Microsoft', 28000, 'Delhi', 'python', 4, 'married'),
 (113, 'Axar', 'Patel', 26, 'CTS', 27000, 'Chennai', 'Java', 5, 'married'),
 (114, 'Ambati', 'Rayudu', 28, 'TCS', 31000, 'Pune', 'python', 5, 'married'),
 (115, 'Gautham', 'Gambhir', 31, 'Microsoft', 32000, 'chennai', 'Python', 6, 'Married'))
'''
n=[]
c=[]
l=[]
s=[]
for i in data:
    n.append(i[1])
    c.append(i[7])
    l.append(i[6])
    s.append(i[5])

emps = {'Names':n,'Course':c,'Location':l,'Salaries':s}
a = DataFrame(emps)
print(a)
'''
# Text File
'''
data = open('C:\\Users\\LUCKY\\AppData\\Local\\Programs\\Python\Python311\\luckydata.txt')
#data = open('luckydata.txt')
da = data.readlines()
'''
['Rani,90,NTH,hyd,5000\n',
 'Soni,99,ABC,Bang,10000\n',
 'Moui,80,XYZ,Chennai,90000\n',
 'Juni,85,ABC,Hyd,5000']
'''
n=[]
m=[]
l=[]
c=[]
s=[]
for i in da:
    x = i.replace('\n',',').split(',')
    n.append(x[0])
    m.append(x[1])
    l.append(x[2])
    c.append(x[3])
    s.append(x[4])
stu = {'names':n,'marks':m,'Location':l,'Course':c,'Salaries':s}
data1 = DataFrame(stu)
print(data1)
'''
# Database Table & Text File

con = connect(host = 'localhost',user = 'root',password = '8179' , db = 'student')
c = con.cursor()
c.execute('select * from course;')
data = c.fetchall()
'''
((11, 'Python', 3000, 1),
 (12, 'Django', 4000, 2),
 (13, 'Java', 4000, 3),
 (14, 'UI', 500, 6),
 (15, 'Sql', 1000, 7))
'''
s=[]
co=[]
for i in data:
    s.append(i[-2])
    co.append(i[1])
    
    
data = open('mldata.txt')
da = data.readlines()
'''
['TCS,Kohli,Dhoni,Surya,Yadav\n',
 'WIPRO,Nani,Ramesh,Kohli,Sai\n',
 'INFOSYS,Renu,Ram,Satya,Charan,Dhoni\n',
 'CTS,Kohli,Aakash,Prakash,Ramesh,Sai\n',
 'IBM,Lucky,Venky,Siddu,Revi']
'''
n=[]
c=[]
for i in da:
    a=i.split(',')
    n.append(a[1])
    c.append(a[0])

students = {'Names':n,'Company':c,'Salaries':s,'Course':co}
s1 = DataFrame(students)
print(s1)
