#Lists []

#create a list - remember square brackets
x = ['Connor','Ryan',27] #can mix data types
print(f'List: {x}') #print list out
print(f'Length: {len(x)}') #print out length
print(f'My name is {x[0]}')

#adding items
x.append('pizza') #adds at end
x.insert(1,'beer') #adds at specific position
print(f'List: {x}')

#removing items - remove, pop, delete
x.remove('beer') #remove an item
print(f'{x}')

i = x.index('pizza') #will raise an error if not found
print(f'Food: {x.pop(i)}') #pop uses and delets item at the same time
print(f'List: {x}')

i = x.index(27)
del x[i] #delete permanantly deletes item
print(f'List: {x}')


y=['Cats', 'Dogs', 'Birds']
x.extend(y)
print(f'List: {x}')

#sort - sort, reverse. has issues with mixing numbers and strings
x.sort()
print(f'List: {x}')
x.reverse() #alphabatize but backwards
print(f'List: {x}')

#copy
y=x.copy() #copies elements into a new list
y.reverse()
y.append('Apples')
print(f'New: {y}')

#delete the whole thing
del y

#clear
x.clear()
print(f'cleared: {x}')

#Lists can contain other lists [[],[],[]]
x=[]
y=[1,2,3]
z=['Connor','Ryan']
x.append(y)
x.insert(0,z)
print(f'one item in list {x[0][1]}')

print(f'Lists in Lists: {x}')
