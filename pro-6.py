#Project 6 — Examination Answer Evaluation
key = ["A", "B", "C", "D", "A"]
answers = ["A", "C", "", "D", "B"]
correct = 0
wrong = 0
unanswered = 0
for i in range(len(key)):
    if answers[i] == "":
        unanswered += 1
    elif answers[i].upper() == key[i]:
        correct += 1
    else:
        wrong += 1
score = correct - (wrong * 0.25)
print("Correct answers:", correct)
print("Wrong answers:", wrong)
print("Unanswered:", unanswered)
print("Final score:", score)