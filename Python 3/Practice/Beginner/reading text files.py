#reading a text file

#get a file name
import os, sys

print(f'File: {__file__}') #Built in file name
print(f'Args: {sys.argv}')
sfile = os.path.abspath(sys.argv[0])
print(f'Reading: {sfile}')

#Exists
if not os.path.exists(sfile):
    print('File Not Found')
    #file not found error
    exit(1)

#open the file
#FileNotFoundError: wrong file path
f = open(sfile, 'r')

#read a line
line = f.readline()
print(line)

#read number of letters
chars = f.read(10)
print(f'Chars: *{chars}*')

#position
print(f'Position: {f.tell()} of {os.stat(sfile).st_size}')

#seek - move to a position in the file
#zero based
f.seek(0)

#read all lines
print('------------------------------')
for l in f.readlines():
    print(l.strip())

#close the file - whenever you open, you have to close by the end
f.close()