a=input()
for x in a:
    now=str(ord(x))
    fiv=0
    for y in now:
        fiv+=int(y)
    print(x*fiv)
    