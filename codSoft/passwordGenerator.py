'''
A password generator is a useful tool that generates strong and random passwords for users, allowing users to specify the length and complexity of the password. User will specify the desired length of the password.Use a combination of random characters to generate a password of the specified length.And print the password..
'''
import string
import random

str_1 = string.ascii_lowercase # Contains all lower case letters
str_2 = string.ascii_uppercase # Contains all Upper case letters
dig = string.digits # Contains all Numbers
punc = string.punctuation # Contains all the puntuations

# Function to get valid Password length..
def password_len():
    pass_len = input("Enter password length(only Integer Value) : ") # Enter Password length by User...
    # we have to keep asking until valid integer is entered.
    while not pass_len.isdigit(): #check whether the input is integer or not
        print("Invalid Input! Please Enter Integer Value")
        pass_len = input("Enter password length(only Integer Value) : ")
    return int(pass_len)
pass_len = password_len() #get Password length
    
lst = [] 
    #Empty list to extend all letters numbers punctuations. extend will extract only elements inside the list not whole list..
lst.extend(list(str_1))
lst.extend(list(str_2))
lst.extend(list(dig))
lst.extend(list(punc))
    
# print Your Strong Password.
print("Ypur password is: ")
print("".join(random.sample(lst, pass_len)))
    

