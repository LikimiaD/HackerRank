if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        line = input().split()
        if line[0] == "insert": a.insert(int(line[1]),int(line[2]))
        if line[0] == "print": print(a)
        if line[0] == "remove": a.remove(int(line[1]))
        if line[0] == "append": a.append(int(line[1]))
        if line[0] == "sort": a.sort()
        if line[0] == "pop": a.pop()
        if line[0] == "reverse": a.reverse()
