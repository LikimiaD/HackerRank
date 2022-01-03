import string
size = 10
mid_line = '-'.join([string.ascii_letters[size - x] for x in range(1, size)] + [string.ascii_letters[x] for x in range(size)])
lines = []
for x in range(2,size+1):
    main = ''.join(string.ascii_letters[size - x] for x in range(1, x))
    *main_list,_ = list(main)
    reverse = ''.join(x for x in reversed(main_list))
    line = '-'.join(main+reverse)
    num = (len(mid_line)-len(line)) // 2
    output_line = '-' * num  + line + '-' * num
    lines.append(output_line)
    
[print(x) for x in lines]
print(mid_line)
[print(x) for x in reversed(lines)]