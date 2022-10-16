#Functions and Scope

#Lexical scoping (sometimes known as statiac scoping)
#is a convention used with many programming languages that sets the scope
#(range of functionality) of a variable so that i may only be called 
#from within the block of code in which it is defined
#Scopes can be nested inside another

name = 'Connor Ryan'

#functions can access the global scope
def test1():
    print(f'My name is: {name}')

test1()

#Global scope can not access function scope
x = 10
def test2():
    x = 50
    print(f'Function scope {x}')

test2()
print(f'Global scope {x}')

#global > function > statement
x = 15
print(f'Global x: {x}')
def test3():
    x=0
    print(f'function x: {x}')
    for i in range(3):
        x += 1
        y = x * i
        print(f'statement x: {x}')
        print(f'statement y: {y}')
    print (f'function x: {x}')
    print (f'function y: {y}') #this could become an issue be careful
test3()
print(f'Global x: {x}')

#functions do not share scope with each other
def cats():
    z = 1 #only exists in this function
def dogs():
    z = 3 #only exists in this function
  
#functions can return vlaues
def numbers(steps):
    l = range(1,20,steps)
    for i in l:
        print(i)
    return l

def lotto():
    z = numbers(3)
    for x in z:
        print (f'lucky number {x}')

lotto()