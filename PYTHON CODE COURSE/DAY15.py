MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def enough_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}")
            return False
    return True

def coin():
    """Return coins insered in total :>"""
    print("Insert coins plz")
    total = int(input("How many quarters: "))*0.25
    total += int(input("How many dimes: "))*0.1
    total += int(input("How many nickles: "))*0.05
    total += int(input("How many pennies: "))*0.01
    return total

def transaction(money_received, drink_cost):
    """Return True when the payment is accepted"""
    if money_received >= drink_cost:
        change = round(money_received-drink_cost, 2)
        print(f"Here is ur change : {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Not enough monei bruu")
        return False

def make_coffe(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is ur {drink_name}")

on = True
while on:
    order=input("What would u like?")
    if order == "off":
        on = False
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[order]
        if enough_resources(drink["ingredients"]):
            payment = coin()
            if transaction(payment, drink["cost"]):
                make_coffe(order, drink["ingredients"])





