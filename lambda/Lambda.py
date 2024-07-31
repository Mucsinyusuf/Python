print(' Lambda Functions')
def square(x):
    return x*x
# print(square(3))


#lamba 
#syntax
# name = lambda parameter(s): expression
square1 = lambda x,y: 2*x*y
# print(square1(3,2))

#alias

def name_and_alias(name,alias):
    return name.strip().title() + ':' + alias.strip().title()
# print(name_and_alias('john ClEEse ', 'HECKLER'))
#as lambda
name_and_alias1 = lambda name,alias:name.strip().title() + ':' + alias.strip().title()
# print(name_and_alias1('john ClEEse ', 'HECKLER'))



monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']
monty_python.sort(key=lambda name:name.split(' ')[-1])
print(monty_python)
