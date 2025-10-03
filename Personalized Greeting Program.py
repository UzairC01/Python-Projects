#Printing welcome to welcome the user
print("Welcome")

#Asking and storing the user's name
name = input("What is your name: ")

#Asking and storing the user's age
age = int(input("What is your age: "))

#Printing a greeting statement with the user's name and age
print(f"Hello, {name}! You are {age} years old.")

#Asking for a specific number from the user so it can calculate the future age after that specific number of years.
number = int(input("Enter a number to calculate how old your going to be after that specific number of years: "))

#Calculates the future age.
futureage = age + number

#Prints the future age and the number of years they have given
print(f"You will be {futureage} years old, after {number} years")

#Asking the user for a word
word = input("Enter a word: ")

#Prints the first letter of the word
print("First letter of the word is: ", word[0])

#Prints the last letter of the word 
print("Last letter of the word is: ", word[-1])

#Prints Every other letter of the word
print("Every other letter of the word is: ", word[::2])