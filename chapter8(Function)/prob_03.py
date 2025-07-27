
def sum(n):
    if (n== 0):
        return0
    elif(n ==1):
        return 1
    return n + sum(n-1)

n = int(input("Enter the value of n :"))

print(f"The sum of {n} numbers is : {sum(n)}")