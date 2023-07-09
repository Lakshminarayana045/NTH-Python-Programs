#==============================Set 1 =====================================

#1. Write comprehension to fetch all words which name has Mr initial?
'''
names = ['Mrs Kavya', 'Mr. Satya', 'Mr. Rajesh', 'Ms. Rajani']
print([i for i in names if i.startswith('Mr.')])
'''
#2. Write comprehension to count total number of characters (excluding space)?
'''
st = 'Python Narayana Tech House Hyderabada'
print(len([i for i in st if i != ' ']))
'''
#3. Write a comprehension to fetch all palindrome words from list?
'''
names = ['madam', 'python','dad','language','eye','malayalam']
print([i for i in names if i == i[-1::-1]])
'''
#4. Write a comprehension to longest palindrome word?
'''
names = ['madam', 'python','dad','language','eye','malayalam']
l=[]
b=[]
for i in names:
    if i == i[-1::-1]:
        l.append(i)
        b.append(len(i))
for i in l:
    if len(i) == max(b):
        print(i)

print ( [j for j in [i for i in names if i==i[-1::-1]]
         if len(j)==max([len(i) for i in names if i==i[-1::-1]])])
'''

#5. Write a comprehension to fetch the first and last character from each word in the string?
'''
st = 'Python is simple and easy language'.split()
k=[]
for i in st:
    k.append(i[0]+i[-1])
print(k)
print([i[0]+i[-1] for i in st])
'''
#6. Write a comprehension to fetch all words which contains 'a' character in the string?
'''
st = 'Python is simple and easy language'.split()
print([i for i in st if 'a' in i])
'''
#7. Write a comprehension to fetch all words which starts and ends with vowel in the string?
'''
st = 'Python is simple and easy language'.split()
print([i for i in st if i [0] in 'aeiou' and i[-1] in 'aeiou' ])

for i in st:
    if i[-1] in 'aeiou' :
        print(i)
'''
#=================================== Set 2==============================

#1. Write comprehension to fetch all words which name has Player?
'''
names = ['Sai Palyer', 'Nani Teacher', 'Satya Software', 'Kohli Player']
print([i for i in names if 'Player' in i])
'''
#2. Write comprehension to count total number of characters(excluding space)?.
'''
st = 'Python Narayana Tech House Hyderabada'
print(len([i for i in st if i != ' ']))
'''
#3. Write a comprehension to fetch all non-palindrome words from list?
'''
names = ['madam', 'python','dad','language','eye','malayalam']
print([i for i in names if i != i[-1::-1]])
'''
#4. Write a comprehension to shortest palindrome word?
'''
names = ['madam', 'python','dad','language','eye','malayalam']
print ( [j for j in [i for i in names if i==i[-1::-1]]
         if len(j)==min([len(i) for i in names if i==i[-1::-1]])])
'''         
#5. Write a comprehension to fetch all chars from each word except first and last char of word?
'''
st = 'Python is simple and easy language'.split()
print([i[1:-1] for i in st])
'''
#6. Write a comprehension to fetch all words which contains 'a' character in the string?
'''
st = 'Python is simple and easy language'.split()
print([i for i in st if 'a' in i])
'''
#7. Write a comprehension to fetch all words which starts and ends with vowel in the string?
'''
st = 'Python is simple and easy language'
print([i for i in st.split() if i [0] in 'aeiou' and i[-1] in 'aeiou' ])

'''
#=============================Set 3==========================================

#1. Write comprehension to fetch all words which name has Mr initial?
'''
names = ['Mrs Kavya', 'Mr. Satya', 'Mr. Rajesh', 'Ms. Rajani']
print([i for i in names if i.startswith('Mr.')])
'''
#2. Write comprehension to count total number of characters (excluding space)?
'''
st = 'Python Narayana Tech House Hyderabada'
print(len([i for i in st if i != ' ']))
'''

#3. Write comprehension to fetch all names who are not Softwares?
'''
names = ['Sai Palyer', 'Nani Teacher', 'Satya Software', 'Kohli Player']
print([i for i in names if 'Software' not in i])
'''

#4. Write comprehension to count total number of characters(including space)?.
'''
st = 'Python Narayana Tech House Hyderabada'
print(len([i for i in st]))
'''
#5. Write a comprehension to fetch all palindrome words from list?
'''
names = ['madam', 'python','dad','language','eye','malayalam']
print([i for i in names if i == i[-1::-1]])
'''
#6. Write a comprehension to shortest palindrome word?
'''
names = ['madam', 'python','dad','language','eye','malayalam']
print ( [j for j in [i for i in names if i==i[-1::-1]]
         if len(j)==min([len(i) for i in names if i==i[-1::-1]])])
'''
#7. Write a comprehension to fetch all words which starts and ends with vowel in the string?
'''
st = 'Python is simple and easy language'.split()
print([i for i in st if i [0] in 'aeiou' and i[-1] in 'aeiou' ])
'''

