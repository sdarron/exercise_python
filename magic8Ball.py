#! /usr/bin/python3

import random

def getAnswer(answerNamber):
    if answerNamber == 1:
        return 'It is certain'
    elif answerNamber == 2:
        return 'It is decidedly so'
    elif answerNamber == 3:
        return 'Yes'
    elif answerNamber == 4:
        return 'Reply hazy try again'
    elif answerNamber == 5:
        return 'Ask again later'
    elif answerNamber == 6:
        return 'Concentrate and ask again'
    elif answerNamber == 7:
        return 'My reply is no'
    elif answerNamber == 8:
        return 'Outlook not so good'
    elif answerNamber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print (fortune)