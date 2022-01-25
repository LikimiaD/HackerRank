from itertools import product
print(*product(map(int, input().split(' ')), map(int, input().split(' '))))