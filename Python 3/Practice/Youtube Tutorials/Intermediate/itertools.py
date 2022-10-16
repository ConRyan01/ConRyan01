#product, permutations, combinations, accumulate, groupby, infinite iterators
from itertools import product
a = [1,2]
b = [3]
prod = product(a,b, repeat=2)
print(list(prod))

from itertools import permutations
a=[1,2,3]
perm = permutations(a)
print(list(perm))

from itertools import combinations
a = [1,2,3,4]
comb = combinations(a,2)
print(list(comb))