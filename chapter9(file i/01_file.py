# f = open("file.txt")
# data =f.read()
# print(data)
# f.close()


with open("file.txt", "r") as f:
    data = f.read()
    print(data)
f.close()