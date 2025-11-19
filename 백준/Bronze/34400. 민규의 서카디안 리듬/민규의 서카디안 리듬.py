t=int(input())
for x in range(t):
    a=int(input())
    a%=25
    if a>=17:
        print('OFFLINE')
    else:
        print('ONLINE')