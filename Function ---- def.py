# fixed length & non-keyswords
'''
def display(a,b):
    print(a+b)
display(10,20)
'''
# fixed length & keyswords
'''
def display(a,b):
    print(a+b)
display(a=10,b=20)
'''
# variable length & non-keyswords
'''
def dis(a,*b):
    print(a)
    print(b)
dis(10,20,30,40,50)
'''
# variable length & keyswords
'''
def d(a,**b):
    print(a)
    print(b)
d(a=10,b=20,c=30,d=40)
'''
#1.write a python function to find the highest number of two given numbers
'''
n= eval(input('enter 1st number: '))
m= eval(input('enter 2nd number: '))

def highest(a,b):
    if a>b:
        print(a)
    else:
        print(b)
highest(n,m)
'''
#2.write a python function to find the squares of all even number from list
'''
ls=[3,2,5,7,6,8]
def s(ls):
    lst=[]
    for i in ls:
        if i%2==0:
            lst.append(i*i)
    print(lst)        
s(ls)
'''
#3.write a python function to count total number of vowels given string
'''
st='python narayana tech house'
def cv(st):
    v='aeiou'
    d={}.fromkeys(v,0)
    for i in st:
        if i in v:
            d[i]=d[i]+1
            d[i]=st.count(i)
    print(d)
cv(st)

'''
#4.write a python function to count total number of uppercase characters in the given string
'''
st='PythoN NarayanA TecH HousE'
def up(st):
    sri=0
    for i in st:
        if i.isupper():
            sri=sri+1
    print(sri)
up(st)
'''
#5.write a python function to convert the first and last character of each word into uppercase
"""
st='narayana tech house'
def fl(st):
    s=st.split()
    ls=[]
    for i in s:
        s=i[0].upper()+i[1:-1]+i[-1].upper()
        ls.append(s)
    luc=' '.join(ls)
    print(luc)
fl(st)
"""
#6.write a python function to convert the all vowels into uppercase in the given string
'''
st='narayana tech house'
em=[]
for i in st:
   if i in 'aeiou':
       em.append(i.upper())
   else:
       em.append(i)
print(''.join(em))
'''
#7.write a python function to remove the space from string
'''
st='narayana tech house'
def r(st):
    s=st.replace(' ','')
    print("'"+s+"'")
r(st)
'''
#8.write a python function to get the first and last character of character of each word
'''
s='python narayana tech house'
s1=s.split()
ls=[]
for i in s1:
    k=i[0]+i[-1]
    ls.append(k)
str=' '.join(ls)
print(str)
'''
#9.write a python function to fetch only all vowels from each word given string
'''
s='python narayana tech house'
ls=[]
for i in s:
    if i in 'aeiou':
        ls.append(i)
    elif i==' ':
        ls.append(' ')
print(''.join(ls))
'''
#10.write a python function replace all space by commas in the string
'''
s='python narayana tech house'
st=s.replace(' ',',')
print(st)
'''
#11.write a python function to fetch  all vowels from palindrom words

st=['mom','python','malayalam','madam']
ls=[]
for i in st:
    if i==i[-1::-1]:
        ls.append(i)
mf=[]
for j in ls:
    ls1=[]
    for k in j :
        if k in 'aeiou':
            ls1.append(k)
    s=''.join(ls1)
    mf.append(s)
print(mf)


for i in st:
    if i==i[-1::-1]:
        ls.append(i)
        for j in ls:
            u=[]
            for j in 'aeiou':
               u.append(j)
print(u)
           

#12.write a python function to count total number of words which has lessthen 7 characters
'''
st=['python','malayalam','flask','language','django']
c=0
for i in st:
    if len(i) < 7:
        c=c+1
print(c)
'''
#13.write a python function to count total number of words has all uppercase characters
'''
st=['PYTHON','MYSQL','ui','full stack']
c=0
for i in st:
    if i.isupper():
        c=c+1
print(c)
'''



