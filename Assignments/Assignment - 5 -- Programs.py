#1. Write a program to fetch all even numbers from list?
'''
lst=[10,11,13,14,9,8]
l=[]
for i in lst:
    if i%2 == 0:
        l.append(i)
print(l)
'''
#2. Write a program to fetch all string values from list?
'''
lst=[10,'a',True,'b',False]
a=[]
for i in lst:
    if type(i) is str:
        a.append(i)
print(a)
'''   
#3. Write a program to fetch all 5 divisibles from list?
'''
lst=[12,15,27,20,5]
k=[]
for i in lst:
    if i%5 == 0:
        k.append(i)
print(k)
'''
#4. Write a program to count total number of int values in the list
'''
lst=[10,'a',20,True,30,'b',40]
c=0
for i in lst:
    if type(i) is int:
        c=c+1
print(c)
'''
#5. Write a program to count total number of characters in the string(including space)
'''
st='Python language'
z=0
for i in st:
    z=z+1
print(z)

print(len(st))
'''
#6. Write a program to count total number of words in the string
'''
st='python narayana tech house hyd'
h=0
for i in st.split():
    h=h+1
print(h)
'''
#7. Write a program to fetch all vowels from the string? 
'''
st='Python language'
m=[]
for i in st:
    if i in'aeiouAEIOU':
        m.append(i)
print(m)
'''
#8. Write a program to count total number of vowels
'''
st='python narayana'
i=[]
for j in st:
    if j in'aeiouAEIOU':
        i.append(j)
print(len(i))
'''

#9. Write a program to count total number of characters in the string(excluding space)?
'''
st='python is a simple language'
n=[]
for i in st:
    if i != ' ':
        n.append(i)
print(len(n))
'''

#10. Write a program to count total number of consonants in the string?
'''
st='python language'
a=[]
for i in st:
    if i not in 'AEIOUaeiou' and i != ' ':
        a.append(i)
print(len(a))
'''
#11. Write a program to fetch all words which starts with vowel from given string?
'''
st='Python is simple and easy language'
r=[]
for i in st.split():
    if i[0] in 'aeiou':
        r.append(i)
print(r)
'''
#12. Write a program to fetch all words which ends with consonent in the given string?
'''
st='Python is simple and easy language' 
a=[]
for i in st.split():
    if i[-1] not in 'aeiou':
        a.append(i)
print(a)
'''
#13. Write a program to fetch all words which 'a' two or more then two times?
'''
st='Python is simple and easy language'
y=[]
for i in st.split():
    if i.count('a') >= 2:
        y.append(i)
print(y)
'''

#14. Write a program to count number of characters of each word in the string?
'''
st='Python is simple and easy language'
a=[]
for i in st.split():
    a.append(len(i))
print(a)
'''
#15. Write a program to fetch the first and last character from each word in the string?
'''
st="Python is simple and easy language"
g=[]
for i in st.split():
    g.append(i[0]+i[-1])
print(g)
'''

#16. Write a program to fetch all words which contains a' character in the string?
'''
st='Python is simple and easy language'
o=[]
for i in st.split():
    if 'a' in i:
        o.append(i)
print(o)
'''
#17. Write a program to fetch all words which does not contain 'e' character in string 
'''
st='Python is simple and easy language'
o=[]
for i in st.split():
    if 'e' not in i:
        o.append(i)
print(o)
'''

#18. Write a program to fetch all words which contains only 4 or lessthen 4 character
'''
st='Python is simple and easy language'
d=[]
for i in st.split():
    if len(i) <= 4:
        d.append(i)
print(d)
'''
#19. Write a program to fetch all words which contain odd number of characters in the string?
'''
st='Python is simple and easy language'
l=[]
for i in st.split():
    if len(i)%2 != 0:
        l.append(i)
print(l)
'''
#20. Write a program to fetch all words which starts and ends with vowel in the string?
'''
st='Python is number one language'
lucky=[]
for i in st.split():
    if i[0] in 'aeiou' and i[-1] in 'aeiou':
        lucky.append(i)
print(lucky)
'''
#21. Write a program to fetch all palindrome words from list?
'''
names = ['madam', 'python', 'dad','language','eye','malayalam']
sri=[]
for i in names:
    if i == i[-1::-1]:
        sri.append(i)
print(sri)        
'''        
#22. Write a program to fetch all non-palindrome words from list?
'''
names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
p=[]
for i in names:
    if i != i[-1::-1]:
        p.append(i)
print(p)   
'''
#23. Write a program to fetch all palindrome words which starts with 'm' character?
'''
names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
k=[]
for i in names:
    if i == i[-1::-1] and i[0] in 'm':
        k.append(i)
print(k)        
'''
#24. Write a program to fetch all palindrome words which more then 3 characters?
'''
names = ['madam', 'python', 'dad', 'language', 'eye', 'malayalam']
v=[]
for i in names:
    if i == i[-1::-1] and len(i) > 3:
        v.append(i)
print(v)    
'''
#25. Write a program to longest palindrome word?
'''
names = ['madam', 'python', 'dad', 'language' 'eye', 'malayalam']
p=[]
pl=[]
pw=[]
for i in names:
    if i == i[-1::-1]:
        p.append(i)
        pl.append(len(i))
for i in p:
    if len(i) == max(pl):
        pw.append(i)
print(pw)
'''
