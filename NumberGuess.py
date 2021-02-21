import random

def guess(x):
    number = random.randint(1, x)
    guess = 0
    while guess != number:
        guess = int(input(f'Plese guess a number between 1 and {x} - '))
        if guess < number:
            print('Too low, try again!')
        if guess > number:
            print ('Too High, try again')
    print (f'Congrats, you found my number {number}')
    
x = int(input('Please choose the highest number to guees too - '))
guess(x)

