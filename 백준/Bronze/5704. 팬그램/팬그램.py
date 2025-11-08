while True:
    s=set()
    a=input()
    if a=='*':
        break
    for x in a:
        s.add(x)
    pandan=True
    for x in range(26):
        if chr(97+x) not in s:
            pandan=False
    if pandan:
        print('Y')
    else:
        print('N')
        
        
    