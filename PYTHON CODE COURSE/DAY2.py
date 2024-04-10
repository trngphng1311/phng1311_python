# ########Data Types
# ###String   
# #print("Hello"[0]) #Subscript - Result is H
# "Hello"[4]
# ###Interger
# print(123+345)
# ####Float - so thap phan
# 314.59
# ####Boolean - Binary for true/false
# True 
# False 
########################################################################
#How to know the type of the data 
# num_char = len(input("What is your name\n"))
# # print("Your name has "+ num_char) #result la loi syntax
# print(type(num_char)) #check what is the data type -> integer in this case -> print string + integer -> syntax error
#######Type casting - change data type 
# new_num_char=str(num_char)
# print("Your name has "+ new_num_char) 
# a = 123
# float_a=float(a) 
# string_a=str(a)
# intger_a=int(a)
# print(type(float_a))
# print(type(string_a))
# print(type(intger_a))
##################################################################
result = 4/2
result /=2 #take the above result once again divide for 2 
print(result) #now it will print out the final result till the last equation devide is 1
#PEMDAS once again or more for each calculation 
#score = 0 
#Add more 1 unit -> score +=1
#Exponential with 2 -> score **=2
#Subtract 1 unit -> score -=1
#Divide 2 unit -> score /=2
###### MIX STRING - f-String tranfers all the data to be the same kind
# score = 0 
# height = 1.8
# isWinning = True 
# print(f"ur score is {score} \n ur heigt is {height} \n your is winning {isWinning}")
# print(6 + 4 / 2 - (1 * 2))
###############################################################################
T=input("What was the total bill? $\n")
P=input("What percentage tip would you like to give? 10, 12 or 15? $\n")
H=input("How many people to split the bill? \n")
Total=float(T)
Percent=float(P)
Human=float(H)
Pay=(Total/Human)*(1.0+Percent/100.0)
print(f"Each person should pay: ${round(Pay,2)}")













