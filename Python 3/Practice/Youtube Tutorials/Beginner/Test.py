#int
ival = 34
print(f'ival = {ival}')

#float
fval = 3.14
print(f'fval = {fval}')
import sys
print(sys.float_info)

#complex
cval = 3 + 6j
print (f'cval = {cval}')
cval = complex(5,3)
print(f'cval = {cval}')
print(f'real = {cval.real}, imag = {cval.imag}')