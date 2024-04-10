import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game=[rock, paper, scissors]

ur_ans=int(input("What do you choose?\n Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if ur_ans >= 3 or ur_ans < 0:
    print("Invalid ans")
else:
    print(game[ur_ans])
    
    com_ans=random.randint(0,2)
    print(f"Computer choose {com_ans}")
    print(game[com_ans])

    if com_ans > ur_ans: 
        print("Computer win! Ya lose")
    elif ur_ans > com_ans:
        print("Ya win!!!")
    elif ur_ans == 0 and com_ans == 2:
        print("Ya win!!!")
    elif com_ans ==  0 and ur_ans == 2:
        print("Ya lose bru")
    elif ur_ans == com_ans:
        print("Burhh ya drawww")








