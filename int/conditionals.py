# #IF statements
# is_raining = True
# is_cold = True
# print("Good Morning")
# # if is_raining or is_cold:#if both are true or one of the bollean is true or if both are false or one is false
# if is_raining and is_cold:#will only be true if both are true and will be false if both are false 
#     print("Bring umbrella or jacket or both  ")
# else:
#     print("umbrella is optional")


# #Elif statement
# raining = True
# cold = True

# print("Good Evening")


# if raining and cold:
#     print("Bring umbrella and jacket")
# elif raining and not (cold):
#     print("bring only umbrella ")
# elif cold and not (raining):
#     print("bring only jacket")
# else:
#     print("Good to go ")




# amount = 60
# if amount <= 50:
#     print("purchase approved")
# else:
#     print("please enter your pin")

#excersice
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

operator = input("Enter operand:\n")
number1 = float(input("enter first number:\n"))
if operator.lower() == 'f':
    print((number1*9/5)+32)
else:
    number2 = float(input("enter second number:\n"))

    if operator == '+':
        print (number1 + number2)
    elif operator == '-':
        print(number1 - number2)
    elif operator == '*':
        print(number1*number2)
    elif operator == '/':
        print(number1/number2)

    else:
        print("invalid oprator")

   