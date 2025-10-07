#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
characters = []

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

for letter in range(1, nr_letters + 1):
  random_integer = random.randint(0, len(letters) - 1)
  characters.append(letters[random_integer])

for symbol in range(1, nr_symbols + 1):
  random_integer2 = random.randint(0, len(symbols) - 1)
  characters.append(symbols[random_integer2])

for number in range(1, nr_numbers + 1):
  random_integer3 = random.randint(0, len(numbers) - 1)
  characters.append(numbers[random_integer3])

random.shuffle(characters)
password = "".join(characters)
print(f"Your new secure password is: {password}")

