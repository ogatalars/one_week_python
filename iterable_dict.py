test_scores = {
    'Jane':100,
    'Bob': 88,
    'Mary': 99,
    'Tom': 60,
    'Jack': 88,
    'Jill': 99,
    'John': 60,
    'Jeff': 88,
    'Jenny': 99,
}
# .Keys
print(test_scores.keys()) 
# .Values
print(test_scores.values())

for student in test_scores.keys():
    print(student)

for notas in test_scores.values():
    print(notas)
    
total = 0;
for score in test_scores.values():
    total += score 
print(total/len(test_scores))       

for key in test_scores.keys():
    print(key, test_scores[key])
    
# Items 
for item in test_scores.items():
    print(item)    

#Unpacking items
for name, score in test_scores.items():
    print(name, score)    
    
    