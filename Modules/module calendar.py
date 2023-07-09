from calendar import *

#1.Write a programms to display all the days
print([i for i in day_name])

#2.Write a programs to fetch the all days which has only 6 characters
#print([i for i in day_name if len(i) == 6])

#3.WAP to fetch all the days which starts with 'Tu'?
#print([i for i in day_name if i[0] in 'Tu'])

#4.WAP to fetch all the days which has more vowels?
'''
l=[]
for j in day_name:
    l.append(j.count('a')+j.count('e')+j.count('i')+j.count('o')+j.count('u'))
for j in day_name:
    if j.count('a')+j.count('e')+j.count('i')+j.count('o')+j.count('u')==max(l):
        print(j)
'''

#5.WAP to fetch all the days which has only vowel 'a' along with consonants?
'''
for i in day_name:
    a = False
    for j in i:
        if j not in 'aA' and j
        in 'eiouEIOU':
            a = True
    if a == False:
        print(i)
'''
#6.WAP to display all the days except 'day'?
'''
for i in day_name:
    a= ''.join(i)
    print(a.replace('day',''))
    # or
print([i for i in day_abbr ])
'''
#7.WAP to fetch longest day(which has more number of characters)?
#print(max([i for i in day_name ]))

#8.WAP to fetch all the day except vowels?
'''
v=[]
for j in day_name:
    s=''
    for i in j:
        if i in 'aeiou':
            continue
        s = s + i
    v.append(s)
print(v)
# or
l=[]
for i in day_name:
    for j in i:
        if j not in 'aeiou':
            l.append(j)         
s=''.join(l)
print(s.replace('y','y '))
'''
#9.WAP to fetch the shortest day?
#print([ i for i in day_name if len(i) == min([len(j) for j in day_name ]) ])


#10.WAP to fetch all the days which starts with 's' characters and has more characters?
#print([ i for i in day_name  if len(i) == max([len(j) for j in day_name if j.startswith('S')]) and i.startswith('S') ])

        
#11.WAP to fetch all the days which has two or more than two 'e' characters?
#print([ i for i in day_name if i.count('e') >=2 ])

#12.WAP to fetch all the days which has even number of characters?
#print([i for i in day_name if len(i)%2==0])

#13.WAP to display all the days with only start and end character?
#print([ i[0]+i[-1] for i in day_name ] )

#14.WAP to convert all lowercase character into uppercase and uppercase character into lowercase?
'''
u=''
for i in  day_name:
    for j in i:
        if j.isupper():
            u = u+j.lower()
        else:
            u += j.upper()
print(u.replace('Y','Y '))
'''
#15.WAP to convert all vowels into uppercase and consonants into lowercase?
'''
v=''
for j in day_name:
    for i in j:
        if i in 'aeiouAEIOU':
            v += i.upper()
        else:
            v += i.lower()
print(v.replace('y','y '))
'''
#16.WAP to fetch all the months?
#print([ i for i in month_name[1::] ])

#17.WAP to fetch all the months which ends with 'ber'?
#print([i for i in month_name if i.endswith('ber') ])

#18.WAP to fetch the months name which has less number of characters?
#print([ i for i in month_name if i != ' ' and len(i) == min([len(j) for j in month_name[1::]]) ])

#19.WAP to fetch all months name which are having even number index?
'''
for i in month_name[1::]:
    if month_name[1::].index(i)%2 == 0:
        print(i)
        
n = []
c = []
d={}
for i in month_name[1::]:
    n.append(i)
    c.append(month_name[1::].index(i))
for i,j in zip(n,c):
    d[i] = j
print(d)
'''
#20.WAP to display the shortest word which does not ends with 'y'?
'''
l=[]
for i in month_name[1:]:
    if i[-1] != 'y':
        l.append(len(i))
for i in month_name:
    if len(i)==min(l) and i[-1] != 'y':
        print(i)
'''       
#21.WAP to fetch the months name as per user choice?
'''
d = eval(input('Enter Any Number: '))
l=[]
for i in month_name:
    l.append(i)
print(l)
if '1' in d:
    print(l[1])
elif '2' in d:
    print(l[2])
elif '3' in d:
    print(l[3])
elif '4' in d:
    print(l[4])
elif '5' in d:
    print(l[5])
elif '6' in d:
    print(l[6])
elif '7' in d:
    print(l[7])
elif '8' in d:
    print(l[8])
elif '9' in d:
    print(l[9])
elif '10' in d:
    print(l[10])
elif '11' in d:
    print(l[11])
elif '12' in d:
    print(l[12])
else:
    print(" Invalid number ! " )
'''  
#22.WAP to fetch the day name as per user choice?
'''
d = input('Enter Any Number: ')
l=[]
for i in day_name:
    l.append(i)
if '1' in d:
    print(l[0])
elif '2' in d:
    print(l[1])
elif '3' in d:
    print(l[2])
elif '4' in d:
    print(l[3])
elif '5' in d:
    print(l[4])
elif '6' in d:
    print(l[5])
elif '7' in d:
    print(l[6])
else:
    print(" Invalid number! " )
'''
