# Pattern-1
'''
n = int(input("Number of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()
'''
# Pattern-2
'''
n = int(input("Number of Rows: "))
K=1
for i in range(1,n+1):
    for j in range(1,K+1):
        print('*',end='')
    K=K+2
    print()
'''
# Pattern-3
'''
n = int(input("Number Of Rows: "))
for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=' ')
    for j in range(0,i+1):
        print('*',end=' ')
    print()
'''
# Pattern-4:
'''
n = int(input("Number Of Rows: "))
for i in range(n):
    for j in range(1,i+1):
        print(i,end=' ')
    print()
'''
# Pattern-5:
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(i,end=' ')
    print()
'''
# Pattern-6:
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
'''
# Pattern-7:
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-i,end=' ')
    print()
'''
# Pattern-8:
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n,end=' ')
    print()
'''
# Pattern-9:
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=' ')
    print()
'''
# Pattern-10:
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print('',end=' ')
    for k in range(1,i+1):
        print(n,end='')
    print()
'''
# Pattern-11
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,i):
        print('',end=' ')
    for k in range(1,n+2-i):
        print('*',end='')
    print()
'''
# Pattern-12
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n, end='')
    for k in range(1,i+i):
        print('',end=' ')
    for m in range(1,n+2-i):
        print(n,end='')
    print()
'''
# Pattern-13
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=' ')
    for k in range(1,n+2-i):
        print(' ',end=' ')
    for m in range(1,n+2-i):
        print(' ',end=' ')
    for x in range(1,i+1):
        print(n,end=' ')
    print()
'''
# Pattern-14:
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for a in range(1,n+2-i):
        print(n,end=' ')
    for b in range(1,i+i):
        print(' ',end=' ')
    for c in range(1,n+2-i):
        print(n,end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n, end=' ')
    for k in range(1,n+1-i):
        print(' ',end=' ')
    for m in range(1,n+2-i):
        print(' ',end=' ')
    for x in range(1,i+1):
        print(n,end=' ')
    print()
'''
# Pattern-15
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
'''
# Pattern-16:
'''
n=int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(n+1-i,0,-1):
        print(j,end=" ")
    print()
'''
# Pattern-17:
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end=" ")
    print()
'''
# Pattern-18:
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''
# Pattern-19:
'''
n=int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
'''            
# Pattern-20
'''
n=int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    for m in range(1,i+1):
        print(m,end=' ')
    print()
'''
# Pattern-21
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        print(k,end=" ")
    for m in range(i,0,-1):
        print(m,end=" ")
    print()
'''            
# Pattern-22
'''           
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
for i in range(1,n+1):
    for k in range(1,n+2-i):
        print(k,end=" ")
    print()
'''
# Pattern-23
'''
n=int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for x in range(1,n+1-i):
        print(" ",end=" ")
    for y in range(1,n+1-i):
        print(" ",end=' ')
    for z in range(1,i+1):
        print(z,end=" ")
    print()
'''
# Pattern-24
'''
n=int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    for b in range(1,n+1-i):
        print(' ',end=' ')
    for a in range(1,n+1-i):
        print(' ',end=" ")
    for c in range(i,0,-1):
        print(c,end=' ')
    print()
'''
# Pattern-25
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for a in range(1,n+1-i):
        print(' ',end=' ')
    for b in range(1,i+1):
        print(b, end=' ')
    for i in range(i,0,-1): 
        print(i,end=' ')
    print()
for i in range(1,n+1):
    for x in range(1,i):
        print(' ',end=' ')
    for y in range(1,n+2-i):
        print(y,end=' ')
    for k in range(n+1-i,0,-1):
        print(k,end=' ')
    print()
'''
# Pattern-26
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(0,n+2-i):
        print(j,end=' ')
    print()
'''
# Pattern-27
'''
n = eval(input("Enter Any Number:"))
k = 1
for i in range(1,n+1):
    for j in range(i):
        if k>n:
            break
        print(k,end=' ')
        k = k+1
    if k>n:
        break
    print()
'''
# Pattern-28
'''
n = eval(input("Enter Any Number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(1,i):
        print(k,end=' ')    
    print()
'''              
# Pattern-29
'''
n = eval(input("Enter Any Number:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    for k in range(i-1,0,-1):
        print(k,end=' ')
    print()
'''
# Pattern-30
'''
n = eval(input('Enter Any Number:'))
for i in range(1,n+1):
    for j in range(n,i-1,-1):
        print(j,end=' ')
    for k in range(i,n+1):
        print(k,end=' ') 
    print()
'''
# Lucky {Heart}
'''          
for i in range(6):
    for j in range(7):
        if (i==0 and j%3 !=0) or (i==1 and j%3 ==0) or (i-j==2) or (i+j==8):
            print('*',end='')
        else:
            print(end=' ')
    print()
'''
# box type
'''
n = int(input("Number Of Rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-1):
        print(j,end=" ")
    print()
'''
# L-Shape
'''
for row in range():
    for col in range():
        if 
'''





        


