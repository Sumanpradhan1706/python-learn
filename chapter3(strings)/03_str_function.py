name ="suman"
print(len(name))
print(name.endswith("an"))
print(name.startswith("su"))
print(name.capitalize())

# upper() – Converts to UPPERCASE

print(name.upper())   # Output: SUMAN
# lower() – Converts to lowercase

print(name.lower())   # Output: suman
# title() – Capitalizes first letter of each word

name2 = "suman pradhan"
print(name2.title())  # Output: Suman Pradhan
# strip() – Removes spaces from both ends

name3 = "  suman  "
print(name3.strip())  # Output: "suman"
# replace(old, new) – Replaces parts of the string

print(name.replace("su", "ra"))  # Output: raman
# find() – Finds first index of a substring

print(name.find("ma"))  # Output: 2
# count() – Counts how many times a substring appears

print(name.count("a"))  # Output: 1
# isalpha() – Checks if all characters are letters

print(name.isalpha())  # Output: True
# isdigit() – Checks if all characters are digits

age = "25"
print(age.isdigit())  # Output: True
#split() – Splits a string into a list

full_name = "suman pradhan"
print(full_name.split())  # Output: ['suman', 'pradhan']
# join() – Joins a list into a string

words = ['Python', 'is', 'fun']
print(" ".join(words))  # Output: Python is fun
# swapcase() – Swaps case: upper → lower, lower → upper

print(name.swapcase())  # Output: SUMAN