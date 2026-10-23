#Project 3 — Student Performance Trend Analysis
subjects = ["Python", "Mathematics", "English"]
exam1 = [65, 55, 70]
exam2 = [72, 60, 68]
exam3 = [80, 58, 75]
print("Student Performance Analysis")
for i in range(len(subjects)):
    change = exam3[i] - exam1[i]
    print("\nSubject:", subjects[i])
    print("Exam 1:", exam1[i])
    print("Exam 2:", exam2[i])
    print("Exam 3:", exam3[i])
    print("Overall change:", change)
    if change > 0:
        print("Performance improved")
    elif change < 0:
        print("Performance declined")
    else:
        print("No overall change")

    if exam3[i] < 40:
        print("Needs improvement")
weakest = exam3.index(min(exam3))
print("\nWeakest subject:", subjects[weakest])
print("Average in Exam 3:", sum(exam3) / len(exam3))