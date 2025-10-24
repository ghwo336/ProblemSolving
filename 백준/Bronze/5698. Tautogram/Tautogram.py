while True:
    li=list(input().split())
    if li[0]=='*':
        break
    fiv=1
    t=li[0].lower()[0]
    for x in li:
        if x.lower()[0]!=t:
            fiv=0
    if fiv:
        print('Y')
    else:
        print('N')
    
