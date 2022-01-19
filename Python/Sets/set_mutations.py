_, x = input(), set(input().split())
for _ in range(int(input())):
    eval('x.{0}({1})'.format(input().split()[0], input().split()))
print(sum(map(int,x)))