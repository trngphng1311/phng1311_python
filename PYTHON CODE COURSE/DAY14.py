import random
from DAY14_DATA import data
from clear import clear

#format the data 


def random_account():


    return random.choice(data)



def format_data(account):


    """FORMAT THE ACCOUNT FOR EACH TYPE OF ACCOUNT A OR B """


    account_name = account["name"]


    account_des = account["description"]


    account_country = account["country"]


    return (f"{account_name}, a {account_des}, from {account_country}")



def check_ans(guess, a_follower, b_follower):


    """Take the user followers to compare"""


    if a_follower > b_follower:


        return guess == "a"


    else: 


        return guess == "b"



score = 0


continue_game = True
account_b = random.choice(data)

while continue_game:
        


    #Generate thhe random game


    account_a = account_b
    account_b = random.choice(data)


    if account_a == account_b:


        account_b = random.choice(data)



    print(f"Compare A: {format_data(account_a)}")


    print(f"Compare B: {format_data(account_b)}")



    #Ask user for a guess


    guess = input("Whho has more followers? A or B ").lower()



    #Check 


    a_follower = account_a["follower_count"]


    b_follower = account_b["follower_count"]



    correct = check_ans(guess, a_follower, b_follower)

    clear()

    if correct:


        score +=1


        print("Ya right")


    else:


        continue_game = False


        print(f"Ya wrong. FINAL SCORE {score}")