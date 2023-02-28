#global

#global keyword which allows code to modify a variable
#outside of the current scope
x = 1
def test():
    x = 6
    print(x)

test()
print(x)

#global variable
counter = 0

#scope issues
def count(max):
    #without *global", python is confused
    global counter
    counter += 1
    if counter >= max: return False
    else: return True

#global keyword in action
limit = 5
for x in range(limit):
    b = count(limit)
    print(counter)

count(1)