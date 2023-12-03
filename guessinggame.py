#Luis Garcia 12/1/23 Guessing Game
from random import randrange

def main():
    print("This program will simulate a guessing game.")
    randnum = randrange(0,100)
    guesses = 1
    guess = 0
    while guess != randnum:
        guess = eval(input("Please guess a number from 1 to 100. "))
        if guess < randnum:
            print("Higher...")
            guesses = guesses + 1
        elif guess > randnum:
            print("Lower...")
            guesses = guesses + 1
        else:
            print("You got it! The number was " + str(randnum) + " and it took you " + str(guesses) + " tries!")
main()            
