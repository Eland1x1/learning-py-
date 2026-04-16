# RANDOM GENERATOR
# random_integer = random.randint(1,10)
# print(random_integer)
import random

# random_number_0_to_1 = random.random()
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)

# random_coinflip = random.randint(0,1)
# print("Heads or Tails?")
# if random_coinflip == 0:
#     print("Heads")
# else:
#     print("Tails")

#Random choice from list
#Random.choices(variable, k=N)

# LISTS
# you can choose which part of the list with [] and a positive or negative number. 
# states_US = ["Houston", "Delaware", "Arizona"]
# states_US.append ("Florida")
# states_US.extend(["New York","Minnesota"])
# print(states_US)
# nested lists are also possible

# friends = ["Alice" ,"Ethan", "Ross","Maria"]

# print(random.choice(friends)
#While loop??
valid_input = False 
while not valid_input:
    player_choice = int(input("what do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
    if player_choice in [0,1,2]:
        valid_input = True
    else: 
        print("Invalid input, Please try again.")
        
computer_options = ["Rock", "Paper", "Scissors"]
computer_choice = random.choice(computer_options)

print(f"Computer chose: {computer_choice}")

if player_choice == 0:
    if computer_choice == "Rock":
        print("Draw")
    elif computer_choice == "Paper":
        print("You lose")
    else:
        print("You win")
elif player_choice == 1:
    if computer_choice == "Rock":
        print("You win")
    elif computer_choice == "Paper":
        print("Draw")
    else:
        print("You lose")
if player_choice == 2:
    if computer_choice == "Rock":
        print("You lose")
    elif computer_choice == "Paper":
        print("You win")
    else:
        print("Draw")
    
    












