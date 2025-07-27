
def greatest(a,b,c):
    if(a>b and a>c):
        print("Greatest number is:", a)
    elif(b>a and b>c):
        print("Greatest number is:", b)
    else:
        print("Greatest number is:", c)


a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))
c = int(input("Enter the value of c:"))

greatest(a, b, c)  # calling the function with arguments a, b, and c