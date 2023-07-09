india = {
    'andhra': {'capital':'Amaravati','population':5,'cm':'Mr. Jagan', 'districts':26,
                    'language':'Telugu','sex ratio':993/1000,'flower':'Jasmine', 'bird':'Rose-ringed parakeet'},
    'telangana': {'capital':'Hyderabad', 'population': 4, 'cm':'Mr. Chandra Shekar', 'districts':33,
                    'language': 'Telugu','sex ratio':988/1000, 'flower':'Senna auriculata', 'bird':'Indian roller'},
    'odisha': {'capital':'Bhubaneswar', 'population': 4, 'cm': 'Mr. Naveen Patnaik', 'districts':30,
                    'language':'Odia','sex ratio':979/1000, 'flower':'Ashoka', 'bird':'Indian roller'},
    'maharashtra': {'capital': 'Mumbai', 'population':11, 'cm': 'Mr. Eknath Shinde', 'districts':36,
                    'language':'Marathi','sex ratio': 966/1000, 'flower':'Jarul', 'bird':'Yellow-footed green pigeon'},
    'bihar':{'capital':'Patna', 'population':10, 'cm':'Mr. Nitish Kumar','districts':38,
                    'language':'Hindi','sex ratio':1090/1000, 'flower': 'Marigold','bird':'House sparrow'}}

#1. What is the capital of andhra?
print(india['andhra']['capital'])
print([india[i]['capital'] for i in india if 'andhra' in i])

#2. Who is cm of Telangana?
print(india['telangana']['cm'])
print([india[i]['cm'] for i in india if 'telangana' in i])

#3. What is the national flower of maharashtra?
print(india['maharashtra']['flower'])
print([india[i]['flower'] for i in india if 'maharashtra' in i])

#4. What is the national bird of bihar?
print(india['bihar']['bird'])
print([india[i]['bird'] for i in india if i == 'bihar'])

#5. What is the sex ratio of Odisha?
print(india['odisha']['sex ratio'])
print([india[i]['sex ratio'] for i in india if i == 'odisha'])
    
#6. What are the number of districts in Odisha?
print(india['odisha']['districts'])
print([india[i]['districts'] for i in india if i == 'odisha'])

#7. Who is the CM of the state where Bhubaneswar is capital?
print([india[i]['cm'] for i in india if india[i]['capital'] == 'Bhubaneswar' ])

#8. What are the states which has Telugu Language?
print([i for i in india if india[i]['language'] == 'Telugu' ])

#9. What is the national bird of state where cm is Mr. Eknath Shinde?
print([india[i]['bird'] for i in india if india[i]['cm'] == 'Mr. Eknath Shinde' ])

#10. Who is the CM of the state which has more number of districts?
print([india[i]['cm'] for i in india if india[i]['districts'] == max([india[i]['districts'] for i in india])])

#11. What is the state name which has less number of districts?
print([i for i in india if india[i]['districts'] == min([india[i]['districts'] for i in india])])

#12. What are the names of CMs of all the states?
print([india[j]['cm'] for j in india])

#13. What is the capital of state which has less population?
print([india[i]['capital'] for i in india if india[i]['population'] == min([india[i]['population'] for i in india])])

#14. What is the state name which has more sex ratio?
print([i for i in india if india[i]['sex ratio'] == max([india[i]['sex ratio'] for i in india])])

#15. Which state has less population?
print([i for i in india if india[i]['population'] == min([india[i]['population'] for i in india])])

#16. What is the state name which has national bird Indian roller?
print([i for i in india if india[i]['bird'] == 'Indian roller'])

#17. What are the non-Telugu language states?
print([i for i in india if india[i]['language'] != 'Telugu' ])

#18. What is the capital of state which has more population?
print([india[i]['capital'] for i in india if india[i]['population'] == max([india[i]['population'] for i in india])])

#19. Which state has Marigold national flower?
print([i for i in india if india[i]['flower'] == 'Marigold'])


#20. What are the names of states which does not have Ashoka national flower?
print([i for i in india if india[i]['flower'] != 'Ashoka'])

