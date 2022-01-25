from itertools import permutations
x,n = input().split(' ')
print(*[''.join(i) for i in permutations(sorted(x),int(n))],sep='\n')
