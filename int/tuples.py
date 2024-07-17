# # tuples are lists than can;t change
# friends = ['John','Michael','Terry','Eric','Graham']
# friends_tuple = ('John','Michael','Terry','Eric','Graham')
# # print(friends[2:4])
# # print(friends_tuple[2:4])
# # we use tuples when we have lists that we dont want to change

# # sets 
# # sets is unordered list and removes duplicates

# friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
# my_friends_set = {'Reg','Loretta','Colin','Eric','Graham'}
# #using .intersection() to check which element exists in both sets 
# print(friends_set.intersection(my_friends_set))
# #using .difference() to see which elemnt do not exist in the other set)
# print(friends_set.difference(my_friends_set))
# #using the union() to combine ll the sets 
# print(friends_set.union(my_friends_set))
#  # creating empty list 
# empty_list = []
# #or
# empty_list=list()

# #creating empty tuple
# empty_tuple=()
# #or
# empty_tuple=tuple()

# #creating empty Sets
# empty_set={}# this is wrong this is a dictionary

# empty_set=set()# use always this to declare sets

# sets Excersice
#1. Check if ‘Eric’ and ‘John’ exist in friends
#2. combine or add the two sets 
#3. Find names that are in both sets
#4. find names that are only in friends
#5. Show only the names who only appear in one of the lists
#6. Create a new cars-list without duplicates

friends = {'John','Michael','Terry','Eric','Graham'}
my_friends = {'Reg','Loretta','Colin','John','Graham'}
cars =['900','420','V70','911','996','V90','911','911','S','328','900']



print('Eric' in friends and 'John' in friends)
print(friends.union(my_friends))
print('names in both sets :', friends.intersection(my_friends))
print('names only in friends:',friends.difference(my_friends))
print(my_friends.symmetric_difference(friends))
cars_list=set(cars)
print(cars_list)
 #union we can use |
 #intersection = &
 #difference = -
#symmetric_difference() =^ shows only elemnts that appear in one of the sets

