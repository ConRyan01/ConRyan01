#Errors and Exceptions
x = -5 
'''if x < 0:
    raise Exception('x should be positive')'''

#assert (x>=0), 'x is not positivte'

try:
    a = 5/0
except:
    print('cannot divide by 0')