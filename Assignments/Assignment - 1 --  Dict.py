emps = {
'emp1':{'name':'Sai', 'salary':20000, 'company':['TCS','Capgemini','Infosys'], 'hTown':'Hyd'},
'emp2':{'name':'Nani','salary':30000, 'company':['Wipro','NTH'], 'hTown':'Bangalore'},
'emp3':{'name':'Satya','salary':40000, 'company':['NTH','Infosys','CTS'],'hTown':'Chennai'},
'emp4':{'name':'Rohit','salary':25000, 'company':['Infosys','TCS','Defteam'], 'hTown':'Pune'},
'emp5':{'name':'Mohan','salary':22000, 'company':['NTH','HCL','DeepCompute'], 'hTown':'Hyd'},
'emp6':{'name':'Sanjay','salary':45000, 'company':['Wipro','Infosys','Defteam'], 'hTown':'Mumbai'}
}
     
#1.Write a program to display the salary of Sai?
'''
for i in emps:
    if emps[i]['name']=='Sai':
        print(emps[i]['salary'])
'''
#2.Write a program to display the home town of Nani?
'''     
for i in emps:
    if emps[i]['name'] == 'Nani':
        print(emps[i]['hTown'])
'''       
#3.Write a program to display employee name who is working in Pune?
'''      
for i in emps:
    if emps[i]['hTown']=='Pune':
        print(emps[i]['name'])
'''      
#4.Write a program to display all companies names of Satya?
'''
for i in emps:
    if emps[i]['name']=='Satya':
        print(emps[i]['company'])
'''
#5.Write a program to display all employees names who worked in TCS?
'''
for i in emps:
    if 'TCS' in emps[i]['company']:
        print(emps[i]['name'])

'''
#6.Write a program to display all employees names who did not work in Infosys?
'''
for i in emps:
    if 'Infosys' not in emps[i]['company']:
        print(emps[i]['name'])
'''
#7. Write a program to display all employees names?
'''
for i in emps:
    print(emps[i]['name'])
'''
#8. Write a program to display the sum of all salaries?
'''
l=0
for i in emps:
    l=l+emps[i]['salary']
    print(l)
'''
#9. Write a program to display the latest company of Rohit?
'''
for i in emps:
    if emps[i]['name'] == 'Rohit':
        print(emps[i]['company'][-1])
'''
#10. Write a program to display total companies count of Satya?
'''
for i in emps:
    if emps[i]['name']=='Satya':
        print(len(emps[i]['company']))
'''
#11. Write a program to display the employee name who is working in HCL?
"""
for i in emps:
    if 'HCL' in emps[i]['company']:
        print(emps[i]['name'])
"""
#12. Write a program to display employees names who are working in Hyd?
'''
for i in emps:
    if emps[i]['hTown']=='Hyd':
        print(emps[i]['name'])
'''
#13. Write a program to display all employees whose name starts with 'S' character?
'''
for i in emps:
    if emps[i]['name'].startswith('S'):
        print(emps[i]['name'])
'''
#14. Write a program to display all employees whose name ends with vowel?
'''
for i in emps:
    v=('a','e','i','o','u')
    if emps[i]['name'].endswith(v):
        print(emps[i]['name'])
'''
#15. Write a program to display the employees name who worked only in two companies?
'''
for i in emps:
    if len(emps[i]['company'])==2:
        print(emps[i]['name'])
'''
#16. Write a program to display employee names who worked in DeepCompute?
'''
for i in emps:
    if 'DeepCompute' in emps[i]['company']:
        print(emps[i]['name'])
'''
#17. Write a program to display the salary of Pune employee?
'''
for i in emps:
    if emps[i]['hTown'] == 'Pune':
        print(emps[i]['salary'])
'''
#18. Write a program to display the location of employee who is taking 20000 salary?
'''
for i in emps:
    if emps[i]['salary'] == 20000:
        print(emps[i]['hTown'])
'''
#19. Write a program to display the salaries of Sai and Nani?
'''
for i in emps:
    if emps[i]['name'] in ['Sai','Nani']:
        print(emps[i]['salary'])
'''
#20. Write a program to display the name and salary of Bangalore employee?
'''
for i in emps:
    if 'Bangalore' in emps[i]['hTown']:
        print(emps[i]['name'])
        print(emps[i]['salary'])
'''

