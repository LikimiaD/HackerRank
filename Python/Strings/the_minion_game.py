
string = 'BANANANAAAS'


vowels = 'AEIOUaeiou'
stuart = sum(len(string)-i if not string[i] in vowels else 0 for i in range(len(string)))
kevin = sum(len(string)-i if string[i] in vowels else 0 for i in range(len(string)))
[print('Draw') if kevin == stuart else print('Stuart %d' %stuart) if stuart > kevin else print('Kevin %d' %kevin)]

