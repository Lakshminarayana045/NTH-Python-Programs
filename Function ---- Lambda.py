#1.write a lambda expression to add two numbers
'''
x=lambda a,b:a+b
print(x(5,8))
'''
#2.write a lambda expression to find the highest number of two number
'''
h=lambda a,b:a if a > b else b
print(h(15,85))
'''
#==================================== Filter() ====================================================================

#1.write a lambda expression to filter all 3 divible
'''            
ls=[1,5,4,7,8,2,3,6,4,9]
print(list(filter(lambda i :i%3==0,ls)))        
print({i for i in ls if i%3==0})
'''
#2.write a lambda expression to filter all word which has only 6 character
'''
lst=['pyhton','falsk','django','nth']
print(list(filter(lambda i:len(i) == 6,lst)))
print({ i for i in lst if len(i) == 6})
'''
#3.write a lambda expression to filter all word which start with an vowel
'''
st='python is simple and easy language'
print(list(filter(lambda i:i[0] in 'aeiou' , st.split())))
print({ i for i in st.split() if i[0] in 'aeiou'})
'''
#4.write a lambda expression to filter all bool values from list
'''
lst=['a',True,100,'python',False,None,'is']
print(list(filter(lambda i: type(i) == bool,lst)))
print({i for i in lst if type(i) == bool})
'''


#=================================== Map()  =====================================================================

#1.write a lambda expression to add 10 to each element in the list
'''
ls=[5,4,8,7,2,3,7,9,5,4]
print(list(map(lambda i: i+10,ls)))
print([i+10 for i in ls])
'''
#2.write a lambda expression to find square of each elements
'''
ls=[5,4,8,7,2,3,7,9,5,4]
print(list(map(lambda i: i**2,ls)))
print([i**2 for i in ls])
'''
#3.write a lambda expression to find lenght of each word in the string
'''
st='python is simple and easy language'
st=st.split()
print(list(map(lambda i: len(i),st)))
print([len(i) for i in st])
'''
#4.write a lambda expression to fetch only first character form each word
'''
lst=['python','narayana','tech','house']
print(list(map(lambda i: i[0],lst)))
print([i[0] for i in lst])
'''
#5.write a lambda expression to make plural form of each word in list

lst=['player','student','course']
print(list(map(lambda i: i+'s',lst)))
print([i+'s' for i in lst])

#6.write a lambda expression to reverse of each word
"""
lst=['python','django','Ui']
print(tuple(map(lambda i: i[-1::-1],lst)))
print([i[-1::-1] for i in lst])
"""
# write a python program to count no.of occurences of each character in the string
'''
s='Lakshmi narayana'
d={}.fromkeys(s,0)
for i in s:
    #if i in d:
    d[i]=d[i]+1
print(d)
'''
# write a python program to find the lenght of string (excluding space)
"""
s='Konanki Venkat Lakshmi Narayana'
sa=0
for i in s:
    if i != '  ':
        sa=sa+1
print(sa)
""" 
#================================ Reduce() =======================================================================

#1.write a lambda expression to find the highest number the list
'''
ls=[10,14,15,58,78,45,69,32,145]
import functools as a
print(a.reduce(lambda a,b : a if a > b else b,ls))
'''
#2.write a lambda expression to find the least number the list
'''
ls=[10,14,15,58,78,45,69,32,145]
import functools as a
print(a.reduce(lambda a,b : a if a < b else b,ls))
'''
#3.write a lambda expression to find the sum all number from the list
'''
ls=[10,14,15,58,78,45,69,32,145]
import functools as b
print(b.reduce(lambda a,b: a+b,ls))
'''
