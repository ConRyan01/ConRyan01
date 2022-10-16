#Simple app - paint calculator

#how much paint is needed

print('Paint Calculator')
print('Enter a wall size width, height in feet or press enter to stop')
print('example: 12.8')

#variables
walls=[] #List of walls measurements
gallons = 1/350 #one gallon of paint covers 350 sqft
total = 0 #total gallons to buy

#get user input
while True:
    s = input('Enter a wall size:')
    if len(s) == 0: break

    #verify the input
    sqft = s.split(',')
    if len(sqft) < 2:
        print ('Invalid Format')
        break

    #convert strings to ints
    w = int(sqft[0])
    h = int(sqft[1])
    item = [w,h]
    walls.append(item)
    print(f'Adding wall: {item}')

#calculate the numbers
print(f'You Entered {walls}')
for m in walls:
    w = m[0]
    h = m[1]
    s = w*h
    v = s * gallons
    total += v
    
print(f'You need to buy {round(total,2)} gallons of paint')
