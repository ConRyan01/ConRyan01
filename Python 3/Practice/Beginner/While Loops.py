#while loop

x=0
while x <= 10:
    print(f'x = {x}')
    x+=1
print('test 1 is done')

#Pass
#x=0
#while x < 10:
  #  pass #can cause a loop forever
#print('test 2 is done')

#continue and break
x = 0
while True: #loop forever
    x+=1
    if x < 5:
        print(f'x < 5 {x}')
        continue
    print(f'Do something {x}')

    if x == 10:
        print(f'exiting x = {x}')
        break
    
print('Complete')
