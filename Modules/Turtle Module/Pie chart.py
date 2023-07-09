"""
p = eval(input('enter any word: '))
d={}
if type(p) is str:
    if p == p[-1::-1] :
        d[p] = len(p)
        print(d)
    else:
        print('non  - palindrom word')
else:
    print('enter only word')


"""

'''
a =['a','b','c']+
B=['A','B',"C"]
d={}
for i in range(3):
    d[a[i]]=B[i]
print(d)
'''
lst = [10,45,30,67,23,43]
l1 = lst[0]
for i in lst:
    if i>l1:
        l1 = i
print(l1)

