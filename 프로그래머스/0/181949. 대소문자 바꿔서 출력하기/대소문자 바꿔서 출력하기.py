str = input()
for c in str:
    if c.isupper() is True:
        print(c.lower(), end='')
    else:
        print(c.upper(), end='')
