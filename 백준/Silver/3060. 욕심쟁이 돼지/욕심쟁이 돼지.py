def sol():
    n=int(input())
    sumli=sum(list(map(int,input().split())))
    dap=1
    while True:
        if sumli>n:
            print(dap)
            break
        dap+=1
        sumli*=4


t=int(input())
for _ in range(t):
    sol()