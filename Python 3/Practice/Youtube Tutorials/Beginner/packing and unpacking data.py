#packing and unpacking data

#problem with *arg and **kwarg is we can not use lists and dictionaries
#instead we have to pack and unpack data

#packing data
def pack(*nums):
    print(f'packed: {nums}')
    for x in nums:
        print(f'packed: {x}')

pack(1,2,3)

#unpacking data
def unpack(a,b,c):
    print('unpack')
    print(f'a = {a}')
    print(f'b = {b}')
    print(f'c = {c}')

num = [1,2,3]
unpack(*num)

#astericks basically means you will unpack or pack data

#dictionary issue
d = dict(name = 'Connor', age = 29, pet = 'dog')
print('packing dictionary')
pack(*d)

print('unpacking dictionary')
unpack(*d)

#packing a dictionary
def packdict(**nums):
    print(f'nums = {nums}')
    for k in nums:
        print(f'Packed: {k} = {nums[k]}')
packdict(name='Connor',age=28,pet='dog')

#unpacking a dictionary
def unpackdict(name,age,pet):
    print('unpacking a dictionary')
    print(f'Name = {name}')
    print(f'age = {age}')
    print(f'pet = {pet}')

d = dict(name = 'Connor', age = 29, pet = 'dog')
unpackdict(**d)