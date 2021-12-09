def print_formatted(number):
    padding = number.bit_length()
    for i in range(1,number+1): print(f"{i:{padding}d} {i:{padding}o} {i:{padding}X} {i:{padding}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)