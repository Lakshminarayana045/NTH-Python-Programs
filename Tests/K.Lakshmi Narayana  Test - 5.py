# ==================================================== Set-2 ==============================================================
'''
+------+----------+---------------+----------------+------------+--------------------+-----------+------+----------------------+
| id   | name     |qualification  |passedout_year  | percentage | col_name           | hometown  | age  | mail_id              |
+------+----------+---------------+----------------+------------+--------------------+-----------+------+----------------------+
|  101 | Renuka   | MCA           |           2016 |       92.5 | AC College         | Nagapur   |   28 | renuka@gmail.com     |
|  102 | Ramya    | BTech         |           2022 |         90 | NTH College        | Hyderabad |   25 | ramya_nth@gmail.com  |
|  103 | Manjusha | Btech         |           2021 |         89 | GNIT College       | Guntur    |   28 | manju@reddif.com     |
|  104 | Lahari   | MTech         |           2022 |         70 | ABC College        | Mumbai    |   26 | lahari123@gmail.com  |
|  105 | Raghav   | BSc           |           2018 |         90 | NRM College        | Hyderabad |   26 | raghava_py@gmail.com |
|  106 | Chandra  | BTech         |           2020 |         99 | KCR College        | Hyderabad |   25 | chandra@gmail.com    |
|  107 | Suma     | MCom          |           2008 |         66 | ANR Degree College | Chennai   |   30 | suma_mcom@gmail.com  |
|  108 | Rajesh   | MTech         |           2016 |         55 | NTH College        | Bangalore |   27 | rajesh@yahoo.com     |
|  109 | Surya    | MCA           |           2018 |         60 | JNIT College       | Bangalore |   26 | surya_py@gmail.com   |
|  110 | Ramya    | MCA           |           2010 |         99 | NTH College        | Hyderabad |   33 | ramya@gmail.com      |
+------+----------+---------------+----------------+------------+--------------------+-----------+------+----------------------+
'''


from pymysql import *
a = connect(host = 'localhost',user = 'root',password = '8179',db = 'test5')
b = a.cursor()
b.execute(" select * from students " )
a.commit()
data = b.fetchall()



#1.Write a program to fetch  all students names where hometown Guntur
#print([i[1] for i in data if 'Guntur' in i ])

#2.Write a program to fetch  all students and their qualification and passedout_year
#print([i[1],i[2],i[3] for i in data])

#3.Write a program to fetch  all students names and who are done MCA from NTH college
#print([i[1] for i in data if 'MCA' in i and 'NTH College' in i])

#4.Write a program to fetch  all students names who are not done BTech
#print([i[1] for i in data if 'BTech' not in i ])

#5.Write a program to fetch  all students names who are done BTech Before 2020
#print([i[1] for i in data if str('2020') > str(i) and 'BTech' in i ])

#6.Write a program to fetch students names who are got hightest percentage
'''
p=[]
for i in data:
    p.append(i[4])
for i in  data:
    if i[4] == max(p):
        print(i[4])
'''
#7.Write a program to fetch students names who are not from Bangalore but done MCA
#print([i[1] for i in data if 'MCA' in i and 'Bangalore' not in i])

#8.what is the percentage of MCA student who passout_year is 2018
#print([ i[4] for i in data if 'MCA' in i and str('2018') in str(i[3])])

#9.what is gmil account of students who has done Bsc from Hydrabad
#print([ i[-1] for i in data if 'BSc' in i[2] and 'Hyderabad' in i[6]])

#10.what is student name who are mumbai
#print([i[1] for i in data if 'Mumbai' in i[6]])

#11.how many students are there from nth college
#print(len([ i[1] for i in data if 'NTH College' in i[5]]))

#12.what is qualifictaion of the student whose passedout very recently
'''
p=[]
for i in data:
    p.append(i[3])
for i in data:
    if i[3] == max(p):
        print(i[2])

'''


#13. What is the percentage of student who studied in KCR College?
#print([ i[4] for i in data if 'KCR College' in i[5]])

#14. Write a program to fetch student name who is senior of all students?
'''
s=[]
for i in data:
    s.append(i[3])
for i in data:
    if i[3] == min(s):
        print(i[1])
'''
#15. Write a program to fetch student name who has done BTech with high percentage?
'''
p=[]
for i in data:
    p.append(i[4])
for i in data:
    if i[4] == max(p):
        print(i[1])
'''
#16. What is Qualification of Ramya?
#print([i[2] for i in data if i[1] == 'Ramya' ])

#17. How many students are done MTech?
#print([ i[1] for i in data if i[2] == 'MTech' ])

#18. What is the college name of student who got highest percentage?
'''
p=[]
for i in data:
    p.append(i[4])
for i in data:
    if i[4] == max(p):
        print(i[5])
'''
#19. What is the hometown of student who has done BTech in 2020?
#print([ i[6] for i in data if i[2] == 'BTech' and str(i[3]) == str('2020')])

#20. What is the age of student who has done BSC with 90 percentage?
#print([i[7] for i in data if str(i[4]) in str('90') and i[2] =='BSc'])

#21. How many students passedout in 2022?
#print(len([i[1] for i in data if str('2022') == str(i[3])]))

#22. How many students got more then 90 percentage? 
#print(len([i[1] for i in data if str(i[4]) > str(90.00)]))

#23. What is the age of student who got less percentage in MCA?
'''
p=[]
for i in data:
    p.append(i[4])
for i in data:
    if 'MCA' in i[2] and i[4] == min(p):
        print(i[1])

'''
#24. What are the students name who are more then 30 years
#print([i[1] for i in data if i[7] > 30])


#25. What is the name of the college whose student name has more characters
'''
a=[]
for i in data:
    a.append(i[1])
for j in a:
    print(len(j))
for i in data:
    if len(i[1]) ==len(j):
        print(i[5])
'''

# ================================================ Set-3 ================================================================
"""
import pymysql as pm
connection=pm.connect(host='localhost',user='root',password='nari',db='test')
c=connection.cursor()
c.execute('''insert into students values(101, 'Renuka', 'MCA', 2016, 92.5, 'AC College','Nagapur',28,'renuka@gmail.com'),
				    (102, 'Ramya', 'BTech', 2022, 90, 'NTH College', 'Hyderabad',25, 'ramya_nth@gmail.com'),
				    (103, 'Manjusha', 'Btech', 2021, 89, 'GNIT College', 'Guntur',28, 'manju@reddif.com'),
				    (104, 'Lahari', 'MTech', 2022, 70, 'ABC College', 'Mumbai',26, 'lahari123@gmail.com'),
				    (105, 'Raghav', 'BSc', 2018, 90, 'NRM College', 'Hyderabad',26, 'raghava_py@gmail.com'),
				    (106, 'Chandra', 'BTech', 2020, 99, 'KCR College', 'Hyderabad', 25, 'chandra@gmail.com'),
				    (107, 'Suma', 'MCom', 2008,66,'ANR Degree College', 'Chennai', 30, 'suma_mcom@gmail.com'),
				    (108, 'Rajesh', 'MTech', 2016,55, 'NTH College', 'Bangalore', 27, 'rajesh@yahoo.com'),
				    (109, 'Surya', 'MCA', 2018, 60, 'JNIT College', 'Bangalore', 26,'surya_py@gmail.com'),
				    (110, 'Ramya', 'MCA', 2010,99, 'NTH College','Hyderabad', 33, 'ramya@gmail.com')''')
connection.commit()
"""

import pymysql as pm
connection=pm.connect(host='localhost',user='root',password='nari',db='test')
c=connection.cursor()
c.execute('select * from students')
x=c.fetchall()


#1.wap to fetch student name who is is youngest person?
'''
l=[]
for i in x:
    l.append(i[7])
    m=min(l)
    if i[7]==m:
        print(i[1])
'''           
#2.wap to fetch student name who is is oldest person?
'''
l=[]
for i in x:
    l.append(i[7])
    m=max(l)
    if i[7]==m:
        print(i[1])
'''        
#3.wap to fetch student name whose mail id contains nth?
'''
for i in x:
    if 'nth' in i[8]:
        print(i[1])
'''
#4.wap to fetch student name whose mail id doesn't contains _?
'''
for i in x:
    if '_'not in i[8]:
        print(i[1])
'''        
#5.wap to fetch student name who is using yahoo mail account?
'''
for i in x:
    if 'yahoo' in i[8]:
        print(i[1])
'''        
#6.wap to fetch student name who is using gmail account?
'''
for i in x:
    if 'gmail' in i[8]:
        print(i[1])
'''
#7.what is the home town of students who has done BTech in 2020?
'''
for i in x:
    if i[2]=='BTech' and i[3]==2020:
        print(i[6])
'''        
#8.what is the age of student who has done BSc with 90 percentage?
'''
for i in x:
    if i[2]=='BSc' and i[4]==90:
        print(i[7])
'''
#9.how many students passedout in 2022?
'''
c=0
for i in x:
    if i[3]==2022:
        c=c+1
print(c)
'''
#10.how many students got more then 90 percentage?
'''
c=0
for i in x:
    if i[4]>90:
        c=c+1
print(c)        
'''
#11.what is the age of student who got less percentage in MCA?
'''
c=[]
for i in x:
    if i[2]=='MCA':
        c.append(i[4])
m=min(c)
for i in x:
    if i[4]==m:
        print(i[7])
'''
#12.what are the student name who are more then 30 years?
'''
for i in x:
    if i[7]>30:
        print(i[7])
'''
#13.what is the name of the college whose student name has more characters?
'''
c=[]
for i in x:
    c.append(len(i[5]))
    m=max(c)
for i in x:
    if len(i[5])==m:
        print(i[5])
'''
#14.wap to fetch students name who is senior of all students?
'''
c=[]
for i in x:
    c.append(i[3])
    m=min(c)
for i in x:
    if i[3]==m:
        print(i[1])    
'''
#15.wap to fetch students name who is done BTech with high percentage?
'''
c=[]
for i in x:
    if i[2]=='BTech':
        c.append(i[4])
m=max(c)
for i in x:
    if i[4]==m:
        print(i[1])
'''
#16.what is the qualification of ramya?
'''
for i in x:
    if i[1]=='Ramya':
        print(i[2])
'''
#17.how many students are done MTech?
'''
c=0
for i in x:
    if i[2]=='MTech':
        c=c+1
print(c)
'''
#18.how many students are not done BTech?
'''
c=0
for i in x:
    if i[2]!='BTech':
        c=c+1
print(c)
'''
#19.what is the college name who got high percentage?
'''
c=[]
for i in x:
    c.append(i[4])
m=max(c)
for i in x:
    if i[4]==m:
        print(i[5])
'''
#20.what is the percentage of MCA student who passedout_year is 2018?
'''
for i in x:
    if i[2]=='MCA' and i[3]==2018:
        print(i[4])
'''
#21.what is the gmail account of student who has done BSc from hyderabad?
'''
for i in x:
    if i[2]=='BSc' and i[6]=='Hyderabad':
        print(i[8])
'''
#22.what is the students names who are in mumbai?
'''
for i in x:
    if i[6]=='Mumbai':
        print(i[1])
'''
#23.how many students are there in nth college?
'''
c=0
for i in x:
    if i[5]=='NTH College':
        c=c+1
print(c)
'''
#24.what is the qualification of student whose passedout very recently?
'''
c=[]
for i in x:
    c.append(i[3])
m=max(c)
for i in x:
    if i[3]==m:
        print(i[2])
'''
#25.what is the percentage of student who studied in KCR College?
'''
for i in x:
    if i[5]=='KCR College':
         print(i[4])
''' 


