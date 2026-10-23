#Project 5 — Password Policy Validation Engine
password = input("Enter a sample password: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    else:
        has_special = True
valid = True
if len(password) < 8:
    print("Failed: Minimum 8 characters required")
    valid = False
if not has_upper:
    print("Failed: Add an uppercase letter")
    valid = False
if not has_lower:
    print("Failed: Add a lowercase letter")
    valid = False
if not has_digit:
    print("Failed: Add a digit")
    valid = False
if not has_special:
    print("Failed: Add a special character")
    valid = False
if valid:
    print("Password meets the sample policy")
else:
    print("Password does not meet the policy")