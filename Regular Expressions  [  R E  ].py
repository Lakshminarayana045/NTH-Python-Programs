# 1.Write a pattern to match the given mobile number
'''
import re
mobile = input('Enter your mobile number:  ')
m = re.fullmatch('[6-9]\d{9}',mobile)
if m == None:
    print('Not matching')
else:
    print('Matching')
'''
# 2.Write a pattern to check whether the given PAN  number is valid or not
'''
import re
PAN = input('Enter your PAN number: ')
p = re.fullmatch('[A-Z]{5}\d{4}[A-Z]',PAN)
if p == None:
    print('PAN is invalid')
else:
    print('PAN valid')
'''

# 3.Write a pattern to check whether the given vechicle registration number is valid or not
'''
import re
bike=input('Enter your bike Number: ')
b=re.fullmatch('[A-Z]{2}\s\d{2}\s[A-Z]{2}\s\d{4}',bike)
if b == None:
    print('Invalid')
else:
    print('Valid')
'''
# 4.AP 27 BR 6167   TN 04 A 2575    OD 05BR 1529    TS 5 K4587
'''
import re
bike=input('Enter your bike Number: ')
b=re.fullmatch('[A-Z]{2}\s\d{1,2}\s?[A-Z]{1,2}\s{0,1}\d{4}',bike)
if b == None:
    print('Invalid')
else:
    print('Valid')
'''
#================================================================================================================

data = '''Mr. Rakesh is working in TCS Company since 2010  year but Mrs. Sunitha is working in INFOSYS Company since 2015 year only,Mr. Kohli is working in BCCI Company since 2008 year'''

#1.Write a Pattern to fetch all male employes names

import re
emps = re.findall('[Mr. ]{4}[A-Z][a-z]{1,}',data)
print(emps)

import re
print([i for i in re.findall('[Mr. ]{4}[A-Z][a-z]{1,}',data)])

#2.Write a Pattern to fetch all company names
'''
import re
print([i.replace('Company','' ) for i in re.findall('[A-Z]{1,} Company',data)])
'''
#3.write a pattern to fetch employee name who joined in 2010
"""
import re
a=re.findall('[Mrs. ]{4,}[A-Z][a-z]{1,}',data)
b=re.findall('\d{4}',data)
d={}
for i in range(3):
    d[a[i]] = b[i]
for name,year in d.items():
    if year == '2010':
        print(name)


import re
luc = data.split('year'[:-1])
for i in luc:
    if re.findall('\d{4}',i) == ['2010']:
        print(re.findall('[Mrs. ]{4,5}[A-Z][a-z]+',i))
"""
#4.write a pattern to fetch all employees names?
'''
import re
emps=re.findall('[Mrs. ]{4,}[A-Z][a-z]{1,}',data)
print(emps)
print([i for i in re.findall('[Mrs. ]{4,}[A-Z][a-z]{1,}',data)])
'''
#5.write a pattern to fetch all the years?
'''
import re
print(re.findall('\d{4}',data))
'''
#6.write a pattern to fetch the company name of Mrs. Sunita
'''
import re
a=re.findall('[Mrs. ]{4,}[A-Z][a-z]{1,}',data)
b=re.findall('[A-Z]{2,}',data)
d={}
for i in range(3):
    d[a[i]] = b[i]
for ename,cname in d.items():
    if ename == ' Mrs. Sunitha':
        print(cname)

import re
lst = data.split('year')[:-1]
for i in lst:
    if re.findall('[Mrs. ]{4,5}[A-Z][a-z]+',i) == ['Mrs. Sunitha']:
        print(re.findall('[A-Z]{2,}',i))

'''
#7.write a pattern to fetch employees name who is working BCCI company
"""
import re
lst = data.split('year')[:-1]
for i in lst:
    if re.findall('[A-Z]{2,} Company',i) == ['BCCI Company']:
        print(re.findall('[Mrs. ]{4,}[A-Z][a-z]+',i))
        
"""
#8.write a pattern to fetch employees name who has more exp
'''
lst = data.split('year')[:-1]
import re
y = min(re.findall('\d{4}',data))
for i in lst:
    if re.findall('\d{4}',i) == [y]:
        print(re.findall('[Mrs. ]{4}[A-Z][a-z]+',i))
'''
#9.write a pattern to fetch employee name who is not working in INFOSYS
'''
lst = data.split('year')[:-1]
import re
for i in lst:
    if re.findall('[A-Z]{1,} Company',i) != ['INFOSYS Company']:
        print(re.findall('[Mr. ]{4,}[A-Z][a-z]{1,}',i))
'''    
#10.write a pattern to fetch the company name and joining year of Mr. kohli?
'''
lst = data.split('year')[:-1]
import re
for i in lst:
    if re.findall('[Mr. ]{4}[A-Z][a-z]+',i) == ['Mr. Kohli']:
        print(re.findall('[A-Z]{1,} Company',i)+ re.findall('\d{4}',i))
'''
