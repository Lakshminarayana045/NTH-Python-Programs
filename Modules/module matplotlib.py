from matplotlib import pyplot as p

#1.Line plot
'''
branches = ['ECIL','KPHP','AMP',"S.R.Nager",'Uppal']
sales = [30,60,80,50,40]
p.plot(branches,sales)
p.xlabel('Branches')
p.ylabel('Sales')
p.title('Branch wise Sales')
p.show()
'''

#2.Bar Plot
'''
br = ['CSC','EEE','Mech','Civil']
stu = [90,50,100,20]
p.bar(br,stu)
p.xlabel('Branches')
p.ylabel('Students')
p.title('Branch wise Students')
p.show()
'''

#3.Scatter plot
'''
city = ['TS','AP','MP','UP','OD']
buses = [15000,20000,12000,18000,14000]
p.scatter(city,buses)
p.xlabel('State')
p.ylabel('Bus')
p.title('State wise buses')
p.show()
'''

#4.pie plot
'''
slices = [12,25,50,36]
activities = ['Java','PHP','Python','C +']
cols = ['c','g','b','r']
p.pie(slices,labels=activities,colors=cols,startangle=90,shadow= True,explode=(0,0.1,0,0),autopct='%1.1f%%')
p.title('In Ammerpet')
p.show()
'''
#5.Histogram

pg = [22,55,62,45,21,22,34,42,42,4,2]
bi = [0,10,20,30,40,50,60,70,80,90,100]
p.hist(pg, bi, histtype='bar', rwidth=0.5)
p.xlabel('age groups')
p.ylabel('Number of people')
p.title('People age groupes')
p.show()








