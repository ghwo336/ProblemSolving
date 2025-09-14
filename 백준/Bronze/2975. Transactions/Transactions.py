while True:
    li=list(input().split())
    a=int(li[0])
    b=int(li[2])
    if a==0 and b==0:
        break
    if li[1]=='W':
        if a-b<-200:
            print('Not allowed')
        else:
            print(a-b)
    else:
        print(a+b)