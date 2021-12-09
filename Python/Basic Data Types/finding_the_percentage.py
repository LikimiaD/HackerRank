if __name__ == '__main__':
    student_marks = {}
    for _ in range(int(input())):
        line = input().split()
        student_marks[line[0]] = line[1:]
    query_name = input()

    val = 0
    for x in student_marks[query_name]:
        val += float(x)
    print("%.2f" % (val/len(student_marks[query_name])))