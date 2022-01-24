g1, x = input(), set(map(int,input().split(' ')))
g2, b = input(), set(map(int,input().split(' ')))
list  = list(x.union(b))
list.sort()
for item in list:
    if not item in x.intersection(b):
        print(item)