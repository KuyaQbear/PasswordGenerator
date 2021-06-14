import random

#Shuffle
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return "".join(tempList)


#Main Program
userName = input("please provide the first 3 characters of your first name then hit enter.  ")
uppercaseLetter1 = chr(random.randint(65,90)) #Generates a Random Uppercase Letter
uppercaseLetter2 = chr(random.randint(65,90)) #Generates a Random Uppercase Letter
lowercaseLetter1 = chr(random.randint(97, 122)) #Generates a random Lowercase Letter
lowercaseLetter2 = chr(random.randint(97, 122)) #Generates a random Lowercase Letter
randomNumber1 = chr(random.randint(48, 57)) #Generates a random Number
randomNumber2 = chr(random.randint(48, 57)) #Generates a random Number
specialCharacter1 = chr(random.randint(33, 38)) #Generates a special Character
specialCharacter2 = chr(random.randint(33, 38)) #Generates a special Character




#Generates Password in random order
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + randomNumber1 + randomNumber2 + specialCharacter1 +specialCharacter2
password = userName + shuffle(password)


#output
print(password)



