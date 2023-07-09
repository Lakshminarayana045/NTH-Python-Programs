
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
'''

# 5.Write a program to update any one value
'''
d = {'name':'lucky','age':24,'loc':'ONG'}
d['name'] = 'narayana'
print(d)
'''

# 6.Write a python function to get first letter of each word of complete string given by user
"""
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
"""
# 7.Write a python function to reverse of each word in the string given by user
'''
def display():
    st='python narayana tech house hyderabad'
    s = st.split()
    l=[]
    for i in s:
        s=''
        l.append(i[-1::-1])
        s =' '.join(l)
    print('"'+s+'"')
display()
'''

# 8.Write a python function to write vowels in uppercase and consonnants in lowercase of same string given by user
'''
st='python narayana tech house HYDERABAD'
b=[]
for i in st:
    if i in 'aeiouAEIOU':
        b.append(i.upper())
    elif i not in 'aeiouAEIOU':
        b.append(i.lower())
print(''.join(b))
'''
# 9.Separate vowels and consonants
'''
def display():
    st = 'python narayana'
    a=''
    b=''
    for j in st:
        if j not in 'aeiou':
            a = a+j
        else:
            b = b+j
    print(b+a)
display()
'''

# 10.separate uppercase and lowercase
'''
def lucky():
    s = 'pyTHON NaRaYaNa'
    v=''
    c=''
    for i in s:
        if i.isupper():
            v = v+i
        else:
            c = c+i
    print(v+c)
lucky()
'''  

# 11.Write a function to count number of vowels and consonants from given string
'''
st = 'python narayana'
b=0
a=0
c=[]
for i in st:
    if i not in 'aeiou':
        b = b+1
    else:
        a = a+1
c.extend([a,b])
ls=['vowels Are:','consonat Are:']
d={}
for i in range(2):
    d[ls[i]]=c[i]
print(d)

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

# 13.
'''
st = 'Narayana'
a=st[-1::-1]
print(a)
'''
# 14.
'''
a = int(input('Enter any number: '))

if a%3 == 0 and a%5 == 0:
    print('HiBye')
elif a%3 == 0:
    print('Hi')
elif a%5 == 0:
    print("Bye")
else:
    print(a)
'''

# 15.WAP to count of words in the string.
#   more then 5  --> Lengthy String
#   below 5 --> Small String
'''
st = eval(input('enter any string: '))
if type(st) is str:
    if len(st) > 5:
        print('Lengthy String')
    else:
        print('Small String')
else:
    print('Enter string values ! ')
'''














'''


st = 'python narayana'
s = st.split()      #['python', 'narayana']
l=[]
for i in s:                         # i='python'  i='narayana'
    s1=''
    l.append(i[0].upper()+i[1:])
    s1=' '.join(l)
print("'" +s1+ '"')
print(s1)


'''

for i in range(10,1):
    print(i)







    
