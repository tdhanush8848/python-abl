#Project 10 — Energy Conservation Before-and-After Analysis
appliances = ["Fan", "Light", "AC", "Computer"]
before = [30, 20, 100, 40]
after = [24, 12, 75, 32]
savings = []
print("Energy Conservation Report")
for i in range(len(appliances)):
    saved = before[i] - after[i]
    savings.append(saved)

    if before[i] > 0:
        percentage = saved / before[i] * 100
    else:
        percentage = 0
    print("\nAppliance:", appliances[i])
    print("Before:", before[i], "units")
    print("After:", after[i], "units")
    print("Units saved:", saved)
    print("Savings percentage:", round(percentage, 2), "%")
    if saved > 0:
        print("Energy consumption reduced")
    elif saved < 0:
        print("Energy consumption increased")
    else:
        print("No change in consumption")
total_before = sum(before)
total_after = sum(after)
total_saved = total_before - total_after
print("\nTotal before:", total_before, "units")
print("Total after:", total_after, "units")
print("Total energy saved:", total_saved, "units")
best = savings.index(max(savings))
print("Appliance with highest unit savings:", appliances[best])