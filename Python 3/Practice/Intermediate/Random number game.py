
import random

print('Welcome to the random number guessing game!')
topRange = input('Please enter an upper range integer: ')
bottomRange = input ('Please enter a lower range integer: ')
rannum = random.randrange(bottomRange,topRange)
ans = input(f'Guess a number between {bottomRange} and {topRange}: ')

if ans.isdigit == True:
    ans = int(ans)