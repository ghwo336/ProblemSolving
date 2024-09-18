T=int(input())
for x in range(T):
    li=list(map(int,input().split()))
    hp=max(1,li[0]+li[4])
    mp=max(1,li[1]+li[5])
    a=max(0,li[2]+li[6])
    b=li[3]+li[7]
    print(hp+5*mp+2*a+2*b)