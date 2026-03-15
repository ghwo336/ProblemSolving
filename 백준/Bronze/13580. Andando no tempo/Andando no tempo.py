li=list(map(int,input().split()))
if (len(set(li)))<3:
    print('S')
else:
    li.sort()
    if li[0]+li[1]==li[2]:
        print('S')
    else:
        print('N')