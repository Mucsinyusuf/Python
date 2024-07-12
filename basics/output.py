# #!/usr/bin/env python3.9
# age = 10
# print(f"His age is: {age}")

# # input 
# # we can get inputs from users
# #syntax 
# #varriable = input()

# name = input("enter name ")

# print(f"name is :{name}")
# # input values are os a string data type on default 
# # to change we can cast the data type 
# # eg 
# age1 = input()#the number will be string
# age1 = int(input())#it will be a number
# # Here is a table that shows how to cast to different types:

# # Cast	   Explanation
# # int()	    Convert to a whole number
# # float()	Convert to a real number
# # bool()	Convert to a boolean
# # str()	     Convert to a string

# Write a program that gets input from the user, his age.

# The program will output (print) the number of missing years till 120 (in a specific format, shown below).

# For example, for input 25, the expected output is "95 years till 120"

# age4 = int(input("enter age"))
# print(f"{120-age4} years till 120")


# Write a program that gets an input from the user, a number, 1 or 0.

# The program will output "T" if the input is 1 and "F" otherwise.

# number = int(input("Enter the number between 0 and 1\n"))
# if number == 1 :
#     print("T")
# else:
#     print("F")


# myname=input('whats you name \n')
# print(f'his name is {myname}')

#ecercise
first_name=input('your first name\n')
distance =int(input('distance in km\n'))


print(f'hello,{first_name} your km is {distance}km and miles is {round (distance/1.609)} m')


