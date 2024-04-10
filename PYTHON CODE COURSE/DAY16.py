from DAY16_MENU import Menu, MenuItem
from DAY16_COFFEMAKER import CoffeeMaker
from DAY16_MONEYMACHINE import MoneyMachine

my_money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
is_on = True

coffe_maker.report()
my_money_machine.report()

while is_on:
    order = menu.get_items()
    choice = input(f"What whould u like? {order} ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffe_maker.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            coffe_maker.make_coffee(drink)

