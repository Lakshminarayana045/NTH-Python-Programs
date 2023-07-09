#============================================= set-1   =====================================================


# 1.Write a program to fetch all odd elements into one list & even elements into another list
'''
lst=[10,20,30,40,50,60,70,80,90,100,15,7,79]
even=[]
odd=[]
for i in lst:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
'''
# 2.Write a program to fetch all words which has more then 5 characters
'''
name=['lucky','chandu','siddaiah','narayana','sai']
lst=[]
for i in name:
    if len(i) > 5:
        lst.append(i)
print(lst)
'''
# 3.Write a program to fetch all numbers which are divisible by 3 and 5
'''
lst=[5,9,15,20,25,30,35,40]
lucky=[]
for i in lst:
    if i%3 == 0 and i%5 == 0:
        lucky.append(i)
print(lucky)
'''
# 4.Take one dict with 3 pairs, Write a program to add new pair into that existing dict
'''
d = {'name':'lucky','age':24,'loc':'ONG'}
d['sal']=30000
print(d)
            # or
d = {'name':'lucky','age':24,'loc':'ONG'}
d2 ={'salary':30000}
d.update(d2)
print(d)
'''
# 5.Write a program to update any one value
'''
d = {'name':'lucky','age':24,'loc':'ONG'}
d['name'] = 'Lakshmi Narayana'
print(d)
'''

# 6.Write a function called hi_bye() that takes a number given by user.
#   -If the number is divisible by 3, it should return "Hi".
#   -If it is divisible by 5, it should return "Bye".
#   -If it is divisible by both 3 and 5, it should return "HiBye". -Otherwise, it should return the same number
'''
def Hi_Bye(a):
    if a%3 == 0 and a%5 == 0:
        print('HiBye')
    elif a%3 == 0:
        print('Hi')
    elif a%5 == 0:
        print("Bye")
    else:
        print('{}'.format(a))
Hi_Bye(int(input('Enter any number: ')))
'''
# 7.Write a program to insert * in place of every vowels in the string.
'''
st='Python Narayana Tech House'
l=''
for i in st:
    if i in 'aeiou':
        l = l+'*'
    else:
        l = l+i
print(l)
''' 

# 8.Take lengthy string and count total number consonants in dict format
'''
st = eval(input('enter any string : '))
d={}
l = []
for i in st:
    if i not in 'aeiou' and i != ' ':
        l.append(i)
        d[i] = st.count(i)
print(d)
'''
# 9.Take lengthy string and count number of spaces { with using count() }
'''
st='Python Narayana Tech House'
c=0
for i in st:
    if i == ' ':
        c = c+1
print(c)
'''

# 10.Write A Python function to get first letter of each word of complete string given by user?
#   Note: Do not use pre-defined functions Eg:
#   input: "python narayana tech house".
#   output: "Python Narayana Tech House"
'''
def dis(a):
    s=''
    l=[]
    for i in a.split():
        l.append(i[0].upper()+i[1:])
    print(' '.join(l))

    
dis(eval(input('Enter any string: ')))
'''
emps = {

'emp1':{'name':'Rajesh','salaries':{'TCS':30000,'Wipro' :40000,'Infosys':55000},'age':25,"location":'Hyderabad'},
'emp2':{'name':'Kumar','salaries':{'CTS': 40000,'NTH':60000,'Infosys':90000},"age":35,'location':'Hyderabad'},
'emp3':{'name':'Satya','salaries':{'DeepCompute':20000,'Wipro':40000,'Infosys':50000},'age':22,'location':'Bangalore'},
'emp4':{'name':'Saroj','salaries':{'AXA':30000,'Infosys':40000,'Ignify':60000,'Atos':65000},
        'age':30,'location':'Chennal'},}
        
# 11.Write a program to fetch all employees names who is working in Hyderabad?
'''
for i in emps:
    if emps[i]['location'] == 'Hyderabad':
        print(emps[i]['name'])
        
'''
# 12.Write a program to fetch all employees who age is more then 30 years?

'''
for i in emps:
    if emps[i]['age'] > 30:
        print(emps[i]['name'])
    
'''

# 13.Write a program to fetch all employees names who is working in Infosys?
'''
for i in emps:
    if 'Infosys' in emps[i]['salaries']:
        print(emps[i]['name'])
'''
# 14.Write a program to count total number of employees in Infosys?
'''
c=0
for i in emps:
    if 'Infosys' in emps[i]['salaries']:
        c=c+1
print(c)
'''

# 15.Write a program to count total number of employees working in Bangalore?
'''
c=0
for i in emps:
    if 'Bangalore' in emps[i]['location']:
        c=c+1
print(c)
'''
# 16.Write a program to display employee name who is working in NTH company?
'''
for i in emps:
    if 'NTH' in emps[i]['salaries']:
        print(emps[i]['name'])
'''

# 17.Write a program to update the salary of Saroj in Axa company to 35000?
'''
for i in emps:
    if emps[i]['name'] == 'Saroj':
        emps[i]['salaries']['AXA'] = 35000
print(emps[i]['salaries']['AXA'])
        
'''
# 18.Write a program to display all employees names who is working in more then 3 companies?
'''
for i in emps:
    if len(emps[i]['salaries']) > 3:
        print(emps[i]['name'])
'''


#======================================  set-2 ====================================================

# 1.Write a program to fetch all odd elements into one list & even elements into another list

lst=[10,20,30,40,50,60,70,80,90,100,15,7,79]
'''
even=[]
odd=[]
for i in lst:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
'''
# 2.Write a program to fetch all words which has more then 5 characters
'''
name=['lucky','chandu','siddaiah','narayana','sai']
lst=[]
for i in name:
    if len(i) > 5:
        lst.append(i)
print(lst)
'''
# 3.Write a program to fetch all numbers which are divisible by 3 and 5
'''
lst=[5,9,15,20,25,30,35,40]
lucky=[]
for i in lst:
    if i%3 == 0 and i%5 == 0:
        lucky.append(i)
print(lucky)
'''
# 4.Take one dict with 3 pairs, Write a program to add new pair into that existing dict
'''
d = {'name':'lucky','age':24,'loc':'ONG'}
d['sal']=30000
print(d)
            # or
d = {'name':'lucky','age':24,'loc':'ONG'}
d2 ={'salary':30000}
d.update(d2)
print(d)
'''
# 5.Write a program to update any one value
'''
d = {'name':'lucky','age':24,'loc':'ONG'}
d['name'] = 'Lakshmi Narayana'
print(d)
'''

# 6.Write a python function to get first letter of each word of complete string given by user
'''
st = eval(input('enter a string: '))
def display(st):
    s = st.split()
    l=[]
    for i in s:
        s1=''
        l.append(i[0].upper()+i[1:])
        s1=' '.join(l)
    print('"' +s1+ '"')
display(st)
'''
# 7.Write a python function to reverse of each word in the string given by user
'''
st = eval(input('enter a string: '))
def display():
    s = st.split()
    l=[]
    for i in s:
        sn=''
        l.append(i[-1::-1])
        sn =' '.join(l)
    print('"'+sn+'"')
display()
'''
# 8.Write a python function to write vowels in uppercase and consonnants in lowercase of same string given by

'''st = eval(input('enter a string: '))
def display():
    b=[]
    for i in st:
        if i in 'aeiouAEIUO':
            b.append(i.upper())
        else:
            b.append(i.lower())
    print(''.join(b))
display()'''


# 9.Write a python function to Separate vowels and consonants from given string
'''
st = 'python narayana'
def display():
    c=''
    v=''
    for j in st:
        if j not in 'aeiou':
            c = c+j
        else:
            v = v+j
    print("'"+(v+c)+"'")
display()
'''
# 10.Write a python function to separate upper case and lower case characters from given string
'''
st = 'pyTHON NaRaYaNa'
def lucky():
    u=''
    l=''
    for i in st:
        if i.isupper():
            u = u+i
        else:
            l = l+i
    print(u+l)
lucky()
'''
# 11.Write a function to count number of vowels and consonants from given string
'''
st = 'python narayana'
def vc():
    v=0
    c=0
    for i in st:
        if i not in 'aeiou':
            c = c+1
        else:
            v = v+1
    print('vowels Are:',v)
    print('Consonants Are:',c)
vc()
'''
# 12.Write python function to  remove all vowels from given string
'''
st = 'Narayana'
def display():
    a=''
    for j in st:
        if j not in 'aeiou':
            a = a+j
    print(a)
display()
'''
# 13.Write a python to reverse half string
'''
s = 'Narayana'
def display():
    r=len(s)//2
    x=s[0:r]
    y=s[r:]
    print(y+x)
display()
'''
# 14. Write a function called hi_bye() that takes a number given by user.
#    If the number is divisible by 3, it should return "Hi".
#    If it is divisible by 5, it should return "Bye".
#    If it is divisible by both 3 and 5, it should return "HiBye".
#    Otherwise, it should return the same number.
'''
def Hi_Bye(a):
    if a%3 == 0 and a%5 == 0:
        print('HiBye')
    elif a%3 == 0:
        print('Hi')
    elif a%5 == 0:
        print("Bye")
    else:
        print('{}'.format(a))
Hi_Bye(int(input('Enter any number: ')))
'''
# 15. WAP to count number of words in the string.
#   if number of words more then 5 then display "Lengthy String" otherwise "Small String".
'''
st = eval(input('enter any string: '))
if len(st) > 5:
    print('Lengthy String')
else:
    print('Small String')
'''


#============================================   set 3   ==========================================================================

# 1. Write A Python function to get first letter of each word of complete string given by user?
'''
def word(a):
    lst=[]
    for i in a.split():
        lst.append(i[0].upper()+i[1:])
    print(' '.join(lst))
word(eval(input('Enter any string: ')))

'''
# 2. Write a Python Function to reverse of each word in the string given by user?
'''
def reverse(s):
    ls=[]
    for i in s.split():
        ls.append(i[-1::-1])
    print(' '.join(ls))
reverse(eval(input('Enter any string: ')))       
'''
# 3. Write A Python Function to write vowels in uppercase and consonants in lowercase of same string given by user?
'''
def sam(a):
    ul=[]
    for i in a:
        if i in 'aeiou':
            ul.append(i.upper())
        else:
            ul.append(i.lower())
    print(''.join(ul))
sam(eval(input('Enter any string: '))) 
'''
# 4. Write a Python Function to seperate vowels and consonants from given string
'''
def sep(a):
    v=[]
    c=[]
    for i in a:
        if i in 'aeiou':
            v.append(i)
        else:
            c.append(i)
    print(''.join(v+c))
sep(eval(input('Enter any string: '))) 
    
'''
# 5. Write a Python Function to seperate upper case and lower case characters from given string#
#input: 'pyTHON NaRaYaNa'
#output: THONNRYNpy aaaa
'''
def sep(s):
    u=''
    l=''
    for i in s:
        if i.isupper():
            u = u+i
        else:
            l = l+i
    print(u+l)  
sep(eval(input('Enter any string: '))) 
'''
# 6. Write a Python Function to count number of vowels and consonants from given string.
'''
def count(s):
    v=0
    c=0
    for i in s:
        if i in 'aeiou':
            v=v+1
        else:
            c=c+1
    print('Vowels Are: ',v)
    print('Consonants Are: ',c)
count(eval(input('Enter any string: ')))


'''
# 7. Write a Python Function to find the highest number of list elements?
# lst = [10,45,30,67,23,43]   Note: Dont use max()or reduce().
'''
def l():
    lst = [10,45,30,67,23,43]
    for i in lst:
        if i == max(lst):
            print(i)
l()
lst = [10,45,30,67,23,43]
l1 = 0
for i in lst:
    if i > l1:
        l1 = i
print(l1)
'''

# 8. Write Python Function to seperate only integer type values into new list from given list?
'''
lst = [10,'NTH', True, 11, 'Python', False, 12] 
def dis():
    ls=[]
    for i in lst:
        if type(i) == int:
            ls.append(i)
    print(ls)
dis()
'''
# 9. Write Python Function to find index of specific element in the list?
# Eg:Enter Any Element: 150     150 is available in 3rd index position.
'''
lst = [100,200,300,150,'NTH','Python']
def indi(lst):
    n = eval(input("Enter any element: "))
    c = lst.index(n)
    d={}
    d[n]=c
    print(d)
    print("{} is available in {} index position.".format(n,c))         
indi([100,200,300,150,'NTH','Python'])
'''
# 10. Write Python Function to Find The Abbreviation form of given string?
# Enter Any String: 'NARAYANA Tech House'                                 Abbreviation Form is NTH.
# Enter Any String: Integrated Development Learning Environment.          Abbreviation Form is IDLE.
'''
def ab():
    st = input('Enter a string: ')
    l =''
    for i in st.split():
        l=l+(i[0].upper())
    print(l)
ab()
'''
                # or
'''                
s = 'Integrated Development Learning Environment'
s1 = s.split()
l = ''
for i in s1:
    l = l+i[0]
print("Abbreviation Form is: {}".format(l))
'''

# 11. Write Python Program To find the highest number of three given numbers?
'''
a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c = int(input('Enter third number: '))
if a > b and a > c:
    print('Hightest number is',a)
elif b > c and b > a:
    print('Hightest number is',b)
elif c > a and c > b:
    print('Hightest number is:',c)
else:
    print('Are all Same Values')
'''

# 12. Write Python Program to read a string from user. Count total number of vowels and consonants in the string.
# If more vowels are there then display "Vowels Dominated String."
# If more consonants are there then display "Consonants Dominated String."
# If Equal number of Vowels and Consonants are then raise error "EqualVowelsConsonantsError".
'''
class EqualVowelsConsonantsError(Exception):
    pass
n = input("Enter some string(without space): ")
v = 0
c = 0
for i in n:
    if i in 'aeiou':
        v = v+1
    else:
        c = c+1
if c > v:
    print('Consonants Dominated String')
elif v > c:
    print("Vowels Dominated String.")
else:
    raise EqualVowelsConsonantsError("Values are equal")
'''

# 13.Write Python Function to read string from user and display the next character of every character in the given string.
# Enter Any String:a            The Result String: b
# Enter Any String: Narayana    The Result String: Obsbzbob

'''
n = input("enter the string: ")
b = 'abcdefghijklmnopqrstuvwxyzABCDEFHIJKLMNOPQRSTUVWXYZ'
d = []
for i in n:
    if i in b:
        c = b.index(i)
        d.append(b[c+1])
print(''.join(d))        
'''
