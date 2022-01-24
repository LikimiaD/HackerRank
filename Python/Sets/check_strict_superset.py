s, num = set(input().split(' ')), int(input())
count = 0
for _ in range(num):
    x = set(input().split(' '))
    if s.issuperset(x):
        count += 1
print(count==num)