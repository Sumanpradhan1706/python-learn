a= int(input("Enter the marks of bengali:"))
b= int(input("Enter the marks of english:"))
c= int(input("Enter the marks of math:"))

if(a>= 40 and b>=40 and c>=40):
    print("You are pass")
elif(a<33 or b<33 or c<33):
    print("You are fail")
else:
    print("You are pass with grace marks")