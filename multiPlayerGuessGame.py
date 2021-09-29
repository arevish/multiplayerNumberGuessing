# For multiple number or players(2 or more)
import random
print("Welcome to Guess the number game!!! ")
play = []
player= int(input("Enter number of players: "))
for i in range(player):
    play.append(i)
# print(play)
guess1 = int(input("Please enter a range of number to guess the number \nMinimum: "))
guess2 = int(input("Maximum: ")) 
print(f"Guess the number between {guess1}-{guess2}\nYou have only 5 guesses")

# print("player1 turn")
win =[]
for i in play:
    comp_guess= random.randint(guess1,guess2)
    # print(comp_guess)
    j=1
    n=4
    while n!=-1:
        player1= int(input(f"\nPLAYER{play[i]+1} - Enter your guessed number: "))
        if comp_guess==player1:
            print(f"\nCongrats! You guessed the correct number PLAYER{play[i]+1}")
            print(f"Number of guess took to complete: {j}")
            if i!=player-1:
                print("\nNext player turn")
            win.append(j)
            break
        elif comp_guess>player1:
            print(f"incorrect guess, number is GREATER than this")
        elif comp_guess < player1:
            print(f"incorrect guess, number is LESSER than this")   
        print(f"You have {n} guess left")
        j+=1
        n=n-1
        if n==-1:
            print("\nYou Loose! Run out of guesses")
            win.append(j)
            if i!=player-1:
                print("\nNext player turn")
# whose j value smallest will win , if equal then draw

print("\nSCORE :\nNumber of guesses player took",win)
min = win[0]
for i in win :
    if i < min:
        min = i 
index = win.index(min)
# print(index)
print(f"Player{index+1} wins!!")
print(f"Takes only {min} guess")
# print(min(win))



# For 2 players
'''
import random

def guessgame(a,b, actual):
    guess = int (input(f"guess a number between {a} and {b} "))
    nguess =0
    while guess!= actual:
        if guess< actual:
            guess = int(input("Enter a greater number"))
            nguess+=1

        elif guess> actual:
            guess = int(input("Enter a smaller number"))
            nguess+=1
    print(f"you guesed the number in{nguess} guesses\n")
    return nguess
if __name__ == '__main__' :
    print("Welcome to Guess the number game!!! ")
    a = int(input ("Enter the minimum value\n"))
    b = int(input ("Enter the maximun value\n"))
    actual1 =random.randint(a,b)
    print("player 1 turn")
    g1 = guessgame(a,b,actual1)
    actual2 =random.randint(a,b)
    print("player 2 turn")
    g2 = guessgame(a,b,actual2)

    if g1<g2:
        print("player1 won")
    elif g1>g2:
        print("player2 won")
    else:
        print("Its a tie!\n")
    print(f"the number of turns for player 1 was {actual1} and for player2 was {actual2}")
    '''