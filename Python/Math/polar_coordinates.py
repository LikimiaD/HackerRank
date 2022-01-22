from cmath import phase
from math import sqrt
from re import findall

x = findall('-?[0-9][0-9]?', input())
print('{}\n{}'.format(
    sqrt(pow(int(x[0]),2) + pow(int(x[1]),2)),
    phase(complex(int(x[0]),int(x[1])))
))