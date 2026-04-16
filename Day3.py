# if and else statements do a certain command when a condition is/isnt met. indentation is required under the if/else to do something
# elif is an in between condition check to catch anything that is in between the main two conditions. 
def are_you_tall_enough(height):
    # height = int(input("What is your height in cm: "))
    if height >= 175:
         print("You are a big boiiii!")
    else:
        print("You little goblin you lol")

# are_you_tall_enough(height = int(input("what is your height?")))

def Even_or_Odd(number):
    if number % 2 == 0:
        print("Even")
    else: 
        print("Odd")

    
def main():
    number = int(input("What is your number? "))
    Even_or_Odd(number)

# if __name__ == "__main__":
#     main()

# print("Welcome to Python Pizzeria")
# bill = 0
# size = input("What is the size of your pizza? S/M/L? ")
# pepperoni = input("Do you want pepperoni on your pizza. Type Y or N. ")
# extra_cheese = input("Do you want extra cheese on your pizza? Type Y or N. ")

# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25

    
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == "Y":
#         bill += 1 

# print(f"Your Total will be: ${bill}")

# logical operators to use in an if statements ("and", "or", "not")
# "and" is only true if the whole line of conditions are true
# "or" is only false when all of it is true
# "not" it flips the meaning around of true and false ()
# word.lower (stringmethods)


print("Welcome to Skull Island. \nYour mission is to escape King Schlong")

first_choice = input("Which direction would you like to go? \nType left or right. ")
second_choice = input("You found a cave! \nWould you like to go in? Type Y or N: ")
last_choice = input("You've entered and found 3 doors inside. \nWhich color door are you choosing? Red, Green or Yellow? ")

if first_choice == "right" or first_choice == "Right":
    print(second_choice) 
    if second_choice == "Y" or second_choice == "y":
        print(last_choice)
        if last_choice == "Red" or last_choice == "red":
            print("You have been caught in a fire trap! Game over")
        elif last_choice == Yellow or last_choice == yellow:
            print("You have found the way out! ")
else:
    print("Game over")










