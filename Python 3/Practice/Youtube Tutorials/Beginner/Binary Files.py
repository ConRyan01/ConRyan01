#working with binary files
#install hex editor
#right click and open with hex editor

#imports
import random
import operator

#create random bytes
def randomBytes(size):
    bytes = []
    for x in range(size):
        bytes.append(random.randrange(0,255))
    return bytes

def displayBytes(bytes):
    print("-"*20)
    for index,item in enumerate(bytes, start=1):
        print(f'{index} = {item} ({hex(item)}')
    print("-"*20)

#write bytes
def writeBytes(filename,bytes):
    with open(filename,'wb') as file:
        for i in bytes:
            file.write(i.to_bytes(1,byteorder='big'))

#read bytes
def readBytes(filename):
    bytes = []
    with open(filename, 'rb') as file:
        while True:
            b = file.read(1)
            if not b:
                break
            bytes.append(int.from_bytes(b, byteorder='big'))
    return bytes

#see it in action

#create random bytes
outbytes = randomBytes(10)
displayBytes(outbytes)

#write bytes
filename = 'test.txt'
writeBytes(filename,outbytes)

#read bytes
