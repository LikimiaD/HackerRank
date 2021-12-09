if __name__ == '__main__':
    input()
    x = input().split()
    for _ in range(len(x)): x[_] = int(x[_])
    print(sorted(set(x))[-2])
