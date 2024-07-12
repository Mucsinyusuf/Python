message = 'nice seeing you'
print(message)
print(message.upper())
print(message.lower())
print(message.capitalize())
print(message.title())


string = "mucsin yusuf abdirahman"
print(len(string))
print(string.count('yusuf'))

#slicing strings
print(message[2:])


msg='welcome to Python 101: Strings'
msg1=msg[20]+' '+msg[:8]+msg[25:29]+msg[7:11]+msg[8]+msg[12]+msg[2]+msg[1]+msg[25]

print(msg1.title())
print(msg1)
print(msg1[::-1].title())
#find()finds words in strings
print(msg1.find('tyler'))
#replace() replaces words in strings
print(msg1.replace('tyler','python'))
print('tyler'  in msg1)# checks if tyler is in the msg you can add not before in to check if it is true it doesnt exist

#[::-1]reverses strings 

name='TERRY'
color = 'RED'
mssg = '[' + name + '] loves the color ' + color + '!'
mssg1= f'[{name}] loves the color {color.lower()}!'
print(mssg1)
