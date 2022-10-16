#Walrus Operator and Global
#Added in Python 3.8 looks like :=

#Assign a variable from an expression
#must have the right version!

#common issues ( )
#y := len('hello') #not valid syntax
(y := len('hello')) #valid but not recommended
print(y)

people = ['Conno','Kaitland','Michelle']
if (n := len(people)) <= 3: print(n)

#simple example
lines = []

def canAdd(max=5):
    global lines #Allows us to ensure we are using the global variable
    if allowed := (count := len(lines)) <max:
        print(f'You can enter {max - count} more')
    return allowed

while canAdd():
    lines.append(l := input('enter a line:'))

print(f'You Entered: {lines}')