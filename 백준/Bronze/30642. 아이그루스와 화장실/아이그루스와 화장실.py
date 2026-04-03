a=int(input())
b=input()
c=int(input())
if b=='induck':
    if c%2==0:
        print(c)
    else:
        if c-1==0 and c!=a:
            print(c+1)
        else:
            print(c-1)
else:
    if c%2==1:
        print(c)
    else:
        print(c-1)