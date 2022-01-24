def merge_the_tools(string, k):
    for x in range(0, len(string), k):
        g = ''
        for item in string[x : x+k]:
            if item not in g: g += item
        print(g)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)