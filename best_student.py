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

max_score = 0;
best_student = '';
for student, score in test_scores.items():
    if score > max_score:
        max_score = score
        best_student = student
print(f"Highest score: {max_score} by {best_student}")        