#Project 1 — Attendance Recovery Computation
total = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))
if total <= 0 or attended < 0 or attended > total:
    print("Invalid input")
else:
    percentage = attended / total * 100
    print(f"Current attendance: {percentage:.2f}%")
    if percentage >= 75:
        print("You are eligible.")
    else:
        extra = 0
        while attended / total * 100 < 75:
            total += 1
            attended += 1
            extra += 1
        print("Additional classes required:", extra)
        print(f"Final attendance: {attended / total * 100:.2f}%")