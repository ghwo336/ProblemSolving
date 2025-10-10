while True:
    m=int(input())
    n=m**2
    dap=0
    if n==0:
        break
    for x in range(1,int(n**0.5)+2):
        if n%x==0 and x<n//x:
            hap=n//x
            cha=x
            if (hap+cha)%2==0 and hap-cha>2*m:
                dap+=1
    print(dap)
            
        