'''
class studentsdata:             # creating class  
    name = 'lucky'
    fee = 40000
    loc = 'ongole'
    def learning(self):
        print('He is learning python course')
    def practice(self):
        print('He is practicing programming ')
s1 = studentsdata()             # creating object

print(s1.name)                  # calling class attributes by using object
print(s1.fee)
print(s1.loc)

s1.learning()
s1.practice()
'''

# 1.
'''
class empdata:
    company = 'TCS'
    location = "HYD"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print('emp name: ',self.name)
        print('emp salary: ',self.salary)
        print('emp company: ',self.company)
        print('emp location: ',self.location)
e1 = empdata('lucky',30000)
e1.display()

employee = empdata('srinu',30000)
employee.display()
'''
# 2
'''
class myclass:
    def __init__(lucky):
        print('constructor is calling')
    def display(lucky):
        print('method is calling')
m = myclass()
m.display()
'''

    
        
