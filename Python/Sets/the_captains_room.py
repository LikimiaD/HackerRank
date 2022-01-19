from collections import Counter
_, x = input(),map(int, input().split())
print(Counter(x).most_common()[-1][0])