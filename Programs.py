# make a patterns
'''
a = '*'
for i in range(1,10):  # number choice
    print(a*i)
'''
# number
'''
a = eval(input('enter any number 1: '))
b = eval(input('enter any number 2: '))
c = eval(input('enter any number 3: '))
'''
'''
if type(a) == int and type(b) == int and type(c) == int:
    if a > b:
        print('{} is greaterthen {}'.format(c,a))
    if a > c:
        print('{} is greaterthen {}'.format(c,b))
    else:
        print('{} is not greaterthen {}'.format(a,b))
        print('{} is not greaterthen {}'.format(a,c))
else:
    print('Enter 3 Values Interger Only')

'''
        # or
'''
a = eval(input('enter any number 1: '))
b = eval(input('enter any number 2: '))
c = eval(input('enter any number 3: '))

if type(a) and type(b) and type(c) is int:
    if a > b and a > c:
        print(a,'Greaterthen' ,b,c)
        if b > c:
            print(b,'second highest')
            print(c,'third highest')
        else:
            print(c,'second highest')
            print(b,'third highest')
    elif b > a and b > c:
        print(b,'Greaterthen' ,a,c)
        if a > c:
            print(a,'second highest')
            print(c,'third highest')
        else:
            print(c,'second highest')
            print(a,'third highest')
    elif c > a and c > b:
        print(c,'Greaterthen',a,b)
        if a > b:
            print(a,'second highest')
            print(b,'third highest')
        else:
            print(b,'second highest')
            print(a,'third highest')
    else:
        print('all are same')
else:
    print('enter interger values')
'''
# Registration

'''
users_databases = { 'sai':'sai@1234','nani':'nani@1234' }
while True:
    user = input('Enter your name: ')
    if user in users_databases:
        print(" It's already existed name ")
        continue
    else:
        pwd = input('Enter  your password ')
    users_databases[user] = pwd
    print(users_databases)
    break
'''

        # Login
'''

while True:
    user = input('Enter your user name: ')
    if user not in users_databases:
        print('User name is not found ')
        continue
    else:
        while True:
            pwd = input('enter your password:')
            if pwd != users_databases [user]:
                print('Invalid password')
                continue
            else:
                print('Login success')
            break
    break

'''
# Given gears check your car speed
'''
g = eval(input('enter which gear you drive: '))
gear = ['n',1,2,3,4,5,6,'r']

if g in gear:
    if g =='n' :
        print('your car in neutral')
    elif g == 1:
        print('your car in 20 speed')
    elif g is 2:
        print('your car in 40 speed')
    elif g is 3:
        print('your car in 60 speed')
    elif g is 4:
        print('your car in 80 speed')
    elif g is 5:
        print('your car in 120 speed')
    elif g is 6:
        print('your car in 150 speed')
    else:
        print('your car moving on reverse')
else:
    print('enter correct gear number')

'''

'''
money=[4000,4500,5000]
m=eval(input('Enter your Hostel Fee :  '))

if m in money :
    if m == 5000:
        print('hello')
    elif m == 4500:
        print('lahari')
    else:
        print('this hostels are very high')
elif m < 4000:
    print('hostel are not avalible')
else:
    print( 'this money  very high')
'''


'''
ls=eval(input('enter number:   '))
if type(ls) is int:
    if ls > 0:
        print(ls, 'positive number')
        if ls%2 == 0:
            print( ls ,'P even numbers')
        else:
            print( ls, 'P Odd number')
    elif ls < 0:
        print( ls ,'negative number')
        if ls%2 == 1:
            print( ls, 'N odd numbers')
        else:
            print(ls, 'N even number')
    else:
        print(' your enter ZERO')
else:
    print('only number')
'''

                # Python programs
# count any number
'''
n = 23245
count = 0
while(n>0):
    count = count+1
    n = n/10
    print(count)
'''
# Dates
'''
import data,timedelta

today = date.today()
dates = [(today - timedelta(days=i)).strftime("%d-%m-%y")
         for i in range(10)]
print(dates)
'''
#Palindrom
"""
st=['mom','python','malayalam','madam']
ls=[]
for i in st:
    if i==i[-1::-1]:
        ls.append(i)
mf=[]
for j in ls:
    ls1=[]
    for k in j :
        if k in "aeiou":
            ls1.append(k)
    s=''.join(ls1)
    mf.append(s)
print(mf)

st=['mom','python','malayalam','madam']
luc=[]
for i in st:
    b=''
    if i==i[-1::-1]:
        for c in i:
            if c in [a for a in 'aeiou']:
                b = b+c
        luc.append(b)
print(luc)


st='python narayana tech house'
v='aeiou'
d={}.fromkeys(v,0)
for i in st:
    if i in d:
        d[i] = d[i]+1
print(d)
"""

#1.Write a python program to fetch all even numbers           
'''
ls=[10,9,20,15,14,13,18,20,45,40,81,56]
s=[]
for l in ls:
    if l%2 == 0:
        s.append(l)
print(s)
'''
#2.Write a python program to fetch all 5 divisbles from given list
"""
ls=[10,9,20,15,14,13,18,20,45,40,81,56]
e=[]
for i in ls:
    if i%5 == 0:
        e.append(i)
print(e)
"""    
#3.Write a python program to fetch all int values from given list
'''
lt=[10,9,20,15,14,13.4598,18,20,45,40,81.25,56,14.48,148952.8544,1789832.5484,52858]
s=[]
for i in lt:
    if type(i) == int:
        s.append(i)
print(s)
'''
#4.Write a python program to fetch all non-int values from list
'''
venky=[10,9,20,15,14,13.4598,18,20,45,40,81.25,56,14.48,148952.8544,1789832.5484,52858]
k=[]
for lucky in venky:
    if type(lucky) is float: # != int
        k.append(lucky)
print(k)
'''
#5.Write a python program to fetch all words which contain only four characters
'''
lst=['nani','dhoni','ring','lap','clap']
s=[]
for i in lst:
    if len(i) == 4:
        s.append(i)
print(s)
'''
#6.Write a python program to fetch all words which startswith 'n' characters
'''
lt=['nani','dhoni','nepal','bhupal']
sri=[]
for i in lt:
    if i.startswith('n'): #i[0]=='n'
        sri.append(i)
print(sri)
'''
#7.Write a python program to fetch all words which endsswith 'i' characters       
'''
names=['nani','dhoni','rohan','kohil','sachin']
ls=[]
for l in names:
    if l[-1] == 'i':
        ls.append(l)
print(ls)
'''
#8.Write a python program to fetch all words which contins either 4 or 6 characters
'''
st ='python is simple and easy language'
s=st.split()
lst=[]
for i in s:
    if len(i)==4 or len(i)==6: # len(i) in [4,6]
        lst.append(i)
print(lst)
'''
#9.Write a python program to fetch all words which startswith vowel
'''
st =('python is simple and easy language').lower()
m=st.split()
ls=[]
for i in m:
    if i[0] in 'aeiou':
        ls.append(i)
print(ls)
'''
#10.Write a python program to fetch all words which starts with vowel and ends with consonats
'''
st =('python is simple and easy language').lower()
k=st.split()
l=[]
for i in k:
    if i[0] in 'aeiou' and i[-1] not in 'aeiou':
        l.append(i)
print(l)
'''

#11.Write a python program to fetch all words which contain 'a' character
                # lst = ['sai','rohan','dhoni','kohli','django']
'''               
lst = ['sai','rohan','dhoni','kohli','django']
ls=[]
for i in lst:
    if 'a' in i: 
        ls.append(i)
print(ls)
'''
#12.Write a python program to fetch all words which has even number of characters            
           # lst = ['sai','nani','dhoni','siva','django']
'''           
lst = ['sai','nani','dhoni','siva','django']
k=[]
for i in lst:
    if len(i)%2 == 0:
        k.append(i)
print(k)
'''
#13.Write a python program to fetch all names which has two or more words
            # lst = ['python sai','nani mysql','dhoni','siva','django lucky']
'''
lst = ['python sai','nani mysql','dhoni','siva','django lucky']
s=[]
for i in lst:
    if ' ' in i:
        s.append(i)
print(s)
'''       

            
#14.Write a python program to reverse all word in list
        # # lst = ['sai','rohan','dhoni','kohli','django']
'''        
lt=['sai','rohan','dhoni','kohli','django']
l=[]
for i in lt:
    l.append(i[-1::-1])
print(l)
'''     

#15.Write a python program to fetch all words except first and last character from each word
        # name = ['python','django','flask']
'''
name = ['python','django','flask']
lst=[]
for i in name:
    lst.append(i[1:-1])
print(lst)
'''
#16.Write a python program to count number of character in the given string { with out use len() }
'''
s='narayana tech house'
lucky=0
for i in s:
    lucky=lucky+1
print(lucky)
'''
#17.Write a python program to count number of characters{with out space} in the given string
'''
st='narayana tech house'
count=0
for i in st:
    if i == ' ':    # i != '':
        continue
    count=count+1
print(count)
'''
#18.Write a python program to count number of spaces in the given string
"""
st='python is simple and easy language'
s=0
for i in st:
    if i==' ':
        s=s+1
print(s)
"""
#19.Write a python program to count total number of words in the given string
"""
st='python is simple and easy language'
s=st.split()
a=0
for i in s:
    a=a+1
print(a)
"""
#20.Write a python program to count total number of characters in each word in the given string
'''
s='python is simple and easy language'
sr=s.split()
ls=[]
for i in sr:
    ls.append(len(i))
print(ls)
'''
        # or
'''
s='python is simple and easy language'
sr=s.split()
ls=[]
for i in sr:
    count=0
    for j in i:
        count=count+1
    ls.append(count)
print(ls)
'''
#21.Write a python program to count total number of vowels in string
'''
st=('Konanki Lakshmi Narayana').lower()
N = 0
for j in st:
    if j in 'aeiou':
        N=N+1
print(N)
'''
#22.Write a python program to count total number of characters of thr word which contains 'i' characters
'''
s='python is simple and easy language'
st=s.split()
ls=[]
for lucky in st:
    if 'i' in lucky:
        ls.append(len(lucky))
print(ls)
'''
#23.Write a python program to get all words which has more then 5 charscters
'''
s='python is simple and easy language'
st=s.split()
l=[]
for i in st:
    if len(i) > 5:
        l.append(i)
print(l)
'''
#24.Write a python program to fetch all palindrome words
'''
ls=['mom','madam','dad','malayalam','lucky','venky','sri']
em=[]
for i in ls:
    if i == i[-1::-1]:
        em.append(i)
print(em)
'''
#25.Write a python program to fetch all non-palindrome words
'''
ls=['mom','madam','dad','malayalam','lucky','venky','sri']
em=[]
for i in ls:
    if i != i[-1::-1]:
        em.append(i)
print(em)
'''
#26.Write a python program to fetch all words which don't have atlast one vowel
'''
lst=['sky','python','django','mysql','sai']
s=[]
ks=['a','e','i','o','u']
for i in lst:
    a=0
    for j in i:
        if j in ks:
            a=1
    if a==0:
        s.append(i)
print(s)
'''
#27.Write a python program to fetch  all words vowels and must containts only 4 character
'''
lst=['anil','animations','only','django','ice']
sl=[]
for i in lst:
    if i[0] in 'aeiou' and len(i) == 4:
        sl.append(i)
print(sl)
'''
#28.Write a python program to inter-change words
'''
ls=['venky','lucky','sri','revi']
lst=ls[-1::-1]
print(lst)
'''
#29.Write a python program to fetch all words with out vowels in the word
'''
ls=['venky','lucky','sri','revi']
l=[]
for i in ls:
    a=''
    for j in i:
        if j not in 'aeiou':
            a=a+j
    l.append(a)
print(l)
'''

ply={'sachin':35,'kohil':27,'rohit':30,'surya':25}

#30.1 who is youngest player
'''
lst=[]       
for name,age in ply.items():
    lst.append(age)
print(min(lst))

for i in ply:
    lst.append(ply[i])
print(min(lst))
'''
#30.2 who is oldest player
'''
lst=[]       
for name,age in ply.items():
    lst.append(age)
print(max(lst))

for i in ply:
    lst.append(ply[i])
print(max(lst))
'''
#30.3 what is the age of kohil
'''
for name,age in ply.items():
    if name=='kohil':
        print(age)

for i in ply:
    if i == 'kohil':
        print(ply[i])
'''        
#30.4 display the names whose age above 30 years
'''
for name,age in ply.items():
    if age > 30:
        print(name)

for i in ply:
    if ply[i] > 30:
        print(i)
'''        
#30.5 display the age of plyears whose name starts with 's'
'''
for name,age in ply.items():
    if name.startswith('s'):
        print(name)

for i in ply:
    if i[0] == 's':
        print(i)
'''

names=['mom','language','malayalam','python','madam','dad']

#31.1 Write a python program to fetch the biggest palindrom word
'''
p=[]
l=[]
for i in names:
    if i ==i[-1::-1]:
        p.append(i)
        l.append(len(i))
for j in p:
    if len(j) == max(l):
        print(j)
'''
#31.2 Write a python program to fetch the smallest palindrom word
'''
p=[]
l=[]
for i in names:
    if i == i[-1::-1]:
        p.append(i)
        l.append(len(i))
for j in p:
    if len(j) == min(l):
        print(j)
'''
#31.3 Write a python program to fetch the palindrom word which contains only 5 characters
'''
for i in names:
    if i == i[-1::-1] and len(i) == 5:
        print(i)
'''
#31.4 Write a python program to fetch the smallest non-palindrom word
'''
p=[]
l=[]
for i in names:
    if i != i[-1::-1]:
        p.append(i)
        l.append(len(i))
for j in p:
    if len(j) == min(l):
        print(j)
'''
#31.5 Write a python program to fetch the non-palindrom word which contains 'a' character
'''
for i in names:
    if i != i[-1::-1] and 'a' in i:
        print(i)
'''
#31.6 Write a python program to fetch the all palindrom word which starts with 'm' character
'''
ls=[]
for i in names:
    if i == i[-1::-1] and i[0] == 'm':
        ls.append(i)
print(ls)
'''
#31.7 Write a python program to fetch the all palindrom word which has more two 'a' character
'''
for i in names:
    if i==i[-1::-1] and i.count('a') == 2:
        print(i)
'''
#31.8 Write a python program to fetch the both palindrom and non-palindrom word which has 'l' character
'''
ls=[]
for i in names:
    if 'l' in i:
        ls.append(i)
print(ls)
'''
#31.9 Write a python program to fetch all palindrom word which has even numbers of character
'''
l=[]
for i in names:
    if i == i[-1::-1] and len(i)%2 ==1:
        l.append(i)
print(l)
'''
# write a python program to count no.of occurences of each character in the string
"""
s='Lakshmi narayana'
d={}.fromkeys(s,0)
for i in s:
    #if i in d:
    d[i]=d[i]+1
print(d)
"""
# write a python program to find the lenght of string (excluding space)
"""
s='Konanki Venkat Lakshmi Narayana'
sa=0
for i in s:
    if i != '  ':
        sa=sa+1
print(sa)
"""
# write a program to palindrom word and its length ?
'''
p = eval(input('enter any word: '))
d={}
if type(p) is str:
    if p == p[-1::-1] :
        d[p] = len(p)
        print(d)
    else:
        print('non  - palindrom word')
else:
    print('enter only words')
'''
# WAP each word contains a character  
'''
lst=['narayana','shiva','lucky','mohan','krishna'] #['aaaa','a', '','a','a']
c=[]
for i in lst:
    s=''
    for j in i:
        if j == 'a':
            s=s+j
    c.append(s)
print(c)
'''

# number reverse
'''

n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)

'''

# Take lengthy string and count total number consonants in dict format
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
# How to check given object is string or not

'''
my_string = 'Hello'

if isinstance(my_string, str):
    print("The object is a string.")
else:
    print("The object is not a string.")

'''

# ascending order        descending order       
'''
# Define a string
my_string = "Hello, World!"

# Sort the string in ascending order
sorted_string = sorted(my_string)

# Display the sorted string
print("".join(sorted_string))

# Sort the string in descending order
sorted_string = sorted(my_string, reverse=True)

# Display the sorted string
print("".join(sorted_string))

'''
'''
w=''
a = 'Ruby'
for i in a:
    w = i+w
print(w)
'''
'''
from numpy import *

a = array([[[10,20,30]],[[40,50,60]],[[60,70,80]]])
print(a)

'''



'''
lst = ['1','2']
a = ''.join(lst)
'''
'''
def arrange_players(n, A):
    highest_rated = [i for i in range(n) if A[i] == -1]
    remaining = [(A[i], i) for i in range(n) if A[i] != -1]
    remaining = sorted(remaining, reverse=True)
    result = [-1] * n
    i = 0
    j = 0
    while i < len(highest_rated) and j < len(remaining):
        if highest_rated[i] < remaining[j][1]:
            result[highest_rated[i]] = remaining[j][1]
            i += 1
        else:
            result[remaining[j][1]] = highest_rated[i]
            j += 1
    while j < len(remaining):
        result[remaining[j][1]] = highest_rated[-1]
        highest_rated.pop()
        j += 1
    
    return result
'''

#print([i for i in range(30)])



stu ={ 's1':{'name':'revi','no':1},
       's2':{'name':'sai','no':2} }

# wap to display number 2 has taken students name


# waptd whose name contain 4 letters only
'''
for i in stu:
    if len(stu[i]['name']) == 4:
        print(stu[i]['name'])
    
'''
names = "python is simple language"

na = names.split()

l=[]
for i in na:
    l.append(len(i))
for j in na:
    if len(j) == min(l):
        print(j)

#contact book
'''
name = []
phone_numbers = []
num = int(input("enter no of contact you want to save :"))
for i in range(num):
    name = input("name:")
    phone_number = input("phone number:")
    names.append(name)
    phone_numbers.append(phone_number)
print("\nName\t\t\tPhone Number\n")
for i in range(num):
    print("{}\t\t\t{}".format(names[i], phone_numbers[i]))
search_term = input("\nenter search term:")
print("search result:")
if search_term in names:
    index = names.index(search_term)
    phone_number = phone_numbers[index]
    print("name: {}, phone number: {}".format(search_term, phone_number))
else:
    print("name not found")
'''
'''
num = eval(input('enter any number: '))
counter = 0
if num == 0:
    counter = 1
elif num < 10:
    counter = 1
elif num < 100:
    counter = 2
elif num < 1000:
    counter = 3
else:
    while num > 0:
        num = num // 10
        counter += 1
print(counter)
'''


'''
a = eval(input('enter any character: ').lower())
vowel=['a','e','i','o','u']
if type(a) == str:
    if len(a) == 1: # enter value in ''
        if a in vowel:
            print('{} is vowel'.format(a))
        else:
            print('{} is consonant'.format(a))
    else:
        print('one character')
else:
    print('pls enter only string values')
'''






















