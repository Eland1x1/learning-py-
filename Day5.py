import string
import random
# for loops assigns a variable to each item of a list and carries out the action indented after it with them. 
# fruits = ["apple", "pear"]
# for fruit in fruits:
#     print(fruit)
#     print(fruit + "pie")
#     print (f"{fruit} pot pie")

student_scores = [123, 234, 345, 456, 567]

# total_exam_score = sum(student_scores)

# sum = 0 
# for score in student_scores:
#     sum += score

# print(sum)

# max_score = 0 
# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print((max_score))
# print(max(student_scores))

#Range(lower bound, upper bound, steps between numbers) in a for loop allows you to again assign it to a variable and do something. 
#it does not print every number within the upper bound of the range
# total = 0
# for number in range(1,101):
#     total += number

# print(total)

# for i in range(40,65):
#     numbers.append(chr(i))

# print(numbers)

letter = list(string.ascii_letters)
number = list(string.digits)
symbol = ['!','#','$','%','&','*','(',')','+']

print("Welcome to the PyPassword Generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("Final how many numbers would you like?\n"))

password = []

for i in range(nr_letters):
    i = random.choice(letter)
    password.append(i)
for i in range(nr_symbols):
    i = random.choice(symbol)
    password.append(i)
for i in range(nr_numbers):
    i = random.choice(number)
    password.append(i)

print(password)
str_password = "".join(password)
print(str_password)
random.shuffle(password)
print(password)
str_password = "".join(password)
print(str_password)
# datum = ["18", "04", "2026"]
# strin_datum = "-".join(datum)
# print(strin_datum)

Pokemon = "my,favorite,pokemon,is:,pikachu"
print(Pokemon) 
print(Pokemon.split("m"))
   






    



    

    




