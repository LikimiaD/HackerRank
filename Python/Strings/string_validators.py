import re
if __name__ == '__main__':
    a = input()
    print(''.join(re.findall('[a-zA-Z0-9]',a)).isalnum())
    print(''.join(re.findall('[a-zA-Z]', a)).isalpha())
    print(''.join(re.findall("[0-9]",a)).isdigit())
    print(''.join(re.findall('[a-z]', a)).islower())
    print(''.join(re.findall('[A-Z]', a)).isupper())