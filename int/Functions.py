#functions
#always declare the function before using it like declare above 
# def greeting(name, age=28, color='red'):
# #     print(f"Hello {name}, you will be {age + 1}  next birthday!")
# #     print(f"We hear you like the color {color}")

# # name = input("enter your name:").capitalize()
# # color = input("whats your color:").lower()
# greeting(name,32,color)





def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return amount , tax, total_amount
price = value_added_tax(100)
print(price, type(price))