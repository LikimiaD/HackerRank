x = input()
z = ''
for sym in x: z += sym.upper() if sym.isupper() == False else sym.lower()