import random
from clear import clear
from DAY11_ART import logo

def deal_card ():
    """Returns a random card from the deck"""
    cards = [ 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0 
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
    if user_score == comp_score:
        return "Draw (-_-)"
    elif user_score == 0:
        return "Win with Black Jack (>_<)"
    elif user_score > 21:
        return "Over, you lose (T-T)"
    elif comp_score > 21: 
        return "Computer lose so you win (^_^)"
    elif user_score > comp_score:
        return "Ya winn (^_<)"
    else: 
        return "Ya really lose this time (;_;)"

def Blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not over: 

        user_score=calculate_score(user_cards)
        comp_score=calculate_score(computer_cards)
        print(f"Ur cards {user_cards}, current score {user_score}")
        print(f"Ur cards 1st card, current score {computer_cards[0]}")


        if user_score == 0 or comp_score == 0 or user_score > 21:
            over= True
        else: 
            deal = input("Type y to another car, n for pass: ")
            if deal == "y":
                user_cards.append(deal_card())
            else: 
                over = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    print(f"Ur final hand {user_cards} and score {user_score}")
    print(f"Ur final hand {computer_cards} and score {comp_score}")

    print(compare(user_score, comp_score))

while input("Do you want to play a game of Blackjack? Y or N ").lower() == "y":
    clear()
    Blackjack()