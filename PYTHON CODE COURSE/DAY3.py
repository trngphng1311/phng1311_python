print("WELCOME")
turn=input("Would like to turn here").lower()
sw=input("Would like to swim or wait").lower()
door=input("Choose door color").lower()
if turn=="left": 
    if sw=="wait":
        if door=="blue":
            print("BEAST OVER")
        elif door=="Red":
            print("Fire OVER")
        elif door=="Yellow":
            print("WIN")
    else: print("OVER")
else: print("OVER")