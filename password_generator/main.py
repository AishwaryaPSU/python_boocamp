#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_len = len(letters)
number_len = len(numbers)
symbols_len = len(symbols)
random_pos = 0
password = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for i in range(0, nr_letters):
  random_pos = random.randint(0, letters_len - 1)
  password += letters[random_pos]
for i in range(0, nr_numbers):
  random_pos = random.randint(0,nr_numbers-1)
  password += numbers[random_pos]
for i in range(0, nr_symbols):
  random_pos = random.randint(0,nr_symbols-1)
  password += symbols[random_pos]

print("Easy Level Password: ")
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_pwd = ""
password_len = len(password)
for i in range(password_len):
  if len(password) == 0:
    break
  random_pos = random.randint(0,(len(password)-1))
  hard_pwd += password[random_pos]
  #password = password.replace(password[random_pos], "")
  password = password[:random_pos] + password[random_pos + 1:]
print("Hard Level Password: ")
print(hard_pwd)