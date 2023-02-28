#intro to functions

#A function is a block of code which only runs when its called.
#You can pass data, known as parameters (or arguments), into a function.
#A function can return data as a result.

#note the difference between parameters and arguments
#Function parameters are the names listed in the function's definition.
#Function arguments are the real values passed to the function.
#parameters are initialized to the values of the arguments supplied.

#define a function
def test():
    print('This is a function')

#define a function with parameters
def sqft(w,h):
    v = w*h
    return v

#call a function
test()

#call a function multiple times
for x in range(4):
    test()

#call a function with parameters
x = sqft(12,8)
print(f'The Square footage is {x}')
