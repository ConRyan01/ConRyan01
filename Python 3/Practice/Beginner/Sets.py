#sets {}
#sets contain unordered, unique, immutable data types in a hash table

#creating a set
s = {1,2,2,2,3,4,5}
print(s)

l = ['Connor','Ryan',27]
s = set(l)
print(s)

#adding items to a set
s.add('Hello')
s.update([1,2,3,'Hello'])
print(s)

#removing items
s.discard('Hello') #will not throw an error
s.remove(3) #will throw an error
v = s.pop() #takes a random item since its a set
print(s)

x = set('abcd') 
y = set('cdefg')

s = x.union(y) #all elements in either set
print(f'Union {s}')

s = x.intersection(y) #all elements in common
print(f'intersection {s}')

s = x.difference(y) #all elements x has but y does not
print (f'Difference {s}')

s = x.symmetric_difference(y) #all elements that neither set has in common
print (f'symmetric difference {s}')