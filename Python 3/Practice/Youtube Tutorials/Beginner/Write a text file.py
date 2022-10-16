#Write  a text file

import os

#simplify mode usage
def toFile(filename,mode,data):
    f = open(filename,mode)
    for i in range(5):
        f.write(str(i)+': ' + data + '\r\n')
    f.close()

#write will overwrite the entire file
def writeFile(filename):
    toFile(filename,'w','Hello World')

#append will add to the end of the file
def appendFile(filename):
    toFile(filename,'a','Hello again')

#read the file
def readFile(filename):
    if not os.path.exists(filename):
        print('file not found')
        return
    f = open(filename, 'r')
    for line in f.readlines():
        print(line)
    #print(f.read())    use for only smaller file sizes
    f.close()

#see it in action
myfile = 'hello.txt'
writeFile(myfile)
appendFile(myfile)
readFile(myfile)
