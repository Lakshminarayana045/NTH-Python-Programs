a = '''Mr. Sai,9090909090,sai@gmail.com,AB 12 XY 1234,04/12/2000,TCS Company,ABCDE1234D
8789878987,Mr. Nani,BNBVG2345D,BN12MN2345,Wipro Company,nani123@gmail.com, 8/11/1999
Infosys Company,satya_i@gmail.com,OD 34 x 9876,31/01/1998,PERAN1245K,Mrs. Satya,9988998899
MNBFD1234R,rojan@gmail.com,TS23 AX 1234,1/1/1990,CTS Company,Mr. Rohan,8179817681
'''
# creating data into file format name is empdata
'''
l=open('empdata.txt','w')
l.write("Mr. Sai")
l.close()
'''
#1. Write a program to fetch all Employees names?
import re
a=open('empdata.txt').read()
'''
b=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',a)
print(b)
'''
#2. Write a program to fetch all mobile numbers from file?
'''b=re.findall('[8-9][0-9]{9}',a)
print(b)'''
#3. Write a program to fetch all PAN Numbers from file?
'''b=re.findall('[A-Z]{5}[0-9]{4}[A-Z]',a)
print(b)'''
#4. Write a program to fetch all email ids frmo file?
'''b=re.findall('[a-z]{1,}[_]*[a-z]*[0-9]*[@][a-z]{1,}[.][a-z]{1,}',a)
print(b)'''
#5. Write a program to fetch all registration numbers from file?
'''b=re.findall('[A-Z]{1,2}[ ]?[0-9]{1,2}[ ]?[a-zA-Z]{1,2}[ ]?[0-9]{1,4}',a)
print(b)'''
#6. Write a program to fetch all company names?
'''b=re.findall('[A-Z]{1,} Company',a)
print(b)'''
#7. Write a program to fetch all date of births?
'''b=re.findall('[0-9]{1,}[/.][0-9]{1,}[/.][0-9]{1,}',a)
print(b)'''
#8. Write a program to fetch company name Mr. Sai?
'''a=open('empdata.txt').readlines()
for i in a:
    if 'Mr.Sai' in i:
        x=re.findall('[A-Z]{3}[ ]?[A-Z]{1}[a-z]{1,}',i)
        print(x)'''
#9. Write a program to fetch email id of Mr. Rohan?
'''for i in a:
    if 'Mr.Rohan' in i:
        x=re.findall('[a-z]{1,}[_]*[a-z]*[0-9]*[@][a-z]{1,}[.][a-z]{1,}',i)
        print(x)'''
#10. Write a program to fetch employee name who is using 9090909090?
'''for i in a:
    if '9090909090' in i:
        x=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',i)
        print(x)'''
#11. Write a program to fetch PAN number of Mr. Satya?
'''for i in a:
      if 'Mrs.Satya' in i:
        x=re.findall('[A-Z]{5}[0-9]{4}[A-Z]{1,}',i)
        print(x)'''
#12. Write a program to fetch contact number of both Nani and Satya?
'''for i in a:
    if 'Mrs.Satya' in i or 'Mr.Nani' in i:
        x=re.findall('[6-9]{1}[0-9]{9}',i)
        print(x)'''
#13. Write a program to fetch emp names of Infosys and TCS companies?
'''for i in a:
    if 'Infosys Company' in i or 'TCS Company' in i:
        x=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',i)
        print(x)'''
#14. Write a program to fetch DOB of TCS Employee?
'''for i in a:
    if 'TCS Company' in i:
        x=re.findall('[0-9]{1,}[/.][0-9]{1,}[/.][0-9]{1,}',i)
        print(x)'''
#15. Write a program to fetch birth year of Mr. Nani?
'''for i in a:
    if 'Mr.Nani' in i:
        b=re.findall('[/][0-9]{4}',i)
for i in b:
    print(i.replace('/',''))'''
#16. Write a p rogram to fetch the emp name whose mobile number starts with 8?
'''for i in a:
    if i.startswith('8'):
        b=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',i)
        print(b)'''
#17. Write a program to fetch odisha emp name?
'''for i in a:
    if 'OD 34 x 9876' in i:
        x=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',i)
        print(x)'''
#18. Write a program to fetch youngest employee name?
'''b=re.findall('[0-9]{1,}[/.][0-9]{1,}[/.][0-9]{1,}',a)
for i in b:
    if min(b) in i:
        print(i)
for j in a:
    if j in i:
        x=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',j)
print(x)'''
#19. Write a program to fetch all Male Employees?
'''for i in a:
    if 'Mr.' in i:
        b=re.findall('[A-Z]{1}[a-z]{1}[.][A-Z]{1}[a-z]{1,}',i)
        print(b)'''
#20. Write a program to fetch total count of female employees?
'''for i in a:
    if 'Mrs.' in i:
        b=re.findall('[A-Z]{1}[a-z]{2}[.][A-Z]{1}[a-z]{1,}',i)
print(len(b))'''
#21. Write a program to fetch all employees names who born in January?
'''for i in a:
    if '/1/' in i or '/01/' in i:
        b=re.findall('[A-Z]{1}[a-z]{1,}[.][A-Z]{1}[a-z]{1,}',i)
        print(b)'''
#22. Write a program to fetch contact number of Telangana Employee?
'''for i in a:
    if 'TS23 AX 1234' in i:
        x=re.findall('[6-9]{1}[0-9]{9}',i)
        print(x)'''
#23. Write a program to fetch Company Name and Mobile Number of Wipro Employee?
'''for i in a:
    if 'Wipro' in i:
        b=re.findall('[A-Z]{1,}[a-z]*[ ]?[A-Z]{1,}[a-z]{1,}',i)
        c=re.findall('[6-9]{1}[0-9]{9}',i)
        print(b+c)'''

#24. Write a program to fetch Emp name who born in leaf year?
#25. Write a program to fetch all details of emp whose name not ends with vowel?
'''
for i in a:

    if i[-1] not in'aeiouAEIOU':
    
        b=re.findall('[A-Z]{1}[a-z]{1,2}[.][A-Z]{1}[a-z]{1,}',i)
        print(b)
'''
data = '''Mr. Narayana Trainer is teaching Python Language
since 5 years in both online mode and offline mode,
He also teaches Java Language very rarely.
Python course fee 3000Rs and Java course fee 2000Rs.
Mr. Roshan Trainer is also teaching SAP Course and MSBI Course.
'''
#1. Write a program to fetch Trainers Names?
'''import re
m=re.findall('[A-Z][a-z][.][ ][A-Z][a-z]{1,} Trainer',data)
print(m)'''
#2. Whats are the languages that Mr. Narayana teach?
'''import re
m=re.findall('[A-Z][a-z]{1,} Language',data)
print(m)'''
#3. What are the mode that Mr Narayana teach?
'''import re
m=re.findall('[a-z]{1,} mode',data)
print(m)'''
#4. What are the fee structures of both Python and Java?
'''import re
m=re.findall('[0-9]{1,}[A-Z][a-z]',data)
print(m)'''
#5. What are the courses that Mr. Roshan teach?
'''import re
m=re.findall('[A-Z]{1,} Course',data)
print(m)'''

