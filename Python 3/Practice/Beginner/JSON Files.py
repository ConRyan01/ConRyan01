#JSON Files
#app to app communications

"""
{
    name: Connor
    age: 27
    pet: Dog
}
"""

#imports
import json
filename = 'json.txt'

#To string
outD = dict(name = 'Connor', age = 27, pet='dog')
s = json.dumps(outD) #Dumps puts it to a string
print(f'String = {s}')

#To File
with open(filename, 'w') as f:
    json.dump(outD,f) #Dump puts it to a file

#From string
inD = json.loads(s) #Load the dictionary from the string
print(f'Dictionary = {inD}')

#From File
with open(filename,'r') as f:
    fD = json.load(f)
print(f'Type: {type(fD)} = {fD}')