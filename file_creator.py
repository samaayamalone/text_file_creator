# Prompt user for their name and favorite number
name = input("What's your name? \n")
number = input("What's your favorite number? \n")

# Open 'example.txt' in write mode and write the user's input
with open('example.txt', 'w') as file:
    file.write(f"{name} created this file.\n")
    file.write(f"{name}'s favorite number is {number}.")

  