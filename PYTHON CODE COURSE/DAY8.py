# def greet():
#     print("Hello")
#     print("How do u do?")
#     print("Do I love u")

# greet()

# #Function for input 
# def greet_name(name):
#     print(f"Hello {name}")
#     print(f"How do u do {name}?")

# greet_name("Gwen")

#Function with more than 1 inputs
# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with("Gwen", "HCM City")

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"What is it like in {location}")
# greet_with(name="Gwen", location="HCM City") #doodir vij tris se khong ay anh huong toi vi tri bien va nghiem


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


def ceaser(start_text, shift_amount, cipher_direction):
    end_text=""
    if cipher_direction == "decode":
        shift_amount *=-1
    for letter in start_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position= position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text +=letter
    print(f"The {cipher_direction} text is {end_text}")

# def encrypt(plain_text, shift_amount):
#     cipher_text=""
#     for letter in plain_text:
#         position=alphabet.index(letter)
#         newposi=position + shift_amount
#         new_letter = alphabet[newposi]
#         cipher_text +=new_letter
#     print(f"The encode text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#     plain_text=""
#     for letter in cipher_text:
#         position=alphabet.index(letter)
#         newposi=position - shift_amount
#         new_letter = alphabet[newposi]
#         plain_text +=new_letter
#     print(f"The decode text is {plain_text}")
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode": 
#     decrypt(cipher_text=text, shift_amount=shift)
Should_continue = True
while Should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift% 26

    ceaser(start_text=text,shift_amount=shift,cipher_direction=direction)
    result= input("Wanna play more?\n").lower()
    if result == "no":
       Should_continue=False
       print("Gudbai") 