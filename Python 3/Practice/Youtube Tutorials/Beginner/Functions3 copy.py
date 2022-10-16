#functions in depth

#no arguments
def test():
    print('Normal Function')

print('\r\n------ No Arguments')
test()

#positional and keyword arguments
def message(name,msg,age):
    print(f'Hello {name}, {msg}, you are {age} years old')

print('\r\n\------- Positional and Keyword arguments')
message ('Connor', 'good morning', 27) #positional
message ('Connor', 22, 'good morning') #positional (wrong order)
message (msg = 'Good morning', age = 27, name = 'Connor') #keywords
message ('Connor', age = 27, msg = 'good morning') #both


#internal functions
def counter():
    def display(count = 0): #function in a function
        print(f'internal: {count}')
    for x in range(5): display(x)

print('\r\n----- Internal Functions')
counter()

# *args - positional variable length arguments
def multiple(*args):
    z=1
    for num in args:
        print(f'Num = {num}')
        z *= num
    print (f'multiply: {z}')
print('\r\n------ *args')
multiple(2,3,1)

# **kwargs is used to pass a keyworded, variable length arguments
def profile(**person):
    print(person)
    def display(k):
        if k in person.keys(): print(f'{k} = {person[k]}')
    display ('name')
    display ('age')
    display ('pet')

print('\r\n------- **Kwargs')
profile(name='Connor',age=27)
profile(name='Connor',age=27,pet = 'dog')
profile(name='Connor',age=27,pet = 'dog', food = 'pizza')

#lambda functions (anonymous functions)
print('\r\n------- Lamda')
#normal
def makesqft(width=0,height=0):
    return width*height
print(makesqft(width=10,height = 8))
print(makesqft(15.8))

#lamda
sqft= lambda width=0,height=0: width*height
print(sqft(width=10,height=8))
print(sqft(15,8))