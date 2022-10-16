#Functions and Arguments

#Function in an argument
def test(name, age, pet):
    print(f'name = {name}')
    print(f'age = {age}')
    print(f'pet = {pet}')

def getData():
    return dict(name='Connor',age=28,pet='dog')

d=getData()
test(d['name'],d['age'],d['pet'])

test(**getData())

#function as an argument
def funky(kittens):
    d = kittens()
    print(f'd = {d}')
    print(f'Name: {d["name"]}')

funky(getData) #notice we are not calling the function, just passing it
