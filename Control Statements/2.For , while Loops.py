            # example

# 1.
'''
ls = [10,20,30,40,50]
for i in ls:
    print('lucky')
    print(i)
    print() # print(end='\n') is default
'''

# 2.
'''
st = 'lucky'
for i in st:
    print(i)
    #print(i, end=' ')
'''

# 3.
'''
emp = {'eno':100,'ename':'lucky','salary':30000}
for i in emp:
    print(i,'-',emp[i])
'''

                # range()
#examples
"""             
range(1,10,1) --> 1,2,3,4,5,6,7,8,9
range(2,7)    --> 2,3,4,5,6 
range(5)      --> 0,1,2,3,4
"""

#1.Write a program to Generate the numbers between 1 to 15
"""
for i in range(1,16,1):
    print(i)
"""
'''
i=1
while i < 16:
    print(i)
    i=i+1
'''    

#2.Write a program to Generate the numbers between 10 to 20
'''
for i in range(10,21,1):
    print(i)
'''
'''
i=10
while i < 21:
    print(i)
    i=i+1
'''

#3. 1 to 50 (5 divisible only)
'''
for i in range(1,51,5):
    print(i)

        # or
  
for i in range(1,51):
    if i%5 == 0:
        print(i)

'''
i = 1
while i < 51:
    if i%5 == 0:
        print(i)
    i=i+1

       
    
#4. 11 to 21 (odd number)
'''
for i in range(11,22,2):
    print(i)
'''

    #   11 to 21 (even number)
"""
for i in range(11,21):
    if i%2 == 0:
        print(i)
"""

#5. between 10 to 1
"""
for i in range(10,0,-1):
    print(i)
"""

#6. between -10 to -1
'''
for i in range(-10,0):
    print(i)
'''

#7. between -5 to -15
"""
for i in range(-5,-16,-1):
    print(i)
"""

#8. between 5 to -5
'''
for i in range(5,-6,-1):
    print(i)
'''

#9. between -5 to 5
'''
for i in range(-5,6):
    print(i)
'''

#10. between -21 to 21  ( divisible by 3 )
'''
for i in range(-21,22,3):
    print(i)
'''

#11. between -1 to 1
'''
for i in range(-1,2):
    print(i)
'''

#12. between 0 to 1
'''
for i in range(0,2):
    print(i)
'''

#13. between 0 to -1
'''
for i in range(0,-2,-1):
    print(i)
'''

#14. between -1 to 0
'''
for i in range(-1,1):
    print(i)
'''

#15. between -5 to 7 ( odd numbers )
'''
for i in range(-5,8,2):
    print(i)
'''

        # even number
'''
for i in range(-5,8):
    if i%2 == 0:
        print(i)
'''

#16. lst = [2,5,4,7,9] 
'''
lst = [2,5,4,7,9]
a = []
for i in lst:
    if i%2 == 0:
        a.append(i)
print(a)
'''

#17. lst = [10,15,4,7,25,75,100,21,14]


'''
lst = [10,15,4,7,25,75,100,21,14]
b = []
for i in lst:
    if i%5 == 0:
        b.append(i)
print(b)
'''

#18. lst=['a',1,4,True]
'''
lst=['a',1,4,True]
a = []
for i in lst:
    if type(i) == int:
        a.append(i)
print(a)
'''

#19.lst = ['a','e','i','k','l']

'''
lst = ['a','e','i','k','l',14.20,14,48]

v = ['a','e','i','o','u']

n =[]

for i in lst:
    if i in v:
        n.append(i)
print(n)
'''
        
#20. given string fetch consonants

"""
s = 'lakshmi narayana'
v = ['a','e','i','o','u']

for i in s:
    if i not in v :
        print(i,end = ' ')
"""      
    
    










            
