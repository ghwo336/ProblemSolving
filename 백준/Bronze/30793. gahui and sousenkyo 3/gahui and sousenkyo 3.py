a,b=map(int,input().split())
if b*2>a*10:
    print('weak')
elif b*4>a*10:
    print('normal')
elif b*6>a*10:
    print('strong')
else:
    print('very strong')