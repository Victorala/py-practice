import random
import time

file1 = open('questions.txt','r')
file2 = open('words.txt','r')

cardText = file1.readlines()
options = file2.readlines()

card = random.choice(cardText)

option1 = random.choice(options)
option2 = random.choice(options)
option3 = random.choice(options)

print(card)
time.sleep(1)

print("A. " + option1)
print("B. " + option2)
print("C. " + option3)

choice = input(">>> ")

if choice.upper() == 'A':
    card = card.replace("blank", option1)
elif choice.upper() == 'B':
    card = card.replace('blank', option2)
else:
    card = card.replace('blank', option3)

print(card)