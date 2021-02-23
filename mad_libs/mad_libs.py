import random

f = open('madlibs.txt','r')
madlibText = f.readlines()

madlib = random.choice(madlibText)

noun = input('Enter a noun: ')
madlib = madlib.replace('blank', noun)

print(madlib)