'''
a= open('lucdata.txt','w')
a.write("TCS")
a.close()
'''
# Enter the data in file handling
'''
x=open('nthdata.txt','w')
x.write('TCS,Kohli,Dhoni,Surya,Yadav\nWIPRO,Nani,Ramesh,Kohli,Sai\nINFOSYS,Renu,Ram,Satya,Charan,Dhoni\nCTS,Kohli,Aakash,Prakash,Ramesh,Sai')
x.close()
'''
# Get the data from file
'''
a=open('lucdata.txt')
b=a.read()
print(b)
'''

#1.Write a program to fetch all the data from the files
'''
x=open('lucdata.txt')
y=x.read()
print(y)
'''
#2.Write a program to fetch frist line from the file
'''
print(open('lucdata.txt').readline())

print(open('lucdata.txt').readlines()[0])
'''

#3.Write a program to fetch the last line from the file
#print(open('lucdata.txt').readlines()[-1])

#4.Write a program to count total number of character in the file [including all special character ]
#print(len(open('lucdata.txt').read()))

# Write a program to count total number of character in the file [excluding all special character ]
'''
k=[]
for i in open('lucdata.txt').read():
    if i !=',' and i !='\n':
        k.append(i)
print(len(k))
'''
#5.Write a program to count total number of lines in the file
#print(len((open('lucdata.txt').readlines())))

#6.Write a program to count total number of occurances of 'Sai' in the file
#print((open('lucdata.txt').read().count('Sai')))

#7.Write a program to count total number of words in the first line
#print(len(open('lucdata.txt').readline().split(',')))

#8.Write a program to count total number of words in the file
#print(len(open('lucdata.txt').read().replace('\n',',').split(',')))

#9.Write a program to count total number of commas in the file
#print(open('lucdata.txt').read().count(','))

#10.Write a program to fetch the first word from first line

print(open('lucdata.txt').readline().split(',')[0])
print(((open('lucdata.txt').read()).replace('\n',',')).split(',')[0])

#11.Write a program to fetch the first words from each line

a=open('lucdata.txt').readlines()
b=[]
for i in a:
    b.append(i.split(',')[0])
print(b)
print([ i.split(',')[0] for i in open('lucdata.txt').readlines()])


#12.Write a program to fetch the last word from last line
#print(open('lucdata.txt').read().replace('\n',',').split(',')[-1])

#13.Write a program to fetch the last words from each lines
'''
a=open('lucdata.txt').readlines()
b=[]
for i in a:
    b.append(i.split(',')[-1].replace('\n',''))
print(b)
print([ i.split(',')[-1].replace('\n','') for i in open('lucdata.txt').readlines()])
'''
#14.Write a program to count total number of uppercase words in the file
#print(len([i for i in open('lucdata.txt').read().replace('\n',',').split(',') if i.isupper()]))


#15.Write a program to fetch the third word from second line
#print(open('lucdata.txt').readlines()[1].replace('\n','').split(',')[2])

#16.Write a program to count total number of uppercase characters in the file
'''
c=0
a=open('lucdata.txt').read().replace('\n',',').split(',')
for i in a:
    for j in i:
        if j.isupper():
            c=c+1
print(c)
'''
#17. write a program to fetch first character of second word in the third line ?
#print(open('lucdata.txt').readlines()[2].replace('\n','').split(',')[1][0])

#18. write a program to count the length of third word in the thirdline ?
#print(len(open('lucdata.txt').readlines()[2].replace('\n','').split(',')[2]))

#19. write a program to count all the words in dict format ?
'''
x=open('lucdata.txt').read().replace('\n',',').split(',')
d={}.fromkeys(x,0)
for i in x:
    d[i]=d[i]+1
print(d)
'''
#20. write a program to count of all vowels in the dict format ?
'''
x=open('lucdata.txt').read().replace('\n',',').lower()
v='aeiou'
d={}.fromkeys(v,0)
for i in x:
    if i in d:
        d[i]=d[i]+1
print(d)
'''
#21. write a program to fetch all duplicate words in the file ?
"""
a=open('lucdata.txt').read().replace('\n',',').split(',')
s=[]
for i in a:
    if a.count(i) > 1:
        s.append(i)
d={}.fromkeys(s,0)        
for i in s:
    d[i]=d[i]+1
print(d)
"""
#22. write a program to fetch all unique words in the life ?
'''
x=open('lucdata.txt').read().replace('\n',',').split(',')
print(list(set([i for i in x if x.count(i)>1])))
'''
#23. write a program to fetch all words which starts with vowel ?
"""
print([i for i in open('lucdata.txt').read().replace('\n',',').lower().split(',') if i[0] in 'aeiou'])

a=open('lucdata.txt').read().replace('\n',',').lower().split(',')
for i in a:
    if i[0] in 'aeiou':
        print(i)
""" 
#24. write a program to fetch all words which contains either 3 or 4 characters ?

#print([i for i in open('lucdata.txt').read().replace('\n',',').split(',')  if len(i)==3 or len(i)==4])

#25. write a program to fetch the longest word in the file 
'''
lst=[]
x=open('lucdata.txt').read().replace('\n',',').split(',')
for i in x:
    lst.append(len(i))
print([i for i in x if len(i)==max(lst)])
'''





















