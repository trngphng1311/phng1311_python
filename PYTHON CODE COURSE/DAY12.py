################### Scope ####################
from DAY12_ART import logo
from random import randint
print(logo)
EASY = 10
HARD = 5
turns = 0 
# Make function toi set difficulty ( 5 or 10)
def check_ans(guess, ans, turns):
    if guess > ans:
        print("Too high")
        return turns - 1
    elif guess < ans:
        print("Too low")
        return turns - 1
    else: 
        print(f"You got it, the answer is {ans}")

#Make function to set difficulty
def gamelevel():
    level = input("Choose your level. Type 'easy' or 'difficult': ")
    if level == "easy":
        return EASY
    else: 
        return HARD

def game():
    # Choosing a random number btw 1 and 100 
    print("Welcome to the Number Guessing Game!")
    print("Choose a number from 1 to 100")
    print("Pick up your level, easy or difficult")
    ans = randint(1,100)
    print(f"The ans is {ans}")

    turns = gamelevel()
   
    # Repeat the guessing function 
    guess = 0 
    while guess != ans:
        print(f"You have {turns} attemps to guess")
    # User guess the game 
        guess = int(input("Make a guess: "))
        turns = check_ans(guess, ans, turns)
        if turns == 0:
            print("Ya lost, out of attemps")
            return
        elif guess != ans:
            print("Guess again")

    # Check users guess agaisnt actual ans 

# Trach the turn and reducte by 1 if the ans is wrong 
# Repeat the guessing function 
# If the ns is right then end the game 
game()
