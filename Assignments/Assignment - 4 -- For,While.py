#1. Write a program to generate all 5 divisibles from 10 to 50?
'''
for i in range(10,51,5):
    print(i)

i = 10
while i < 51:
    print(i)
    i = i+5
'''
#2. Write a program to generate all 10 divisibles from 100 to 10?
'''
for i in range(100,9,-10):
    print(i)

i = 100
while i > 9:
    print(i)
    i = i-10
'''  
#3. Write a program to generate all odd numbers from 11 to 25?
'''
for i in range(11,26,2):
    print(i)

i = 11
while i < 26:
    print(i)
    i = i+2
'''
#4. Write a program to generate all even numbers from -2 to -22?
'''
for i in range(-2,-23,-2):
    print(i)

i = -2
while i > -23:
    print(i)
    i = i-2

'''
#5. Write a program to generate all numbers from -3 to 5?
'''
for i in range(-3,6):
    print(i)


i = -3
while i < 6:
    print(i)
    i = i+1
'''
#6. Write a program to generate all 7 divisibles from -21 to 21?
'''
for i in range(-21,22,7):
    print(i)

i = -21
while i<22:
    print(i)
    i = i+7
'''    
#7. Write a program to generate all numbers from 1 to 10 except 2 and 6?
'''
for i in range(1,11):
    if i not in [2,6]:
        print(i)

i = 1
while i < 11:
    if i != 2 and i != 6:
        print(i)
    i = i + 1
'''     
#8. Write a program to generate all numbers from 15 to 1 except 3,6,9 and 12?
'''
for i in range(15,0,-1):
    if i not in [3,6,9,12]:
        print(i)

i = 15
while i > 0:
    if i not in [3,6,9,12]:
        print(i)
    i = i-1
'''   
#9. Write a program to generate all numbers from -2 to 2 except -1 and 1?
'''
for i in range(-2,3):
    if i != -1 and i !=1:
        print(i)

i = -2
while i < 3:
    if i != -1 and i !=1:
        print(i)
    i = i+1
'''
#10. Write a program to generate all 3 divisibles from 15 to -15 except even numbers?
'''
for i in range(15,-16,-1):
    if i%2 != 0:
        print(i)

i = 15
while i > -16:
    if i%2 != 0:
        print(i)
    i = i-1
'''    
