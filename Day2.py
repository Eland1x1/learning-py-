# #Data types: Strings = text within quotation marks
# # Integers = whole numbers 
# # Floats = decimal numbers
# # Booleans = True or false values 
# #square brackets added at the end of your string allows you to dissect parts of your string. Always start from zero aswell
# #certain functions can only work with certain data types so notation is important
# # use 'type' function to determine a data type if uncertain.
# # print("Hello"[4]) 
# # 'str()' function can convert a different datattype into a string
# # 'int()' function can convert string that contains whole numbers into an integer data type
# # same idea with "bool()" and "float()"
# print(f"{type(123)} \n{type("Deez")} \n{type(3.14)} \n{type(False)}")

# print("Number of letters in your name: " + str(len(input("Enter your name: "))))

# print(123 + 567)
# print(6*2)
# print(7-2)
# print(10/2)
# print(10//2)
# print(7**2)

# # math priority PEMDAS (read it from left to right for div/mult and add/subtr)
# # 'round(number, ndigits or ndecimals)' function allows you to round decimal number in the traditional mathmatical way

# # assign a value based on its previous value

# score = 0 

# score += or -= etc. 

# f-string --> allows you to add different types of data with curly brackets {}

# final coding excersise day 2


def tip_calculator(total_bill, tip, people_to_split):
    print("Welcome to the tip calculator!")
    # total_bill = int(input("What was the total bill? $"))
    # tip = int(input("How muchf tip would you like to give? 10, 12 or 15? "))
    # people_to_split = int(input("How many people to split the bill? "))
    tip = float(total_bill * (tip/100))
    Payment_per_person = (total_bill + tip)/ people_to_split
    print(f"Each person should pay: $ {Payment_per_person:.3f}")

tip_calculator(200,5,2)
