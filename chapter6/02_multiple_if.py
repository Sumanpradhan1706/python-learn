a= int(input("Enter your age:"))

#if statement no:1
if(a%2==0):
    print("Even number")
    #if statement no:2
if(a>18):
    print("You are able to vote")

elif(a<0):
    print("Invalid age")
else:
    print("You are not able to vote")
