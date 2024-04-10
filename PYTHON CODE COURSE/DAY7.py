#Step 1 
from replit import clear
from DAY7_WORD import word_list
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

randomword=random.choice(word_list)
end = False
live = 6

from DAY7_ART import logo, stages
display(logo)

display=[]
for _ in randomword: #or for _ in range(len(randomword)):
    display +="_"
    # print(display)

while not end:
    guess=input("Guess a letter\n").lower()
    clear()
    # for letter in randomword:
    #     if letter == guess:
    #         print("Right")
    #     else: print("Wrong")
    if guess in display:
        print("U already guess this letter ")

    for position in range(len(randomword)):
        letter = randomword[position]
        # print(f"Current Position: {position}\n Current letter: {letter}\n Guessed Letter: {guess}")
        if letter == guess:
            display[position] = letter
    print(display)
    
    if guess not in randomword:
        print(f"{guess} not in the word, ya lost 1 life anyway")
        live -= 1
        if live == 0:
            end= True
            print("You lost")
  
    
    if "-" not in display:
        end = True
        print("You win")

    print(stages[live])



