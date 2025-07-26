'''
1 for snake
-1 for water 
0 for gun

'''
import random
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choise:")
youDict = {"s":1 ,"w":-1, "g":0}
reverseDict = {1:"snake", -1:"water", 0:"gun"}

you = youDict[youstr]

print(f" you choose {reverseDict[you]} \n computer choose {reverseDict[computer]}")

if(computer == -1 and you ==1 or computer ==1 and you ==0 or computer == 0 and you ==-1 ):
    print("you win")
elif(computer == you):
    print(" Draw game!")
else:
    print("You lose")