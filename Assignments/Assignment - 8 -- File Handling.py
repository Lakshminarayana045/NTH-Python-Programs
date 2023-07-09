'''
TCS,Sai,Rohit,Satya,Dhoni,Sarath,Saroj,Venkat,Sas
INFOSYS,Kohli,Santosh,Venkat,Koti,Prabha,Soumya,Mishra
WIPRO,Satya,Kohli,Ram,Chinna,Pop,Amelia,Suresh,Arjuna
CTS,Prabha,Subha,Debha,Rabha,Venkat,Dhoni,Surya,Saroj
NTH,Narayana,Akhil,Arha,Venkat,Sravya,Ananya,Revanth,Aha
ABC,Arha,Chinna,Satya,Dhoni,Venkat,Rohit,Yash,Nikhilesh
'''

#1. Write a program to fetch all data from the file.
#print(open('nthdata.txt').read())

#2. Write a program to read the first line from the file.
#print(open('nthdata.txt').readline())

#3. Write a program to read the last line from the file.
#print(open('nthdata.txt').readlines()[-1])

#4. Write a program to read the 3rd line from file
#print(open('nthdata.txt').readlines()[2])

#5. Write a program to count total number of characters in the file?
#print(len(open('nthdata.txt').read()))

#6. Write a program to count total number of commas in the file?
#print(open('nthdata.txt').read().count(','))

#7. Write a program to count total number of words in the first line?
#print(len(open('nthdata.txt').readlines()[0].split(',')))

#8. Write a program to count total number of lines in the file?
#print(len(open('nthdata.txt').readlines()))


#9. Write a program to count total number of 'Sai' name in the file?
#print(open('nthdata.txt').read().count('Sai'))

#10. Write a program to fetch the first word from each line in the file?
'''
for i in open('nthdata.txt').readlines():
    print(i.split(',')[0])
    
print([i.split(',')[-1].replace('\n','') for i in(open('nthdata.txt').readlines())])
'''
#11. Write a program to fetch the last word from each line?
'''
for i in open('nthdata.txt').readlines():
    print(i.split(',')[-1].replace('\n',''))

print([i.split(',')[-1].replace('\n','') for i in(open('nthdata.txt').readlines())])
'''
#12. Write a program to fetch all words which starts with 'a' Character?
'''
a=open('nthdata.txt').read()
b=a.replace('\n',',').split(',')
for i in b:
    if i[0] == 'a':
        print(i)
'''
#13. Write a program to fetch all words which ends with an vowel?
'''
a=open('nthdata.txt').read()
b=a.replace('\n',',').split(',')
x=[]
for i in b:
    if i[-1] in 'aeiouAEIOU':
        x.append(i)
print(x)

print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[-1] in 'aeiouAEIOU'])
'''
#14. Write a program to fetch all words which has either 'a' or 'i' characters in the file?
'''
a=open('nthdata.txt').read()
b=a.replace('\n',',').split(',')
r=[]
for i in b:
    if 'a' in i or 'i' in i:
        r.append(i)
print(r)
#print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if 'a' in i or 'i' in i])
'''
#15. Write a program to fetch all words which contains only 5 characters in the file?
'''
a=open('nthdata.txt').read()
b=a.replace('\n',',').split(',')
s=[]
for i in b:
    if len(i) is 5:
        s.append(i)
print(s)

print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if len(i) is 5])
'''
#16. Write a program to fetch all words which does not contains vowels except i in the file?
'''
a=open('nthdata.txt').read()
b=a.replace('\n',',').split(',')
for i in b:
    if 'a' not in i and 'e' not in i and 'o' not in i and 'u' not in i and 'i' in i:
        print(i)
'''
#17. Write a program to fetch all words which ends with uppercase character in the file?
'''
a=open('nthdata.txt').read()
b=a.replace('\n',',').split(',')
for i in b:
    if i[-1].isupper():
        print(i)

print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[-1].isupper()])
'''
#18. Write a program to count total number of characters in the file excluding commas and \ns?
'''
a=open('nthdata.txt').read().replace('\n',',')
c=0
for i in a:
    if i!=',' and i!='\n':
        c += 1
print(c)
#print(len([i for i in open('nthdata.txt').read().replace('\n',',').split(',') for j in i]))
'''
#19. Write a program to count total number of words in the entire file?
#print(len(open('nthdata.txt').read().replace('\n',',').split(',')))

#20. Write a program to fetch all even number words from from every line the file?
'''
b=open('nthdata.txt').read().replace('\n','').split(',')
for i in b:
    if len(i)%2 == 0:
        print(i)
'''    
#21. Write a program to fetch all words which ends with 'bha' in the file?
'''
b=open('nthdata.txt').read().replace('\n','').split(',')
for i in b:
    if i.endswith('bha'):
        print(i)
print([i for i in open('nthdata.txt').read().replace('\n',',').split(',')  if i.endswith( 'bha')])
'''
#22. Write a program to display all TCS employees?
'''
for i in open('nthdata.txt').readlines():
    if 'TCS' in i:
        print(i.replace('TCS,',''))
'''
#23. Write a program to display the company name of Chinna Employee?
'''
for i in open('nthdata.txt').readlines():
    if 'Chinna' in i:
        print(i.split(',')[0])
'''
#24. Write a program to fetch the 2nd from 3rd line in the file?
#print(open('nthdata.txt').readlines()[2].split(',')[1])

#25. Write a program to fetch the first character from each word in the 3rd line?
'''
for i in open('nthdata.txt').readlines()[2].split(','):
    print(i[0])
print([i[0] for i in  open('nthdata.txt').readlines()[2].split(',')])
'''
#26. Write a program to fetch first and last character of each word in the last line?
'''
for i in open('nthdata.txt').readlines()[-1].split(','):
    print(i[0]+i[-1])
    
print([i[0]+i[-1] for i in  open('nthdata.txt').readlines()[-1].split(',')])
'''
#27. Write a program to fetch all characters(except 1st and last chars) of each word in the 2nd line?
'''
for i in open('nthdata.txt').readlines()[1].split(','):
    print(i[1:-1])

print([i[1:-1] for i in open('nthdata.txt').readlines()[1].split(',')])
'''
#28. Write a program to count total number of words which starts with 'S' character?
'''
c = 0
for i in open('nthdata.txt').read().replace('\n',',').split(','):
    if i[0] in 'S':
        c +=1
print(c)
print(len([i for i in open('nthdata.txt').read().replace('\n',',').split(',')  if i.startswith( 'S')]))
'''
#29. Write a program to fetch all duplicate names in the file?
'''
l=[]
b=open('nthdata.txt').read().replace('\n',',').split(',')
for i in b:
    if b.count(i) > 1:
        l.append(i)
print(set(l))
'''
#30. Write a program to count all vowels in the file? (Note: output must be in dict)
'''
lst=['a','e','i','o','u','A','E','I','O','U']
d={}.fromkeys(lst,0)
for i in open('nthdata.txt').read().replace('\n',',').split(','):
    for j in i:
        if j in d:
            d[j]=d[j]+1      
print(d)
''' 
#31. Write a program to reverse all words in the file?
'''
l=[]
for i in open('nthdata.txt').read().replace('\n',',').split(','):
    l.append(i[-1::-1])
print(l)
print([i[-1::-1] for i in open('nthdata.txt').read().replace('\n',',').split(',')])
'''
#32. Write a program to fetch all words which contains two or more then 'a' characters?
'''
a = open('nthdata.txt').read().replace('\n',',').split(',')
for i in a:
    if i.count('a') >= 2:
        print(i)
print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i.count('a')>=2])
'''
#33. Write a program to fetch all words which starts and ends with 'a' character?
'''
a = open('nthdata.txt').read().replace('\n',',').split(',')
for i in a:
    if i[0] in 'a' and i[-1] in 'a':
        print(i)
print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[0] in 'A' and i[-1] in 'a'])
'''
#34. Write a program to fetch word which has more number of 'a' characters?

a = open('nthdata.txt').read().replace('\n',',').split(',')
k=[]
for i in a:
    k.append(i.count('a'))
for i in a:
    if i.count('a') == max(k):
        print(i)
        
print([i for i in open('nthdata.txt').read().replace('\n',',').split(',')
       if max([i.count('a') for i in open('nthdata.txt').read().replace('\n',',').split(',')
               if 'a'in i])==i.count('a')])

#35. Write a program to fetch all company names which starts with vowel?

for i in open('nthdata.txt').readlines():
    if i.split(',')[0][0] in 'aeiouAEIOU':
        print(i.split(',')[0])
        
print([i.split(',')[0] for i in open('nthdata.txt').readlines() if i.split(',')[0][0] in 'aeiouAEIOU'])

#36. Write a program to display company name which contains Saroj Employee?
'''
for i in open('nthdata.txt').readlines():
    if 'Saroj' in i.split(','):
        print(i.split(',')[0])
'''
#37. Write a program to count all words which starts and ends with consonants?
'''
c=0
for i in open('nthdata.txt').read().replace('\n',',').split(','):
    if i[0] not in 'aeiouAEIOU' and i[-1] not in 'aeiouAEIOU':
        c += 1
print(c)

print(len([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i[0] not in 'aeiouAEIOU' and i[-1] not in 'aeiouAEIOU']))
'''
#38. Write a program to fetch all company names which does not contain Venkat employee?
'''
for i in open('nthdata.txt').readlines():
    if 'Venkat' not in i.split(','):
        print(i.split(',')[0])

print([i.split(',')[0] for i in open('nthdata.txt').readlines() if 'Venkat' not in i.split(',')])
'''
#39. Write a program to display company name where Narayana is working?
'''
for i in open('nthdata.txt').readlines():
    if 'Narayana' in i.split(','):
        print(i.split(',')[0]) 

print([i.split(',')[0] for i in open('nthdata.txt').readlines() if 'Narayana' in i.replace('\n',',').split(',')])
'''      
#40. Write a program to display the first word and last word from each line in dict format?
'''
f=[]
l=[]
for i in open('nthdata.txt').readlines():
    f.append(i.split(',')[0])
    l.append(i.split(',')[-1].replace('\n',''))
d={}
for i,j in zip(f,l):
    d[i]=j
print(d)
'''
#41. Write a program to fetch all names whose name starts with 'a' in NTH company?
#print([j for i in open('nthdata.txt').read().split('\n') if 'NTH' in i for j in i.split(',') if j[0] in 'Aa'])

#42. Write a program to count total number of employees in CTS company?
#print([len(i.split(',')[1:]) for i in open('nthdata.txt').readlines() if 'CTS' in i])

#43. Write a program to fetch all companies where Venkat employee is working?
#print([i.split(',')[0] for i in open('nthdata.txt').readlines() if 'Venkat' in i])

#44. Write a program to fetch all companies names which name starts with Vowel?
#print([i.split(',')[0] for i in open('nthdata.txt').readlines() if i.split(',')[0][0] in 'aeiouAEIOU'])

#45. Write a program to fetch all palindrome names from the file?
#print([i for i in open('nthdata.txt').read().replace('\n',',').split(',') if i.lower()==i.lower()[-1::-1]])

#46. Write a program to fetch all companies names where palindrome named employees working?
#print([i.split(',')[0] for i in open('nthdata.txt').read().split('\n') for j in i.split(',') if j.lower()==j.lower()[-1::-1]])


#47. Write a program to fetch the lengthiest company name?
'''
lst=[]
for i in open('nthdata.txt').read().split('\n'):
    lst.append(len(i.split(',')[0]))
for i in open('nthdata.txt').read().split('\n'):
    if str(max(lst)) in str(len(i.split(',')[0])):
        print(i.split(',')[0])
'''
#48. Write a program to fetch the lengthiest employee name in ABC company?
'''
lst=[]
for i in open('nthdata.txt').read().split('\n'):
    if 'ABC'in i.split(','):
        for j in i.split(',')[1:]:
            lst.append(len(j))
for i in open('nthdata.txt').read().split('\n'):
    if 'ABC'in i.split(','):
        for j in i.split(',')[1:]:
            if str(max(lst)) in str(len(j)):
                print(j)
'''
#49. Write a program to fetch shortest employee name in the WIPRO company?
'''
lst=[]
for i in open('nthdata.txt').read().split('\n'):
    if 'WIPRO'in i.split(','):
        for j in i.split(',')[1:]:
            lst.append(len(j))
for i in open('nthdata.txt').read().split('\n'):
    if 'WIPRO'in i.split(','):
        for j in i.split(',')[1:]:
            if str(min(lst)) in str(len(j)):
                print(j)
'''
#50. Write a program count total number of employees in each company(in dict format)?
'''
lst=[]
for i in open('nthdata.txt').read().split('\n'):
    lst.append(i.split(',')[0])
d={}.fromkeys(lst,0)
for i in open('nthdata.txt').read().split('\n'):
    for j in i.split(','):
        if j in d:
            d[j]=len(i.split(',')[1:])
print(d)
'''

