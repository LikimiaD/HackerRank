for _ in range(int(input())):
    g1, x = input(), set(map(int,input().split(' ')))
    g2, y = input(), set(map(int,input().split(' ')))
    print(x.issubset(y))