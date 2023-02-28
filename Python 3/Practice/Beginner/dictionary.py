#dictionary {k:v , k:v}
#indexed by keys, which can be any immutable type

#create a dictionary
d = {'pet' : 'dog','age' : 5, 'name' : 'spot'} #hard way
print(d)
d = dict(pet='dog',age=5,name='spot') #easy way
print(d)

#get keys and values
print(f'Items: {d.items()}')
print(f'keys: {d.keys()}')
print(f'Values: {d.values()}')

#getting a value from the key
print(f'Name: {d["name"]}')

#add an item
d['trick'] = 'sit'
print(d)

#remove an item
del d['trick']
print(d)