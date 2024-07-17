# msg ='Welcome to Python 101: Split and Join'
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = (','.join(','.join(csv.split(';')).split(':')).split(','))
print(friends_list)
#we can use replace
print('replace=',csv.replace(';',',').replace(':',',').split(','))


# print(msg.split())
# print(csv.split(','))
#join
# print(''.join(friends_list))
#when we split we turn something into a list and we join we chnage it a string

