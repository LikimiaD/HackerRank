if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name,score))
    for s in sorted([s for s,g in students if g==sorted(set([x[1] for x in students]))[1]]): print(s)