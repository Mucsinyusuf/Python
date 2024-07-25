# my_list = [1,5,3,7,2]
# my_dict = {'car':4,'dog':2,'add':3,'bee':1}
# my_tuple = ('d','c','e','a','b')
# my_string = 'python'
# print(my_list,'original')
# print(list (reversed(my_list)))
# print(my_list[::-1])#reverses the list 

# print(my_dict,'original')
# # print(sorted(my_dict.items()))
# # print(my_dict, 'new')

# print(my_string,'original')
# print(sorted(my_string))
# print(my_string, 'new')

# print(my_tuple,'original')
# print(sorted(my_tuple))
# print(my_tuple, 'new')


my_list = [1,5,-3,7,-2]
my_llist=[['car',4,65],['dog',2,30],['add',3,10],['bee',1,24]]
print(sorted(my_list, key=abs))#when you add abs sorts the list regardless of negativ or positive
print(sorted(my_llist , key = lambda item :item[1]))
