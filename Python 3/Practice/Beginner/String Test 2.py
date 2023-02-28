str = "Hello World, this is a string! "

print(len(str)) #get length
print(str * 3) #Repeat
print(str.replace("Hello", "Hola")) #Replace
print(str.split(',')) #split
print(str.capitalize())

#slicing - or getting a sub string
print(str[0:5])
print(str[6:])
print(str[-8:])

#index - the position of
c = str.find('H') #-1 if not found
print(f'find returned {c}')