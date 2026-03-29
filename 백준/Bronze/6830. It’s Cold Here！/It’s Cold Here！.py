dap=''
fiv=202
while True:
    try:
        a,b=input().split()
        b=int(b)
        if fiv>b:
            dap=a
            fiv=b
    except:
        print(dap)
        break