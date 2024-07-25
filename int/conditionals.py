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

# operator = input("Enter operand:\n")
# number1 = float(input("enter first number:\n"))
# if operator.lower() == 'f':
#     print((number1*9/5)+32)
# else:
#     number2 = float(input("enter second number:\n"))

#     if operator == '+':
#         print (number1 + number2)
#     elif operator == '-':
#         print(number1 - number2)
#     elif operator == '*':
#         print(number1*number2)
#     elif operator == '/':
#         print(number1/number2)

#     else:
#         print("invalid oprator")


# def num_days(month):

#     if month == 'jan':
#         print('number of days in',month,'is',31)
#     elif month == 'feb':
#         print('number of days in',month,'is',28)
#     elif month == 'mar':
#         print('number of days in',month,'is',31)
#     elif month == 'apr':
#         print('number of days in',month,'is',30)
#     elif month == 'may':
#         print('number of days in',month,'is',31)
#     elif month == 'jun':
#         print('number of days in',month,'is',30)
#     elif month == 'jul':
#         print('number of days in',month,'is',31)
#     elif month == 'aug':
#         print('number of days in',month,'is',31)
#     elif month == 'sep':
#         print('number of days in',month,'is',30)
#     elif month == 'oct':
#         print('number of days in',month,'is',31)
#     elif month == 'nov':
#         print('number of days in',month,'is',30)
#     elif month == 'dec':
#         print('number of days in',month,'is',31)

# num_days('oct')
# optimize/shorten the code in the function
# try to reduce the number of conditionals 


def num_days(month):

    if month == 'jan' or month == 'mar' or month == 'may' or month == 'jul' or month == 'aug' or month == 'oct' or month == 'dec':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    elif month == 'apr' or month == 'jun' or month == 'sep' or month == 'nov':
        print('number of days in',month,'is',30)
    else :
        print("invalid")
num_days('oct')

# def num_days(month):
#     days = 31
#     if month in {'apr','jun','sep','nov'}:
#     #if month == 'apr' or month =='jun' or month =='sep' or month =='nov':
#         days = 30
#     elif month == 'feb':
#         days = 28
#     print('number of days in',month,'is',days)
    

# num_days('jan')