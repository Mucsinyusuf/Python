movie = {
    "title": 'life of Brian',
    "year": 1979,
    "cast": ['John','Eric','Michael','George','Terry']
}
# updating dictionary
movie.update({'title' : 'The Holy Grail','year':1975,'cast':['John','Eric','Michael','George','Terry']})
movie['title']='The Holy Grail'
movie['budget']= 765
year = movie.pop('year')
# print(movie.get('title'))
# # print(movie.get('budget'))
# print (len(movie))
# print(movie.keys())
# print (year)



# for key, value in movie.items():
#     print(key, value)






python = {'John':35,'Eric':36,'Michael':35,'Terry':38,'Graham':37,'TerryG':34}
holy_grail = {'Arthur':40,'Galahad':35,'Lancelot':39,'Knight of NI':40, 'Zoot':17}
life_of_brian = {'Brian':33,'Reg':35,'Stan/Loretta':32,'Biccus Diccus':45}
print('Arthur' in holy_grail)
if "Arthur" not in python:
    print("hes not here") 

#concantinating dics

people = {}
peopl1={}
people2={}
#method one is update()
people.update(python)
people.update(holy_grail)
people.update(life_of_brian)
print(sorted(people.items()))
#method 2 comprehention
for groups in (python,holy_grail,life_of_brian): peopl1.update(groups)
print(sorted(peopl1.items()))
#method3 unpacking
people2={**python,**holy_grail,**life_of_brian}
print(sorted(people2.items()))
print('he sum of the ages ', sum(people.values()))