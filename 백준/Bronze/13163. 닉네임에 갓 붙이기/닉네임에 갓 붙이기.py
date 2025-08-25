n=int(input())
for x in range(n):
    a,b=input().split(" ",1)
    print("god",end='')
    for y in b:
        if y!=' ':
            print(y,end='')
    print('')