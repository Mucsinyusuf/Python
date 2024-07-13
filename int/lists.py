# #lists
# friends = ['john','michael','terry','eric']
# cars = [911,130,328,535,740,308]

# # #accessing using index
# # print(friends[1],friends[3])
# # #slicing
# # print(friends[:2])
# # #length of strings
# # print(len(friends))
# # print(friends.index('john'))
# # print(friends.count('michael'))

# #sorting 
# friends.sort()
# print(friends)
# #sorting in different direction
# friends.sort(reverse=True)
# print(friends)
# friends.reverse()
# print(friends)

# cars.sort()
# print(cars)
# #sorting in different direction
# cars.sort(reverse=True)
# print(cars)
# cars.reverse()
# print(cars)

# print(min(cars))
# print(max(cars))
# print(sum(cars))

# print(min(friends))
# print(max(friends))

# #modifying lists

# #1 Append
# friends.append('Mucsin')
# #2 Insert
# friends.insert(1,'Abdi')
# #use index directly
# friends[2]='Terryg'
# #extending the lists 
# # friends.extend(cars)
# #removing something
# friends.remove('Terryg')
# friends.pop(2)
# # friends.clear()
# del friends[2]
# #coping lists 
# new_friends=friends[:]
# friends2=friends.copy()
# friends3=list(friends)

# print(friends)
# print(new_friends)
# print(friends2)
# print(friends3)

sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []

day7=int(input("enter number of lemonades\n"))
sales_w2.append(day7)
print(sales_w2)
# sales.extend(sales_w2)
# sales.extend(sales_w1)
sales = sales_w1 + sales_w2
print(sales)

bestday=max(sales)*1.5
worstday=min(sales)*1.5
print(bestday)
print(worstday)
sum = bestday+worstday
print(sum)