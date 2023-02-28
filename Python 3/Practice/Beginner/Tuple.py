#Tuple ()

#Tuple is a fast list that cannot be modified

#create a Tuple
t=(1,2,3,4)
print(t)

#Access elements
print(f'Index: {t[0]}')
print(f'Slice: {t[2:]}')
print(f'Bool: {3 in t}')

#assignment
(x,y,z) = (1,2,3)
print(x)
print(y)
print(z)

#assignment
(x,y,z) = range(1,4)
print(x)
print(y)
print(z)