#1.Write a comprehension to fetch all even number from list
'''
lst = [10,11,13,14,9,8]
print([i for i in lst if i%2 == 0])
'''
#2.Write a comprehension to fetch all string values from list
'''
lst = [10,'a',True,'b',False]
print([i for i in lst if type(i) is str])
'''
#3.Write a comprehension to fetch all 5 divisibles from list
'''
lst = [12,15,27,20,5]
print([i for i in lst if i%5 == 0])

'''
#4.Write a comprehension to count total number of  int values in the list
'''
lst = [10,'a',20,True,30,'b',False,40]
print(len([i for i in lst if type(i) is int]))
'''
#5.Write a comprehension to count total number of characters in the list
'''
st='Python language'
print(len([i for i in st]))
'''
#6.Write a comprehension to count total number of words in the string
'''
st = 'python narayana tech house hyd'
print(len([i for i in st.split()]))
'''
#7.Write a comprehension to fetch all vowels from the string
'''
st='Python language'
print([i for i in st if i in 'aeiou'])
'''
#8.Write a comprehension to count total number of vowels
'''
st='Python language'
print(len([i for i in st if i in 'aeiou']))
'''
#9.Write a comprehension to count total number of characters in the list {excluding space}
'''
st = 'python is a simple language'
print(len([i for i in st if i != ' ']))
'''
#10.Write a comprehension to count total number of consonannts in the string
'''
st = 'python language'
print(len([i for i in st if i not in 'aeiou' and i != ' ']))
'''
#11.Write a comprehension to fetch all words which starts with vowels from given string
'''
st = 'python is simple and easy language'
print([i for i in st.split() if i[0] in 'aeiou'])
'''
#12.Write a comprehension to fetch all words which ends with consonnant in the given string?
'''
st='Python is simple and easy language'
print([i for i in st.split() if i[-1] not in 'aeiou'])
'''

#13. Write a comprehension to fetch all words which 'a' two or more then two times?
'''
st='Python is simple and easy language!'
print([i for i in st.split() if i.count('a') >= 2])
'''
#14. Write a comprehension to count number of characters of each word in the string?
'''
st='Python is simple and easy language' 
print([len(i) for i in st.split()])
'''
#15. Write a comprehension to fetch the first and last character from each word in the string?
'''
st='Python is simple and easy language' 
print([i[0]+i[-1] for i in st.split()])
'''
#16. Write a comprehension to fetch all words which contains 'a' character in the string?
'''
st='Python is simple and easy language'
print([i for i in st.split() if i.count('a')])
'''
#17. Write a comprehension to fetch all words which does not contain 'e' character in string?
'''
st='Python is simple and easy language'
print([i for i in st.split() if 'e' not in i])
'''
#18. Write a comprehension to fetch all words which contains only 4 or lessthen 4 characters? 
'''
st='Python is simple and easy language'
print([i for i in st.split() if len(i) <= 4])
'''

#19. Write a comprehension to fetch all words which contain odd number of characters in the st
'''
st='Python is simple and easy language' 
print([i for i in st.split() if len(i)%2 != 0])
'''
#20. Write a comprehension to fetch all words which starts and ends with vowel in the string?
'''
st='Python is number one language'
print([i for i in st.split() if i[0] in 'aeiou' and i[-1] in 'aeiou'])
'''
#21. Write a comprehension to fetch all palindrome words from list?
'''
names = ['madam', 'python', 'dad', 'language', 'eye',"malayalam"] 
print([i for i in names if i == i[-1::-1]])
'''
#22. Write a comprehension to fetch all non-palindrome words from list?
'''
names = ['madam', 'python','dad', 'language', 'eye','malayalam']
print([i for i in names if i != i[-1::-1]])
'''
#23. Write a comprehension to fetch all palindrome words which starts with 'm' character?
'''
names = ['madam', 'python','dad', 'language', 'eye','malayalam']
print([i for i in names if i == i[-1::-1] and i[0] == 'm'])
'''
#24. Write a comprehension to fetch all palindrome words which more then 3 characters?
'''
names = ['madam', 'python', 'dad', 'language', 'eye',"malayalam"] 
print([i for i in names if i == i[-1::-1] and len(i) > 3])
'''
#25. Write a comprehension to longest palindrome word?
'''
names = ['madam', 'python', 'dad', 'language', 'eye',"malayalam"] 
print([j for j in [i for i in names if i == i[-1::-1]]
       if len(j) == max([len(i) for i in names if i == i[-1::-1]])])
'''
