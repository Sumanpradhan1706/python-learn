friends = ["Apple","orange","Mango","Banana"]
print(friends)

friends.append("Lichi")  # Adding a new element to the end of the list
print(friends)

l1 = [1,2,3,4,5]
l1.sort()  # Sorting the list in ascending order
print(l1)
l1.reverse()  # Reversing the list
print(l1)
l1.insert(2, 33333) # Inserting an element at index 2
print(l1)

value = l1.pop(3)
print("Popped value:", value)  # Output the popped value
print(l1)  # Output the modified list after popping an element