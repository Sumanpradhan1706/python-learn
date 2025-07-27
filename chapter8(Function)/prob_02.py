
def convert(c):
    f = (c * 9/5) +32
    return f

c = int(input("Enter temperature in Celsius: "))
print(f"the temperature in farenhite of temperature {c}c is : {convert(c)}")