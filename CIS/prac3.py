import os

security_levels = {
    'top secret' : 3,
    'secret' : 2,
    'confidential' : 1,
    'unclassified' : 0
}

print("Enter your security clearance level: ")
for clearance in security_levels.keys():
    print(f"  {clearance}")
user_clearance = input("> ").lower()

if user_clearance not in security_levels.keys():
    print("Invalid security clearance level.")
    exit()

filename = "demo.txt"
with open(filename,'r') as f:
    contents = f.read()

file_clearance = security_levels['secret']

if security_levels[user_clearance] >= file_clearance:
    print("Access granted.")
    print(contents)
else:
    print("Access denied.")