a,b=map(int,input().split())
c,d=map(int,input().split())
e=a+d
f=b+c
if e>f:
    print('Persepolis')
elif e<f:
    print('Esteghlal')
else:
    if d>b:
        print('Persepolis')
    elif d<b:
        print('Esteghlal')
    else:
        print('Penalty')
        