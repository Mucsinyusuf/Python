# if statement allow us to execute code with conditions
# forexample

age = 20
status = "Child"
if age > 18:
    status = 'Adult'

print(status)

# To use an if statement we need to add a colon : at the end of the if statement 
# and everything that is inside the if is indented with 4 spaces
# Syntax
# if condition:
#    code 
#    code 
#    code 
#    code 

# if the condition is True, we will enter code block inside if (the indeted code )

# if else statement
# we use the if else when we have more than one condition 
# because if its used when only one condition is met 
age2 = 10
status2 = ''
if age2 > 18 :
    status2 = 'Adult'
else:
    status2 = "child"
print (status2)

# we can also use elif

age3 = 73
status3 = ''
if age3 < 18:
    status3 = 'Child'
elif age3 >= 18 and age3 <= 65:
    status3 = 'Adult'
else:
    status3 = 'Old'


# print(status3)

# Syntax elif
# you can have as much as elif as you want
# if condition1:
#     code
# elif condition2:
#     code
# elif condition3:
#     code
# ...

# Note that the code inside the if/elif/else must be indented




# You are given a code which gets as input two numbers n1 and n2 and a character op.
#The possible values for op are '+', '-', '/' and '*'

# Your task is to set the variable result based on the conditions:

# if op is '+', set result with n1 + n2.
# if op is '-', set result with n1 - n2.
# if op is '/', set result with n1 / n2.
# if op is '*', set result with n1 * n2.



n1 = 4
n2 = 2
op = '-'
result = 0


if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
elif op == '*':
    result = n1 * n2
elif op == '/':
    result = n1 / n2

print (result)