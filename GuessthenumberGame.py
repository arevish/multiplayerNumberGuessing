#For one person vs computer
import random
i = random.randint(0,100)
j=5
m=0
print("Total number of guesses = 6")
while (True):
    n=int(input("Enter your number "))
    m=m+1
    if n==i:
        print("You WIN!")
        print("number of guess you took to finish",m)
        break
    else:
        if n<i:
            print("You are close ,Number is greater than this ")
        else:
            print("Your are close , Number is smaller than this")
    print("Number of guess left",j)
    j=j-1
    if j<0:
        print("Game Over! run out of guess")
        print("Number was ",i)
        break
    continue
