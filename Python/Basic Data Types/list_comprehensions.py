if __name__ == '__main__':
    x,y,z,n = int(input()),int(input()),int(input()),int(input())
    g = []
    for num1 in range(x+1):
        for num2 in range(y+1):
            for num3 in range(z+1):
                if num1 + num2 + num3 != n:
                  g.append([num1,num2,num3])
    print(g)