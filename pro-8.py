#Project 8 — Student Marks Matrix Analysis
subjects = ["Python", "Maths", "English"]
students = ["Ravi", "Priya", "Arun"]
marks = [
    [85, 78, 90],
    [92, 88, 84],
    [70, 65, 75]
]
print("Student Marks Analysis")
for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)
    print("\nStudent:", students[i])
    print("Marks:", marks[i])
    print("Total:", total)
    print("Average:", round(average, 2))
    if average >= 85:
        print("Performance: Excellent")
    elif average >= 70:
        print("Performance: Good")
    else:
        print("Performance: Needs improvement")
print("\nSubject Averages")
for j in range(len(subjects)):
    total = 0
    for i in range(len(students)):
        total += marks[i][j]
    average = total / len(students)
    print(subjects[j], ":", round(average, 2))