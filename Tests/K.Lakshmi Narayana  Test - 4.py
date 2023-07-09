# =============================== Set-1 =====================================
#print(open('employeedata.txt').readlines())
#1.Write a program to fetch all employees names
'''
import re
print(re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',open('employeedata.txt').read()))
'''
#2.Write a program to fetch all locations
'''
import re
print(re.findall('[A-Z]{0,}[a-z]{0,}[A-Z]{1,}[a-z]{1,} Location',open('employeedata.txt').read()))
'''
#3.Write a program to fetch all emilids
'''
import re
print(re.findall('[a-z]{1,}\.?[a-z]{1,}[0-9]{0,}\W[a-z]{1,}.com',open('employeedata.txt').read()))
'''
#4.Write a program to count number of NTH Company employess
'''
import re
print(len([re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',i) for i in open('employeedata.txt').readlines() if 'NTH Company' in i]))
'''
#5.Write a program to fetch all married female employees
'''
import re
print([re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',i) for i in open('employeedata.txt').readlines() if 'Female' in i ])
'''
#6.Write a program to display employees names who are using gmail accounts
'''
import re
print([re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',i) for i in open('employeedata.txt').readlines() if 'gmail' in i])
'''
#7.Write a program to display the company name of  Mr. Narayana
'''
import re
print([re.findall('[A-Z]{1,} Company',i) for i in open('employeedata.txt').readlines() if 'Mr. Narayana' in i])
'''
#8.Write a program to display the employee name who is working in INFOSYS Company
'''
import re
print([re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',i) for i in open('employeedata.txt').readlines() if 'INFOSYS Company' in i])
'''
#9.Write a program to display email id of Mrs. Renuka
'''
import re
print([re.findall('[a-z]{1,}\.?[a-z]{1,}[0-9]{0,}\W[a-z]{1,}.com',i) for i in open('employeedata.txt').readlines() if 'Mrs. Renuka' in i])
'''
#10.Write a program to display the employee name who born on 09-09-2002
'''
import re
print([re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',i) for i in open('employeedata.txt').readlines() if '09-09-2002' in i ])
'''
#11.Write a program to display youngest employee name
'''
import re
a = open('employeedata.txt').readlines()
l=[]
for i in a:
    l.append(re.findall('\d{2}\W\d{2}\W\d{4}',i))
print(l)
for i in a:
    if re.findall('\d{2}\W\d{2}\W\d{4}',i) == min(l):
        print(re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',i))
'''
#12.Write a program to display employee name who born after 2000 year
'''
import re
a = open('employeedata.txt').readlines()
for i in a:
    if re.findall('-\d{4}',i) > ['-2000']:
        print(re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',i))
'''
#13.Write a program to display all female employees name
'''
import re
print([re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',i) for i in open('employeedata.txt').readlines() if 'Female' in i ])
'''
#14.Write a program to display all employees names whose mobile number start with 9
'''
import re
m=re.findall('\d{10}',open('employeedata.txt').read())
n=re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',open('employeedata.txt').read())
d={}
for i,j in zip(n,m):
    d[i] = j
for i in d:
    if d[i][0] in '9':
        print(i)
'''
#15.Write a program to fetch all employees names
'''
import re
print(re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',open('employeedata.txt').read()))
'''
#16.Write a program to display the employee name who is working in Hello Company
'''
import re
print([re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',i) for i in open('employeedata.txt').readlines() if 'Hello Company' in i])
'''
#17.Write a program to display the employee gender who belongs to DramaPet Location
'''
import re 
print([re.findall('[A-Z]{1}[a-z]{3,4}',i) for i in open('employeedata.txt').readlines() if 'DramaPet Location' in i])
'''
#18.Write a program to display company name whose mail id contains java
'''
import re
print ( [re.findall('[A-Z]{1,}[a-z]{1,}[A-Z]{1,}',i) for i in open('employeedata.txt').readlines() if 'java' in i])
'''
#19.Write a program to display the count of total male employees
'''
import re    
print(len([re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',i) for i in open('employeedata.txt').readlines() if 'Male' in i ]))
'''
#20.Write a program to display all employees names whose mobile number start and end with 90
'''
import re
m=re.findall('\d{10}',open('employeedata.txt').read())
n=re.findall('[Mrs. ]{3,}[A-Z]{1}[a-z]{1,}',open('employeedata.txt').read())
d={}
for i,j in zip(n,m):
    d[i] = j
for i in d:
    if d[i][0] in '9' and d[i][1] in '0'and d[i][-2] in '9' and d[i][-1] in '0':
        print(i)

'''
#======================================= Set-3 ==============================================================
empdata='''Mr. Narayana,9010607010,10-03-1990,NTH Company,Hyderabad Location,Male,AP 12 XY 1234,CRRPP0660D, narayana_python@gmail.com
INFOSYS Company,Mr. Hari,9090909090,Bangalore Location,hari123@gmail.com,ABBD1212S,12-09-1990,AP 34MR 2321,Male
OD 89 BR 9887,18-05-1995,BDERF9890R,Female,renu.java@gmail.com,Chennai Location,9890989098,Mrs. Renuka,TagIT Company
ramu_python@gmail.com,Mumbai Location,9887988798,Mrs. Ramulamma,NTH Company,OIUYR7665D,20-10-1988, MR 23 HG 9887,Female
TS 98 GR 8745,10-03-2000,BNGTR4567D,Hello Company, Mr. Yatakaram,8776655443,Hyderabad Location,yatakarampeeks@gmail.com,Male
Mr. Durgarao,9876543210,09-09-2002,Male,Drama Company,DramaPet,AP 23 ER 4323,OKJHY7876D,dramarao@yahoo.com
'''

#1.wap to fetch all company names?
'''
import re
com=re.findall('[A-Za-z]{1,} [Company]',empdata)
print([i.replace('C','')for i in com])
'''
#2.wap to fetch all pan numbers?
'''
import re
pan=re.findall('[A-Z]{5}\d{4}[A-Z]',empdata)
print(pan)
'''
#3.wap to count total no.of female employees?
'''
c=0
x=open('empdata.txt').readlines()
for i in x:
    i.replace('\n',',').split(',')
    if 'Female' in i:
        c=c+1
print(c)        
'''
#4.wap to fetch all employees names whose vehicle belongs to AP?
'''
import re
x=empdata.split('\n')
for i in x:
    if re.findall('AP',i)==['AP']:
        print(re.findall('[Mrs. ]{4,5}[A-Z][a-z]{2,}',i))
'''                  
#5.wap to display an employee name who is using yahoo mail account?
'''
import re
x=empdata.split('\n')
for i in x:
    if re.findall('yahoo',i)==['yahoo']:
        print(re.match('[Mr. ]{4,5}[A-Z][a-z]{3,}',i))
l=[]
x=open('empdata.txt').readlines()
for i in x:
    if 'yahoo' in i:
        i.replace('/n',',').split(',')
        l.append(re.findall('[Mr. ]{4,5}[A-Z][a-z]{3,}',i))
        print(l)
'''
#6.wap to display employee name who is working in hello company?
'''
l=[]
import re
x=open('empdata.txt').readlines()
for i in x:
    if 'Hello' in i:
        i.replace('\n',',').split(',')
        l.append(re.findall('[Mr. ]{4,5}[A-Z][a-z]{3,}',i))
        print(l)
'''        
#7.wap to display working location of employee whose number is 9010607010?
'''
import re
x=open('empdata.txt').readlines()
for i in x:
    if '9010607010' in i:
        i.replace('\n',',').split(',')
        l=(re.findall('[A-Z][a-z]{2,} [Location]',i))
        print([i.replace('L','') for i in l])
'''        
#8.wap to display employee name whose date of birth is 12-09-1990?#
'''
import re
x=open('empdata.txt').readlines()
for i in x:
    if '12-09-1990' in i:
        i.replace('\n',',').split(',')
        l=(re.findall('[Mr. ]{4,5}[A-Z][a-z]{3,}',i))
        print(l)
'''
#9.wap to display the company name of Mr.Yatakaram?
'''
import re
x=open('empdata.txt').readlines()
for i in x:
    if 'Mr. Yatakaram' in i:
        i.replace('\n',',').split(',')
        l=(re.findall('[A-Z][a-z]{1,}\s[Company]',i))
        print([i.replace('C','') for i in l])
'''
#10.wap to display employee name who is working in NTH Company?
'''
import re
x=open('empdata.txt').readlines()
for i in x:
    if 'NTH Company' in i:
        i.replace('\n',',').split(',')
        l=(re.findall('[Mrs. ]{4,5}[A-Z][a-z]{3,}',i))
        print(l)
'''
#11.wap to display youngest employee?
'''
import re
x=open('empdata.txt').readlines()
l=min(re.findall('\d{2}-\d{2}-\d{4}',empdata))
for i in x:
    if re.findall('\d{2}-\d{2}-\d{4}',i)==[l]:
        print(re.findall('[Mrs. ]{4,5}[A-Z][a-z]{1,}',i))
'''
#12.wap to display to employee name who born after 2000 year?
'''
import re
x=open('empdata.txt').readlines()
for i in x:
    if re.findall('-\d{4}',i)>['-2000']:
        print(re.findall('[Mrs. ]{4,5}[A-Z][a-z]{1,}',i))
'''       
#13.wap to display all female ?
'''
import re
emp=re.findall('[Mrs.]{4}\s[A-Z][a-z]{3,}',empdata)
print(emp)
'''
#14.wap to display all employee names whose mobile number starts with 9?
'''
import re
x=open('empdata.txt').readlines()
for i in x:
    re.findall('[9]\d{9}',i)
    print(re.findall('[Mrs.]{3,4}\s[A-Z][a-z]{3,}',i))
'''
#15.wap to display all employees names?
'''
import re
emp=re.findall('[Mrs. ]{4,5}[A-Z][a-z]{3,}',empdata)
print(emp)
'''
#16.wap to display employee name who is working in NTH company?
'''
import re
x=open('empdata.txt').readlines()
for i in x:
    if 'NTH Company' in i:
        i.replace('\n',',').split(',')
        l=(re.findall('[Mrs. ]{4,5}[A-Z][a-z]{3,}',i))
        print(l)
'''
#17.wap to display employee gender who belongs to Hyderabad location?
'''     
import re
x=empdata.split('\n')
for i in x:
    if re.findall('[Hyderabad]{9}',i)==['Hyderabad']:
        print(re.findall('[A-Z][a-z]{0,}ale',i))        
'''
#18.wap to display company name whose mail id contains python?
'''
import re
x=open('empdata.txt').readlines()
for i in x:
    if 'python' in i:
        i.replace('\n',',').split(',')
        l=(re.findall('[A-Za-z]{1,} [Company]',i))
        print([i.replace('C','') for i in l])
'''        
#19.wap to display count female employees?
'''
import re
emp=re.findall('[Mrs. ]{5}[A-Z][a-z]{3,}',empdata)
print(len(emp))
'''
#20.wap to display employees names whose num is starts and ends with 90?#
'''
import re
x=open('empdata.txt').readlines()
for i in x:
    if re.fullmatch('[90]{2}\d{6}[90]{2}',i):
        print(re.findall('[Mr.]{3,4}\s[A-Z][a-z]{2,}',i))
'''

