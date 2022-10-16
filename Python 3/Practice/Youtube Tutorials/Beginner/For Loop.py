#For loop and range

#for loop on lists, tuples, and sets
x = [1,2,3,4] #list
t = (1,2,3,4) #Tuple
s = {1,2,3,4} #Set

for i in s:
    print(f'i = {i}')

#for loop in dictionaries
x = dict(Connor = 27, Kaitland = 26, Roxy = 10)
print(x)

for k in x.keys():
    print(f'keys: {k} = {x[k]}')

for k,v in x.items():
    print(f'Keys: {k} = {v}')

#Range
x = range(5)
print(x)
for i in x:
    print(f'Range: {i}')

#Range start, stop and step
x = range (5,20,3)
print(x)
for i in x:
    print(f'Stepped: {i}')