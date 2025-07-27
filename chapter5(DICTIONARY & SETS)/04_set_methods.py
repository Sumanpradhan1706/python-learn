s ={1,5,32,54,5,5,5,}

print(s, type(s))

s.add(556)
print(s,type(s))


s = {1, 2}
s.update([3, 4])
print(s)  # {1, 2, 3, 4}


s = {1, 2, 3}
s.remove(2)
print(s)  # {1, 3}

s = {1, 2}
s.discard(5)  # No error
print(s)  # {1, 2}

s = {10, 20, 30}
print(s.pop())  # Random element like 10

s = {1, 2}
s.clear()
print(s)  # set()

a = {1, 2}
b = {2, 3}
print(a.union(b))  # {1, 2, 3}

a = {1, 2}
b = {2, 3}
print(a & b)  # {2}

a = {1, 2, 3}
b = {2, 4}
print(a - b)  # {1, 3}

a = {1, 2, 3}
b = {2, 3, 4}
print(a ^ b)  # {1, 4}

a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True


a = {1, 2, 3}
b = {1, 2}
print(a.issuperset(b))  # True


a = {1, 2}
b = {3, 4}
print(a.isdisjoint(b))  # True
