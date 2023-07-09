movies = {
'actors':{
'prabhas':{'knownAs':'Darling', 'awards':{'nandi':1, 'cinemaa':1, 'siima':1},'remuneration':100,
           'hits':{'industry':2, 'super':3,'flops':8}, 'age':41, 'height':6.1, 'mStatus':'single','sRate':'35%'},
'mahesh':{'knownAs':'Prince','awards':{'nandi':8, 'cinemaa':3, 'siima':3},'remuneration':50,
          'hits':{'industry':2, 'super':6,'flops':11},'age':46, 'height':6.2, 'mStatus':'married','sRate':'46%'},
'ramcharan':{'knownAs':'Mega Power Star', 'awards':{'nandi':2, 'cinemaa':1, 'siima':1},'remuneration':70,
             'hits':{'industry':3, 'super':1,'flops':5}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'50%'},
'ntr':{'knownAs':'Jr NTR', 'awards':{'nandi':2, 'cinemaa':5, 'siima':3}, 'remuneration':70,
       'hits':{'industry':1, 'super':7,'flops':11}, 'age':36, 'height':5.9, 'mStatus':'married','sRate':'40%'},
'pavan':{'knownAs':'Power Star', 'awards':{'nandi':2, 'cinemaa':2, 'siima':5},'remuneration':50,
         'hits':{'industry':2,'super':7,'flops':16}, 'age':48, 'height':5.9, 'mStatus':'married','sRate':'37%'},},
'actress':{
'tamanna':{'knownAs':'Milky Beauty', 'awards':{'nandi':0, 'cinemaa':1, 'siima':1},'remuneration':10,
           'hits':{'industry':1, 'super':7,'flops':11}, 'age':28, 'height':5.5, 'mStatus':'single','sRate':'40%'},
'rashmika':{'knownAs':'Butter Milky Beauty', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},'remuneration':12,
            'hits':{'industry':0, 'super':4,'flops':2}, 'age':36, 'height':5.7, 'mStatus':'single','sRate':'30%'},
'saipallavi':{'knownAs':'Laughing Queen', 'awards':{'nandi':0, 'cinemaa':0, 'siima':2},'remuneration':8,
              'hits':{'industry':0, 'super':3,'flops':0}, 'age':28, 'height':5.6,'mStatus':'single','sRate':'60%'},
'samantha':{'knownAs':'Sam', 'awards':{'nandi':2, 'cinemaa':3, 'siima':5},'remuneration':15,
            'hits':{'industry':3, 'super':7,'flops':4}, 'age':33, 'height':5.9,'mStatus':'married','sRate':'70%'},
'kajal':{'knownAs':'Kaj', 'awards':{'nandi':0, 'cinemaa':2, 'siima':2},'remuneration':12,
         'hits':{'industry':1, 'super':6,'flops':8}, 'age':35, 'height':6.0, 'mStatus':'married','sRate':'60%'},}}

#1. Write a program to display all actors names
'''
for i in movies['actors']:
    print(i)
    
print([i for i in movies['actors']])  
'''
#2. Write a program to display all actress names
'''
for i in movies['actress']:
    print(i)
print([i for i in movies['actress']])
'''
#3. Who is Darling?
'''
for i in movies['actors']:
    if 'Darling' in movies['actors'][i]['knownAs']:
        print(i)
print([i for i in movies['actors'] if 'Darling' in movies['actors'][i]['knownAs']])
'''
#4. What are the total number of Nandi Awards won by actors?
'''
m=[]
for i in movies['actors']:
    m.append(movies['actors'][i]['awards']['nandi'])
print(sum(m))
print(m)
'''
#5. What is the name of Prince?
'''
for i in movies['actors']:
    if 'Prince' in movies['actors'][i]['knownAs']:
        print(i)
print([i for i in movies['actors'] if 'Prince' in movies['actors'][i]['knownAs']])        
'''        
#6. What are the total number of awards own by Ram Charan?
'''
for i in  movies['actors']:
    if (i) == 'ramcharan':
        print(sum(movies['actors'][i]['awards'].values()))
'''        
#7. Which actor won more number of Nandi Awards?
'''
lst=[]
for i in movies['actors']:
    lst.append(movies['actors'][i]['awards']['nandi'])
for i in movies['actors']:
    if max(lst) == movies['actors'][i]['awards']['nandi']:
        print(i)
print([i
       for i in movies['actors']
       if movies['actors'][i]['awards']['nandi'] ==
       max([movies['actors'][i]['awards']['nandi'] for i in movies['actors']])])
'''
#8. What is the success rate of Prince?
'''
for i in movies['actors']:
    if 'Prince' in movies['actors'][i]['knownAs']:
        print(movies['actors'][i]['sRate'])

print([movies['actors'][i]['sRate'] for i in movies['actors'] if 'Prince' in movies['actors'][i]['knownAs']])
'''
#9. Which artist has more number of Hits?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['hits']['industry']+movies[i][j]['hits']['super'])
for i in movies:
    for j in movies[i]:
        if max(lst) == movies[i][j]['hits']['industry']+movies[i][j]['hits']['super']:
            print(j)
            # or

lst=[]            
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['hits']['industry']+movies[i][j]['hits']['super'])
    for j in movies[i]:
        if max(lst) == movies[i][j]['hits']['industry']+movies[i][j]['hits']['super']:
            print(j)
'''
#10. Who is Milky Beauty?
'''
for i in movies['actress']:
    if 'Milky Beauty' == movies['actress'][i]['knownAs']:
        print(i)
print([i for i in movies['actress'] if 'Milky Beauty' == movies['actress'][i]['knownAs']])
'''                                                             
#11. What is the nick name of Rashmika?
'''
for i in movies['actress']:
    if 'rashmika' in i:
        print(movies['actress'][i]['knownAs'])
    
print([movies['actress'][i]['knownAs']for i in movies['actress'] if 'rashmika' in i])
'''
#12. What are actress names who did not win at least one Nandi Award?
'''
for i in movies['actress']:
    if movies['actress'][i]['awards']['nandi']==0:
        print(i)
print([i for i in movies['actress'] if movies['actress'][i]['awards']['nandi']==0])
'''
#13. What are the total number of SIIMA awards won by all artists?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        if 'siima' in movies[i][j]['awards']:
            lst.append(movies[i][j]['awards']['siima'])
print(sum(lst))
'''
#14. What is the artist name who has more success rate?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['sRate'])
for i in movies:
    for j in movies[i]:
        if max(lst)in movies[i][j]['sRate']:
            print(j)
'''
#15. What is the age of actor who has more super hit movies?
'''
lst=[]
for i in movies['actors']:
    lst.append(movies['actors'][i]['hits']['super'])
for i in movies['actors']:
    if str(max(lst)) in str(movies['actors'][i]['hits']['super']):
        print(i)
'''
#16. What is the actress name who is married?
'''
for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='married':
        print(i)
print([i for i in movies['actress'] if movies['actress'][i]['mStatus']=='married'])
'''
#17. Who is the tallest actress?
'''
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['height'])
for i in movies['actress']:
    if str(max(lst)) in str(movies['actress'][i]['height']):
        print(i)
'''
#18. Who is the Youngest artist?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['age'])
for i in movies:
    for j in movies[i]:
        if str(min(lst))in str(movies[i][j]['age']):
            print(j)
'''
#19. Who are unmarried actress?
'''
for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='single':
        print(i)
print([i for i in movies['actress'] if movies['actress'][i]['mStatus']=='single'])
'''
#20. Who is smallest actress?
'''
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['age'])
for i in movies['actress']:
    if str(min(lst)) in str(movies['actress'][i]['age']):
        print(i)
'''
#21. Which actress has more Flops?
'''
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['hits']['flops'])
for i in movies['actress']:
    if str(max(lst)) in str(movies['actress'][i]['hits']['flops']):
        print(i)
'''
#22. What is the age of butter milky beauty?
'''
for i in movies['actress']:
    if 'Butter Milky Beauty' in movies['actress'][i]['knownAs']:
        print(movies['actress'][i]['age'])
'''
#23. What are the total number of flops of all actress?
'''
lst=[]
for i in movies['actress']:
        if 'flops' in movies['actress'][i]['hits']:
            lst.append(movies['actress'][i]['hits']['flops'])
print(sum(lst))
'''
#24. What are the ages of Sam and Kaj?
'''
for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Sam':
        print(movies['actress'][i]['age'])
    if movies['actress'][i]['knownAs']=='Kaj':
        print(movies['actress'][i]['age'])
'''          
#25. Which actress own highest total number of Awards?
'''
lst=[]
for i in movies['actress']:
 lst.append(movies['actress'][i]['awards']['nandi']+movies['actress'][i]['awards']['cinemaa']+movies['actress'][i]['awards']['siima'])  
for i in movies['actress']:
    if movies['actress'][i]['awards']['nandi']+movies['actress'][i]['awards']['cinemaa']+movies['actress'][i]['awards']['siima']==max(lst):
        print(i)
'''        
#26. Who is the tallest artist?
'''
lst=[]
for i in movies:
    for j in movies[i]:        
            lst.append(movies[i][j]['height'])
for i in movies:
    for j in movies[i]:
        if str(max(lst))in str(movies[i][j]['height']):
            print(j)
'''
#27. What are the total number of Industry hits of who has more Success Rate?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['sRate'])
for i in movies:
    for j in movies[i]:
        if str(max(lst)) in str(movies[i][j]['sRate']):
            print(movies[i][j]['hits']['industry'])
'''
#28. What is the success rate of youngest actress?
'''
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['sRate'])
for i in movies['actress']:
    if str(min(lst))in movies['actress'][i]['sRate']:        
        print(i)
'''        
#29. Who is youngest married actress?
'''
lst=[]
for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='married':
        lst.append(movies['actress'][i]['age'])
for i in movies['actress']:
    if str(min(lst))in str(movies['actress'][i]['age']):
        print(i)
'''           
#30. Who is oldest unmarried actor?
'''
lst=[]
for i in movies['actors']:
    if movies['actors'][i]['mStatus']=='single':
        lst.append(movies['actors'][i]['age'])
for i in movies['actors']:
    if str(max(lst)) in str(movies['actors'][i]['age']):
        print(i)
'''
#31. Who are the high successful actor and actress?
'''
lst=[]
for i in movies:
    for j in movies[i]:
            lst.append(movies[i][j]['sRate'])
for i in movies:
    for j in movies[i]:
        if str(max(lst))in str(movies[i][j]['sRate']):
            print(j)
'''          
#32. Totally how many unmarried artists are acting in movies?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        if movies[i][j]['mStatus']=='single':
            lst.append(j)
print(len(lst))
'''
#33. Which actress is having more industry hit movies?
'''
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['hits']['industry'])
for i in movies['actress']:
    if str(max(lst)) in str(movies['actress'][i]['hits']['industry']):
        print(i)
'''
#34. Which actress does not have atleast one industry hit also?
'''
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['hits']['industry'])
for i in movies['actress']:
    if str(min(lst)) in str(movies['actress'][i]['hits']['industry']):
        print(i)
'''
#35. What are the total number of industry and super hits of tallest actress?
'''
s=0
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['height'])
for i in movies['actress']:
    if str(max(lst)) in str(movies['actress'][i]['height']):
        s=s+movies['actress'][i]['hits']['industry']+movies['actress'][i]['hits']['super']
print(s)
'''
#36. Which actress is having lengthiest nick name?

lst=[]
for i in movies['actress']:
    lst.append(len(movies['actress'][i]['knownAs']))
for i in movies['actress']:
    if str(max(lst)) in  str(len(movies['actress'][i]['knownAs'])):
       print(i,len(movies['actress'][i]['knownAs']))
        
#37. Who are the youngest unmarried artist?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        if movies[i][j]['mStatus']=='single':
            lst.append(movies[i][j]['age'])
for i in movies:
    for j in movies[i]:
            if str(min(lst)) in str(movies[i][j]['age']):
                       print(j)
'''                       
#38. What are the total number of Industry hits and Super Hits of the actress who got more SIIMA awards?
'''
s=0
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['awards']['siima'])
for i in movies['actress']:
    if str(max(lst)) in str(movies['actress'][i]['awards']['siima']):
        s=s+movies['actress'][i]['hits']['industry']+movies['actress'][i]['hits']['super']
print(s)
'''
#39. What are the ages of Darling and Milky Beauty?
'''
for i in movies['actors']:
    if movies['actors'][i]['knownAs']=='Darling':
        
        print(movies['actors'][i]['age'])
for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Milky Beauty':
              print(movies['actress'][i]['age'])
'''              
#40. What are names of actors whose nick name contains star?       
'''
for i in movies['actors']:
    lst=movies['actors'][i]['knownAs']
    if 'Star' in lst:
        print(i)
'''
#41. What is the total remuneration of all actors?
'''
s=0
for i in movies['actors']:
    s=s+movies['actors'][i]['remuneration']
print(s)
'''
#42. What is the remuneration of an actor who has more flops?
'''
lst=[]
for i in movies['actors']:
    lst.append(movies['actors'][i]['hits']['flops'])
for i in movies['actors']:
    if str(max(lst)) in str(movies['actors'][i]['hits']['flops']):
        print(movies['actors'][i]['remuneration'])
'''
#43. What is the highest remuneration of an unmarried actress?
'''
for i in movies['actress']:
    if movies['actress'][i]['mStatus']=='single':
        print(max([movies['actress'][i]['remuneration']]))
'''
'''
print(max([movies['actress'][i]['remuneration']
           for i in movies['actress']
           if movies['actress'][i]['mStatus']=='single']))
'''
#44. What are the names of artists who has more remuneration?
'''
lst=[]
for i in movies:
    for j in movies[i]:
        lst.append(movies[i][j]['remuneration'])
for i in movies:
    for j in movies[i]:
        if str(max(lst)) in str(movies[i][j]['remuneration']):
            print(j)
'''            
#45. What is the remuneration of high successful Actress?
'''
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['sRate'])
for i in movies['actress']:
    if str(max(lst)) in str(movies['actress'][i]['sRate']):
        print(movies['actress'][i]['remuneration'])
'''
#46. What is the remuneration of actress who has more industry hits?
'''
lst=[]
for i in movies['actress']:
    lst.append(movies['actress'][i]['hits']['industry'])
for i in movies['actress']:
    if str(max(lst)) in str(movies['actress'][i]['hits']['industry']):
        print(movies['actress'][i]['remuneration'])
'''
#47. What are the ages of an actors whose remuneration is more then 90 crores?
'''
for i in movies['actors']:
    if movies['actors'][i]['remuneration']>90:
        print([movies['actors'][i]['age']])
'''        
#48. What are the total number of industry hits of both Prince and Butter Milky Beauty?
'''
for i in movies['actors']:
    if movies['actors'][i]['knownAs']=='Prince':
        print(movies['actors'][i]['hits']['industry'])
for i in movies['actress']:
    if movies['actress'][i]['knownAs']=='Butter Milky Beauty':
        print(movies['actress'][i]['hits']['industry'])
'''
#49. What is the age of Laughing Queen?
'''
for i in movies['actress']:
    if 'Laughing Queen' in movies['actress'][i]['knownAs']:
        print(movies['actress'][i]['age'])
'''        
#50. What are the total number of awards won by an actor who has less successful rate?
'''
lst=[]
for i in movies['actors']:
    lst.append(movies['actors'][i]['sRate'])
for i in movies['actors']:
    if min(lst) in movies['actors'][i]['sRate']:
        print(movies['actors'][i]['awards']['nandi']+
              movies['actors'][i]['awards']['cinemaa']+
              movies['actors'][i]['awards']['siima'])
        
'''
#====================================================   OR  ==========================================================================


#1. Write a program to display all actors names?
'''
a=movies["actors"]
for i in a:
    print(i)
'''
#2. Write a program to display all actress names?
'''
a=movies["actress"]
for i in a:
    print(i)
'''
#3 Who is Darling?
'''
a=movies["actors"]
for i in a:
    if a[i]["knownAs"]=="Darling":
        print(i)
'''
'''
for i in movies:
    for j in movies[i]:
        if movies[i][j]["knownAs"] == "Darling":
            print(j)
'''           
#4 What are the total number of Nandi Awards won by actors?
'''
a=movies["actors"]
l=[]
for i in a:
    l.append(a[i]["awards"]["nandi"])
print(sum(l))
''' 
#5 What is the name of Prince?
'''
a=movies["actors"]
for i in a:
    if a[i]["knownAs"]=="Prince":
        print(i)
'''
#6 What are the total number of awards own by Ram Charan?
'''
v=[]
a=movies["actors"]
for i in a:
    if i=="ramcharan":
        v.append(a[i]["awards"]["nandi"]+a[i]["awards"]["cinemaa"]+a[i]["awards"]["siima"])
print(sum(v))
'''    
#7 Which actor won more number of Nandi Awards?
'''
a=movies["actors"]
h=[]
for i in a:
    h.append(a[i]["awards"]["nandi"])
s=max(h)
for j in a:
    if s==a[j]["awards"]["nandi"]:
        print(j)
'''
#8 What is the success rate of Prince?
'''
a=movies["actors"]
for i in a:
    if a[i]["knownAs"]=="Prince":
        print(a[i]['sRate'])
'''
#9 Which artist has more number of Hits?
'''
a=movies["actors"]
s=[]
for i in a:
    s.append(a[i]["hits"]["industry"]+a[i]["hits"]["super"])
x=max(s)
for j in a:
   if x==a[j]["hits"]["industry"]+a[j]["hits"]["super"]:   
        b=movies["actress"]
for c in b:
    s.append(b[c]["hits"]["industry"]+b[c]["hits"]["super"])
e=max(s)
for d in b:
    if e==b[d]["hits"]["industry"]+b[d]["hits"]["super"]:
        print(j,d)
'''
#10 Who is Milky Beauty?
'''
a=movies["actress"]
for i in a:
    if a[i]["knownAs"]=="Milky Beauty":
        print(i)
'''
#11 What is the nick name of Rashmika?
'''
a=movies["actress"]
for i in a:
    if i=="rashmika":
        print(a[i]["knownAs"])
'''
#12. What are actress names who did not win at least one Nandi Award?
'''
a=movies["actress"]
for i in a:
    if a[i]["awards"]["nandi"]==0:
        print(i)
'''
#13 What are the total number of SIIMA awards won by all artists?
'''
r=[]
a=movies["actress"]
for i in a:
    r.append(a[i]["awards"]["siima"])
x=sum(r)
b=movies["actress"]
c=[]
for j in b:
    c.append(b[j]["awards"]["siima"])
y=sum(c)
print(x+y)
'''
#**14 What is the artist name who has more success rate?
'''
f=[]
a=movies["actors"]
for i in a:
    f.append(a[i]["sRate"])
g=max(f)
for j in a:
    if g==a[j]["sRate"]:
        print(j)
r=[]
b=movies["actress"]
for h in b:
    r.append(b[h]["sRate"])
for q in b:
    if b[q]["sRate"]==(max(r)):
        print(j,q)
'''
#15 What is the age of actor who has more super hit movies?
'''
a=movies["actors"]
k=[]
for i in a:
    k.append(a[i]["hits"]["super"])
for j in a:
    if a[j]["hits"]["super"]==max(k):
        print(a[j]["age"])
'''
#16 What is the actress name who is married?
'''
a=movies["actress"]
for i in a:
    if a[i]["mStatus"]=="married":
        print(i)
'''
#17 Who is the tallest actress?
'''
a=movies["actress"]
y=[]
for i in a:
    y.append(a[i]["height"])
for j in a:
    if a[j]["height"]==max(y):
        print(j)
'''
#18 Who is the Youngest artist?
'''
u=[]
a=movies["actors"]
for i in a:
    u.append(a[i]["age"])
for j in a:
    if a[j]["age"]==min(u):
        print(j)
v=[]
b=movies["actress"]
for g in b:
    v.append(b[g]["age"])
for k in b:
    if b[k]["age"]==min(v):
        print(k)
'''
#19 Who are unmarried actress?
'''
a=movies["actress"]
for i in a:
    if a[i]["mStatus"]=="single":
        print(i)
'''
#20 Who is smallest actress?
'''
a=movies["actress"]
n=[]
for i in a:
    n.append(a[i]["height"])
for j in a:
    if a[j]["height"]==min(n):
        print(j)
'''
#21 Which actress has more Flops?
'''
a=movies["actress"]
y=[]
for i in a:
    y.append(a[i]["hits"]["flops"])
for j in a:
    if a[j]["hits"]["flops"]==max(y):
        print(j)
'''
#22 What is the age of butter milky beauty?
'''
a=movies["actress"]
for i in a:
    if a[i]["knownAs"]=="Butter Milky Beauty":
        print(a[i]["age"])
'''
#23 What are the total number of flops of all actress?
'''
a=movies["actress"]
l=[]
for i in a:
    l.append(a[i]["hits"]["flops"])
print(sum(l))
'''
#24 What are the ages of Sam and Kaj?
'''
a=movies["actress"]
for i in a:
    if i=="samantha" or i=="kajal":
        print(a[i]["age"])
'''
#25 Which actress own highest total number of Awards?
'''
b=[]
a=movies["actress"]
for i in a:
    b.append(a[i]["awards"]["nandi"]+a[i]["awards"]["cinemaa"]+a[i]["awards"]["siima"])
for j in a:
    if a[j]["awards"]["nandi"]+a[j]["awards"]["cinemaa"]+a[j]["awards"]["siima"]==max(b):
        print(j)
'''
#26 Who is the tallest artist?
'''
a=movies["actress"]
x=[]
for i in a:
    x.append(a[i]["height"])
for j in a:
    if a[j]["height"]==max(x):
        c=movies["actors"]
m=[]
for k in c:
    m.append(c[k]['height'])
for n in c:
    if c[n]['height']==max(m):
        print(j,n)
'''
#27 What are the total number of Industry hits of who has more Success Rate?
'''
a=movies["actors"]
d=[]
for i in a:
    d.append(a[i]["sRate"])
for j in a:
    if a[j]["sRate"]==max(d):
        print(a[j]["hits"]["industry"])
b=movies["actress"]
for k in b:
    d.append(b[k]["sRate"])
for l in b:
    if b[l]["sRate"]==max(d):
        print(b[l]["hits"]["industry"])
'''
#28 What is the success rate of youngest actress?
'''
a=movies["actress"]
f=[]
for i in a:
    f.append(a[i]["age"])
for j in a:
    if a[j]["age"]==min(f):
        print(a[j]["sRate"])
'''
#29 Who is youngest married actress?
'''
v=[]
a=movies["actress"]
for i in a:
    if a[i]["mStatus"]=="married":
        v.append(a[i]["age"])
for j in a:
    if a[j]["age"]==min(v):
        print(j)
'''
#30 Who is oldest unmarried actor?
'''
r=[]
a=movies["actors"]
for i in a:
    if a[i]["mStatus"]=="single":
        r.append(a[i]["age"])
for j in a:
    if a[j]["age"]==max(r):
        print(j)
'''
#31 Who are the high successful actor and actress?
'''
g=[]
a=movies["actors"]
for i in a:
    g.append(a[i]["sRate"])
for j in a:
    if a[j]["sRate"]==max(g):
        print(j)
b=movies["actress"]
for k in b:
    g.append(b[k]["sRate"])
for l in b:
    if b[l]["sRate"]==max(g):
        print(l)
'''
#32 Totally how many unmarried artists are acting in movies?
'''
c=0
a=movies["actors"]
for i in a:
    if a[i]["mStatus"]=="single":
        c+=1
b=movies["actress"]
for j in b:
    if b[j]["mStatus"]=="single":
        c+=1
print(c)
'''
#33 Which actress is having more industry hit movies?
'''
t=[]
a=movies["actress"]
for i in a:
    t.append(a[i]["hits"]["industry"])
for j in a:
    if a[j]["hits"]["industry"]==max(t):
        print(j)
'''
#34 Which actress does not have atleast one industry hit also?
'''
a=movies["actress"]
for i in a:
    if a[i]["hits"]["industry"]==0:
        print(i)
'''
#35 What are the total number of industry and super hits of tallest actress?
'''
c=[]
a=movies["actress"]
for i in a:
    c.append(a[i]["height"])
for j in a:
    if a[j]["height"]==max(c):
        #print(j)
        print(a[j]["hits"]["industry"]+a[j]["hits"]["super"])
'''
#***36 Which actress is having lengthiest nick name?
'''
y=[]
a=movies["actress"]
for i in a:
    y.append(a[i]["knownAs"])
for j in a:
    s=sorted👍
    if a[j]["knownAs"]==s[0]:
        print(j)
'''
#37 Who are the youngest unmarried artist?
'''
k=[]
a=movies["actors"]
for i in a:
    if a[i]["mStatus"]=="single":
        k.append(a[i]["age"])
for j in a:
    if a[j]["age"]==min(k):
        print(j)
b=movies["actress"]
for h in b:
    if b[h]["mStatus"]=="single":
        k.append(b[h]["age"])
for g in b:
    if b[g]["age"]==min(k):
        print(g)
'''
#38 What are the total number of Industry hits and Super Hits of the actress who got more SIIMA awards?
'''
l=[]
a=movies["actress"]
for i in a:
    l.append(a[i]["awards"]["siima"])
for j in a:
    if a[j]["awards"]["siima"]==max(l):
        print(j)
        print(a[j]["hits"]["industry"]+a[j]["hits"]["super"])
'''
#39 What are the ages of Darling and Milky Beauty?
'''
a=movies["actors"]
for i in a:
    if a[i]["knownAs"]=="Darling":
        print(a[i]["age"])
b=movies["actress"]
for j in b:
    if b[j]["knownAs"]=="Milky Beauty":
        print(b[j]["age"])
'''
#40 What are names of actors whose nick name contains star?
'''
a=movies["actors"]
for i in a:
    if "Star" in a[i]["knownAs"]:
        print(i)
'''
#41 What is the total remuneration of all actors?
'''
p=[]
a=movies["actors"]
for i in a:
    p.append(a[i]["remuneration"])
print(sum(p))
'''
#42 What is the remuneration of an actor who has more flops?
'''
d=[]
a=movies["actors"]
for i in a:
    d.append(a[i]["hits"]["flops"])
for j in a:
    if a[j]["hits"]["flops"]==max(d):
        print(j)
        print(a[j]["remuneration"])
'''
#43 What is the highest remuneration of an unmarried actress?
'''
k=[]
a=movies["actress"]
for i in a:
    if a[i]["mStatus"]=="single":
        k.append(a[i]["remuneration"])
print(max(k))
print(i)
'''
#44 What are the names of artists who has more remuneration?
'''
u=[]
a=movies["actors"]
for i in a:
    u.append(a[i]["remuneration"])
for j in a:
    if a[j]["remuneration"]==max(u):
        print(j)
b=movies["actress"]
t=[]
for k in b:
    t.append(b[k]["remuneration"])
for l in b:
    if b[l]["remuneration"]==max(t):
        print(l)
'''
#45 What is the remuneration of high successful Actress?
'''
e=[]
a=movies["actress"]
for i in a:
    e.append(a[i]["sRate"])
for j in a:
    if a[j]["sRate"]==max(e):
        print(a[j]["remuneration"])
'''
#46 What is the remuneration of actress who has more industry hits?
'''
s=[]
a=movies["actress"]
for i in a:
    s.append(a[i]["hits"]["industry"])
for j in a:
    if a[j]["hits"]["industry"]==max(s):
        print(a[j]["remuneration"])
'''
#47 What are the ages of an actors whose remuneration is more then 90 crores?
'''
m=[]
a=movies["actors"]
for i in  a:
    if a[i]["remuneration"]>90:
        print(a[i]["age"])
'''
#48 What are the total number of industry hits of both Prince and Butter Milky Beauty?
'''
y=[]
a=movies["actors"]
for i in a:
    if a[i]["knownAs"]=="Prince":
        y.append(a[i]["hits"]["industry"])
print(sum(y))
b=movies["actress"]
f=[]
for j in b:
    if b[j]["knownAs"]=="Butter Milky Beauty":
        f.append(b[j]["hits"]["industry"])
print(sum(f))
'''
'''
a=movies["actors"]
for i in a:
    if a[i]["knownAs"]=="Prince":
        b=movies["actress"]
for j in b:
    if b[j]["knownAs"]=="Butter Milky Beauty":
        print(a[i]["hits"]["industry"]+b[j]["hits"]["industry"])
'''
#49 What is the age of Laughing Queen?
'''
a=movies["actress"]
for i in a:
    if a[i]["knownAs"]=="Laughing Queen":
        print(a[i]["age"])
'''
#50 What are the total number of awards won by an actor who has less successful rate?
'''
b=[]
a=movies["actors"]
for i in a:
    b.append(a[i]["sRate"])
for j in a:
    if a[j]["sRate"]==min(b):
        print(a[j]["awards"]["nandi"]+a[j]["awards"]["cinemaa"]+a[j]["awards"]["siima"])
        print(j)
'''

                        
