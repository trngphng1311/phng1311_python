#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

placeholder = "[name]"

with open("C:/Users/Admin/OneDrive - VietNam National University - HCM INTERNATIONAL UNIVERSITY/Documents/PYTHON/PYTHON CODE COURSE/day24/Input/Names/invited_names.txt.txt") as name_file:
    names = name_file.readlines()
    print(names)
with open("C:/Users/Admin/OneDrive - VietNam National University - HCM INTERNATIONAL UNIVERSITY/Documents/PYTHON/PYTHON CODE COURSE/day24/Input/Letters/starting_letter.txt") as start_file:
    letter_contents = start_file.read()
    for name in names:
        tripped_name = name.strip()
        new_letter = letter_contents.replace(placeholder, tripped_name)
        with open(f"C:/Users/Admin/OneDrive - VietNam National University - HCM INTERNATIONAL UNIVERSITY/Documents/PYTHON/PYTHON CODE COURSE/day24/Output/ReadyToSend/letter_for_{tripped_name}.txt", 'w') as completed_letter:
            completed_letter.write(new_letter)
