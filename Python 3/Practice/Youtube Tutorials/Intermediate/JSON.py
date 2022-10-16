from fileinput import close
import json

person = {'name': 'Connor','age': 28, 'city':'Wilmington','hasChildren':False, 'titles':['engineer','programmer']}

personJSON = json.dumps(person, indent=5, sort_keys=True)
print(personJSON)

'''with open('person.json', 'w') as file:
    json.dump(person, file, indent = 5)
    close'''

with open('person.json','r') as file:
    person = json.load(file)
    print(person)