
# This code demonstrates the use of break  statements in loops.
for i in range(100):
    if(i == 34):
        break # This will exit the loop when i is 34
    print(i)

# Using continue to skip an iteration

for i in range(100):
    if(i == 34):
       continue # This will skip the current iteration when i is 34
    print(i)