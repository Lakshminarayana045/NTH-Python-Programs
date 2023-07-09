                        # 1.simpe if statement
                        
# 1.write a program to check the user value is even number or not ?
'''
n = eval(input('enter any number  '))
if n%2 == 0:
    print('it is even number')
    print('thankyou')
'''

# 2.write a program to check weather student passed in the exam or not ?
'''
marks = eval(input('enter your marks: '))
if marks >=35:
    print('congradulation !!!')
    print('your are passed in the exam')
print('where is the party')
'''

# 3.write a program to check weather a citizen is eligible for using vote or not ?
'''
name = input('enter your name: ')
age = eval(input('enter your age: '))
if age >=18:
    print('hello {},you are {} year old'.format(name,age))
    print('you are elgible to use vote')
    print('you can apply for vote ASAP')
'''

# 4.write a program to check weather the given number is divisible by 5 or not ?
'''
n = eval(input('enter your number: '))
if n%5 == 0:
    print('{} is divisible by 5'.format(n))
'''


                    # 2.if-else statement
                
# 1.write a program to check whether student passed or failed in exam ?
"""
name = input('enter your name: ').title()
marks = eval(input('enter your marks: '))
print ('hello {}, you got {} marks ! '.format(name,marks))
if marks >=35:
    print('you passed in the exam')
    print('congratulation!!!')
else:
    print('you failed in the exam')
    print('Better luck next time')
print('where is the party')
"""
# 2.write a program to find the highest number of two given numbers?
'''
n1 = eval(input('enter 1st number: '))
n2 = eval(input('enter 2nd number: '))
if n1 > n2:
    print('{} is greaterthen {}'.format(n1,n2))
else:
    print('{} is greaterthen {}'.format(n2,n1))
'''
# 3.Tell me Your name , you coming class daily
'''
a = input('Tell me your name: ').title()
b = input('Are you coming to class daily ? (yes/no): ').lower()
if a == 'yes':
    print('{} Wow good,will get more knowledge'.format(a,b))
else:
    print('{} should attend the class to get more knowledge'.format(a,b))
'''
# 4.you have id card ?
'''
ans = input('do you have id card ? (yes/no): ').lower()
if ans == 'yes':
    print('please goto class and have seat')
else:
    print('please goto room and bring it')
'''

                    # 3.elif statement

# 1.write a program to display the grade of student as per marks
"""
marks = eval(input('enter your marks: '))
if marks >= 0 and marks < 35 :
    print('failed')
elif marks >= 35 and marks < 50:
    print('C grade')
elif marks >= 50 and marks < 70:
    print('B grade')
elif marks >= 70 and marks < 90:
    print("A grade")
elif marks >= 90 and marks <= 100:
    print('Distinction')

else:
    print('Invalid marks')
  """

# 2.write a program to find the highest number of two given numbers?
'''
n1 = eval(input('enter 1st number: '))
n2 = eval(input('enter 2nd number: '))
if n1 > n2:
    print('{} is greaterthen {}'.format(n1,n2))
elif n1==n2:
    print('{}, are same value {}'.format(n1,n2))
else:
    print('{} is not greaterthen {}'.format(n1,n2))
'''
# 3.given number even or odd
'''
n = eval(input('enter any number: '))
if n%2 == 0:
    print('{} is even number'.format(n))
elif n%2 == 1:
    print('{} is odd number'.format(n))
else:
    print('invailed number')
'''
# 4.you learning course
'''
course = ['aws','develop','testing','oracle']
name = input('your name: ').title()
c = input('which course learning?: ').lower()
if c=="python":
    print('{},{} is good program language'.format(name,c))
elif c=="java":
    print('{},{} is lengthy program language'.format(name,c))
elif c==".net":
    print('{},{} is feature program language'.format(name,c))
elif c in course:
    print('ok its also good')
else:
    print("i don't a bout it")
'''
# 5.what is today?
"""
days=['monday','tuesday','wednesday','thursday']
d= input('what is today: ').lower()
if d=="friday":
    print('white and white')
elif d=='saturday':
    print('civil dress')
elif d=='sunday':
    print('today holiday, its your choice')
elif d in days:
    print('wear school uniform')
else:
    print('tell me correctly')
"""

# 6.greather then
"""a = 200
b = 33
if b > a:
    print('b is greather then a')
elif a == b:
    print('a and b are equal')
elif a != b:
    print('a and b are not equal')
elif a < b:
    print('a greather then b')
else:
    print('a then b')
"""


                # 4.nested if

# 1.given number odd and even
'''
n = eval(input('enter any number: '))
if type(n) == int:
    if n > 0:
        if n%2 == 0:
            print('{} is positive and even number'.format(n))
        else:
            print('{} is positive and odd number'.format(n))
    elif n < 0:
        if n%2 == 0:
            print('{} is negative and even number'.format(n))
        else:
            print('{} is negative and even number'.format(n))
    else:
        print('{} is zero number'.format(n))
else:
    print('enter only interger values ')
'''
# 2.given number divisible by 5
"""
n=eval(input('enter any number: '))
if type(n) is int:
    if n%5 == 0:
        print('{} is divisible by 5'.format(n))
    else:
        print('{} is not divisible by 5'.format(n))
else:
    print('please enter interger number only')
"""

# 3.IT job
'''
name=input('enter your name: ').title()
qualification=input('enter your qualification: ').lower()
year=eval(input('enter your passed out year: '))
p=eval(input('enter your percentage: '))

qu=['btech','be','mtech','me','mca','bca','bsc']
ye=[2020,2021,2022]

print('hello {},'.format(name))
if qualification in qu:
    if year in ye:
        if p > 0 and p < 35:
            print('please attend interview later with exp')
        elif p >= 35 and p < 60:
            print('please attend interview next week')
        elif p >= 60 and p < 75:
            print('please attend interview tomorrow')
        elif p >= 75 and p <= 100:
            print('please come and attend interview right now')
        else:
            print('please check your percentage')
    elif year < 2020:
        print("""your passed out your is {},sorry,
              this interview only for fresher""".format(year))
    else:
        print("""you have given {} as passed out year,
              so first completed your graduction""".format(year))
else:
    print("""year qualification is {},
          so you not eligible""".format(qualification))
'''
                # or another method

             
'''
qu=['btech','be','mtech','me','mca','bca','bsc']
ye=[2020,2021,2022]

name=input('enter your name: ').title()
qualification=input('enter your qualification: ').lower()

print('hello {},'.format(name))
if qualification in qu:
    year=eval(input('enter your passed out year: '))
    if year in ye:
        p=eval(input('enter your percentage: '))
        if p > 0 and p < 35:
            print('please attend interview later with exp')
        elif p >= 35 and p < 60:
            print('please attend interview next week')
        elif p >= 60 and p < 75:
            print('please attend interview tomorrow')
        elif p >= 75 and p <= 100:
            print('please come and attend interview right now')
        else:
            print('please check your percentage')
    elif ye < 2020:
        print("""your passed out your is {},sorry,
              this interview only for fresher""".format(ye))
    else:
        print("""you have given {} as passed out year,
              so first completed your graduction""".format(ye))
else:
    print("""year qualification is {},
          so you not eligible""".format(qualification))
'''


            # assignments
            
#1 characters count()
'''
a = eval(input('enter any character: ')) 
if type(a) == str:
    a = len(a)
    print('{} has {} characters '.format(n,a))
else:
    print('please enter english words only')
'''

            # or

"""
p=input('enter any name: ').lower()
a=len(p)
if p.isalpha():  # The isdigit() method checks if the input is a digit 
    print(p,'has',a,'characters')
    #print('{} is {} digit number'.format(p,a))
else:
    print("please enter any word ! ")
"""

#2 even or consonants
'''
a = eval(input('enter any character: ').lower())
vowel=['a','e','i','o','u']
if type(a) == str:
    if len(a) == 1: # enter value in '' 
        if a in vowel:
            print('{} is vowel'.format(a))
        else:
            print('{} is consonant'.format(a))
    else:
        print('one character')
else:
    print('pls enter only string values') 
'''


# 3 numbers count()
'''
p=input("enter the number: ")
a=len(p)
if p.isdigit():  # The isdigit() method checks if the input is a digit 
    print(p,'is',a,'digit number')
    #print('{} is {} digit number'.format(p,a))
else:
    print("please enter any interger number! ")
'''


                # or
"""            
n = eval(input('enter any number: ')) # enter char is ''
if type(n) == int:
    a = len(str(n))
    print('{} is {} digit number '.format(n,a))
else:
    print('please enter interger values only')

"""

# 4.number or charcter any one count()

'''
n = input('enter any number: ') 
a = len(n)
print('{} is {} digit number '.format(n,a))
'''

'''
fee = int(input('Enter your Hostel fee: '))
acutally_fee = [4000,3500,4500,5000]

if 0 < fee:
    if fee == 3500:
        print('low')
    elif  fee == 4000:
        print('Normal')
elif 0 > fee:
    print('Pls enter above 3500')
    
'''

   
    
        










