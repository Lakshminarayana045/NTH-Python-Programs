#1. Write a program to check whether a specific player is available in team or not,
#   if not available then append in the team

'''
team = ['Kohli', 'Dhoni', 'Sachin', 'Surya']
p = input('Enter Player name: ')
if p in team:
    print('player is available in team')
else:
    print(p,'is not available team')
    team.append(p)
    print(team)
'''

#2. Write a program to check which language is learning by student.
#   If he is learning Python then tell him that he is learning
#   updated skill otherwise tell him to learn python

'''
c = input('Enter your programming language: ').lower()
if c == python:
    print('Your learning updated skill')
else:
    print('You learn python')
'''

#3. Write a program to check whether the given number is divisible by 10 or not?
'''
n = eval(input('Enter Any Number: '))
if type(n) is int:
    if n%10 == 0:
        print(n,'is divisible by 10')
    else:
        print(n, ' is not divisible by 10')
else:
    print('Enter interger values only')
'''
#4. Write a program to check what type of value is given by user?
'''
dt=eval(input('Enter any value: '))
if type(dt) is int:
    print(dt,"is int datatype")
elif type(dt) is float:
    print(dt,"is float datatype")
elif type(dt) is bool:
    print(dt,"is bool datatype")
elif type(dt) is complex:
    print(dt,"is complex datatype")
else:
    print(dt,"is string datatype")
'''

#5. Write a program to check whether a given string is available or not in the string?
'''
st='python is easy and powerful language'
s = input('Enter string only: ')
if s in st:
    print('given string is available')
else:
    print('given string is not available')
'''    
#6. Write a program for following requirement:
#   Monday, Tuesday, Wednesday, Thursday --> You can wear School Uniform
#   Friday --> You can wear Civil Dress     Saturday --> You can wear white and white   Sunday -->  Its your choice

'''
days=['Monday','Tuesday','Wednesday','Thursday']
d = input('what is today : ').title()
if d in days:
    print('You can wear School Uniform')
elif d == 'Friday':
    print('You can wear Civil Dress')
elif d == 'Saturday':
    print('You can wear white and white')
elif d == 'Sunday':
    print('Its your choice')
else:
    print('you tell me correct day ')

'''

#7. Write a program for following requirement:
#       you need to ask user to enter name, gender.
#       if gender is male then ask him to enter age. if age is more then 30 then ask him to marry.
#       if gender is female then ask her to enter age.if age is more then 25 then ask her to marry.

'''
name = input('Enter your name: ')
gender = input('Enter your gender: ').lower()
if gender == 'male':
    age = eval(input('Enter your age: '))
    if age > 30:
          print('what rey your age very high fristly get marry')
    else:
        print('wait some time you get beautifull wife')
elif gender == 'female':
    age = eval(input('Enter your age: '))
    if age > 25:
        address = input('Tell me your address: ')
        print("i will come to your house,You don't worry we will get marry")
    else:
        print('wait some time you get good package husband')
else:
    print('enter only male or female only')
'''   

#8. Write a program for following requirement:
#       0 to 5 --> You are an Infant
#       6 to 16 --> You are school going kid
#       17 to 22 --> You are college going kid
#       23 to 30 --> You need to settle in life and get marry
#       31 to 45 --> You need to work and earn money
#       46 to 60 --> You need to do business
#       61 and above You need to take rest 
#       below 0 -->Invalid Age, please check once
'''
age = eval(input('Enter your age: '))
if type(age) is int:
    if age > 0 and age <= 5:
        print('You are an Infant')
    elif age >= 6 and age <= 16:
        print('You are school going kid')
    elif age >= 17 and age <= 22:
        print('You are college going kid')
    elif age >= 23 and age <= 30:
        print('You need to settle in life and get marry')
    elif age >= 31 and age <= 45:
        print('You need to work and earn money')
    elif age >= 46 and age <= 60:
        print('You need to do business')
    elif age >= 61:
        print('You need to take rest')
    else:
        print('Invalid Age, please check once')
else:
    print('enter your correct age ')

'''
#9. Write a Python Program to find BMI(Body Mass Index)?
#       Take height (in cms) and weight (in kgs) from user.
#       Calculate BMI by using height and weight.
#       Note: Convert cms into metres BMI = Weight(in kg) / Height*Height(in metre)
#       if BMI between 0 and 18.5, display "Underweight",
#       if BMI between 18.5 and 24.9, display "Normal Weight"
#       if BMI between 25.0 and 29.9, display "Pre-Obesity"
#       if BMI between 30.0 and 40.0, display "Obesity"
#       if BMI between 40. and above, display "Extremly Obesity".

'''
height=eval(input("Enter your height (in cms):"))
weight=eval(input("Enter your weight(in kgs):"))
BMI = weight/ ((height/100)*(height/100))
BMI=weight/(height/100)**2

print(BMI)
if BMI>=0 and BMI<18.5:
    print("You are underweight")
elif BMI>=18.5 and BMI<24.9:
    print("You are normal weight")
elif BMI>=25.0 and BMI<29.9:
    print("You are Pre-Obesity")
elif BMI>=30.0 and BMI<40.0:
    print("You are Odesity")
elif BMI>=40.0:
    print("You are Extremly Obesity")
else:
    print("Invalid BMI")

'''
#10. Write a Python Program to take any one number from user,
#   that number must be between 1 and 10.
#   If the number is below 1 or more than 10 then display "Please enter any number between 1 and 10".
#   If the number between 1 and 10 then check it whether the number divisible by 2 or not.
#   If the number divisible by 2 then display "You have entered even number."
#   If the number is not divisible by 2 then display "You have entered odd number."

'''
n=eval(input("Enter any number:"))
if n < 1 or n > 10:
    print("Please enter any number in between 1 to 10")
else:
    if n%2==0:
        print('You have entered even number')
    else:
        print("You have entered odd number.")
'''
