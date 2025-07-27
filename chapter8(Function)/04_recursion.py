 # factorial(5)  = 5x4x3x2x1 = 120

def fact(n):
    if( n ==0 or n==1):
        return 1
    return n * fact(n-1)   # this is recursion, where the function calls itself
    # for example, fact(5) will call fact(4), which will call fact

n = int(input("Enter a number to find its factorial: "))

print(f"The factorial of {n} is:  {fact(n)}")