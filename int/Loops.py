# #while loop\
# #syntax
# # while condition:
#     #iterator
# #     code 
# #     

# i=0
# while i < 5:
#     i +=1
#     print(f"{i}."+ "*"*i + "Loops are awesome" + "*"*i)
    

# num = 12
# guess = 0
# guess_limit = 3
# guess_numbr= 0

# while guess_numbr < guess_limit:
#     guess = int(input("guess a number 1 - 20"))
#     if guess == num:
#         print("You win !")
#     else:
#         print(f"No , not {guess}")
#         guess_numbr +=1
# if guess != num:
    
#     print(f"you lose ! it was {num}")

#for loops

# for x in range(2,8):
#     print(x)
#syntax
#for i in range(start, end):
    #code


# friends = ['John','Terry','Eric','Michael','George']
# for friend in friends:
#     if friend == 'Eric':
#         print('Found' + friend)
#         continue
#     print(friend)

#nested loops 
# friends = ['John','Terry','Eric','Michael','George']
# for friend in friends:
#     for number in [1,2,3]:
#         print(friend, number)


#excercise
# names = ['john ClEEse','Eric IDLE','michael']
# names1 = ['graHam chapman', 'TERRY', 'terry jones']
# message = "You are invited to the party on saturday."
# names.extend(names1)

# for i in range (1):
#      names.append(input("enter your name: "))

# for name in names :
#     print(f'{name.title()}'+' ' + message)
i = 0
for i in range(3,27):
    print(f"Hello Coddy: {i} ")
    
        
