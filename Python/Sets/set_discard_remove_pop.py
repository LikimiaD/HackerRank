input()
x = set(map(int, input().split()))
for _ in range(int(input())):
    __ = input().split()
    if len(__) == 1:
        x.pop()
    else:
        if __[0] == 'remove': x.remove(int(__[1]))
        if __[0] == 'discard': x.discard(int(__[1]))
print(sum(x))
