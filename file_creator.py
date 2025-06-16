
name = input("What's your name? \n")
fruit = input("What's your favorite fruit? \n")

with open('example.txt', 'w') as file:
    file.write(f"{name} created this file.\n")
    file.write(f"{name}'s favorite fruit is {fruit}.")

  