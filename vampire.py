#! /usr/bin/python3

print('what is your name?')
name = input()
print('It is good to meet you, ' + name)
print('what is your age?')
age = input()
age = int(age)
if name == 'Alise':
    print('Hi, Alise')
elif age < 12:
    print('You are not Alise, kiddo.')
elif age > 1000:
    print('Unlake you, Alise is not an undead, immortal vampire')
elif age > 100:
    print('You are not Alise, grannie')
else:
    print('You are neither Alies nor a little kid')