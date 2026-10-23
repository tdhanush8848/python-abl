#Project 9 — Food Waste Monitoring System
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
prepared = [100, 120, 110, 90, 130]
served = [90, 105, 100, 85, 110]
limit = 10
print("Food Waste Report")
for i in range(len(days)):
    leftover = prepared[i] - served[i]

    if prepared[i] <= 0 or leftover < 0:
        print(days[i], ": Invalid data")
        continue
    waste_percentage = leftover / prepared[i] * 100
    print("\nDay:", days[i])
    print("Prepared:", prepared[i])
    print("Served:", served[i])
    print("Leftover:", leftover)
    print("Waste percentage:", round(waste_percentage, 2), "%")
    if waste_percentage > limit:
        print("Warning: Waste exceeds limit")
    else:
        print("Waste is within limit")
total_prepared = sum(prepared)
total_served = sum(served)
total_leftover = total_prepared - total_served
print("\nTotal meals prepared:", total_prepared)
print("Total meals served:", total_served)
print("Total leftover meals:", total_leftover)