from clear import clear
from DAY9_ART import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
result = {}
finish=False
def find_highest_bid(bid_record):
    highest_bid = 0
    winner=""
    for bidder in bid_record:
        bid_amount=bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not finish:
    name=input("What is ur name?")
    bid=int(input("What is ur Bid price? $"))
    result[name]= bid
    continue_play=input("Are there any bidders? Type Y or N").lower()
    if continue_play == "n":
        finish = True
        find_highest_bid(result)
    elif continue_play == "y":
        clear()






