n,m = input().split(' ')
my_array = list(input().split(' '))
A = set(input().split(' '))
B = set(input().split(' '))

happiness = 0

for i in my_array:
    happiness += (i in A) - (i in B)

print(happiness)