student_dict = {
    "Gurt": 42,
    "Kentex": 98,
    "Gregory": 62,
    "Tim Cheese": 80,
    "John Pork": 84,
}
print(student_dict)
for student in student_dict:
    print(student + "score is", bool(student_dict[student]) ) 