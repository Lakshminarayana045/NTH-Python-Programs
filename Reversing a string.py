day='sunday'

#1.using slicing
print(day[::-1])


#2.by using for loop
temp=''
for i in day:
    temp=i+temp
print(temp)



#3.by using while loop
temp=''
length=len(day)-1
while length>=0:
    temp=temp+day[length]
    length=length-1
print(temp)


#4.by using list reverse
temp=list(day)
temp.reverse()
print(''.join(temp))

             
#5.by using recursion
def reverse_Rec(str):
    if len(str)==0:
        return str
    else:
        return reverse_Rec(str[1:])+str[0]
print(reverse_Rec('sunday'))


#6.by using reversed
temp=reversed(day)
print(''.join(temp))

#7.number reverse

n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number: ",rev)



#switching cases based on odd and even numbers or alternatives numbers 
'''
a='university'
result=''.join([a[i].lower()if i%2==0 else a[i].upper() for i in range(len(a))])
print(result)


for i in range(len(a)):
    if i%2==0:
        print(a[i].upper(),end='')
    else:
        print(a[i].lower(),end='')
'''
