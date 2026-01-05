n=int(input())
for _ in range(n):
    m=int(input())
    a=input()
    dap=1
    now=0
    if a[0]!='M':
        print('NO')
    else:
        while True:
            try:
                if a[now]=='M':
                    if a[now+1]=='I' and a[now+2]=='T':
                        now+=3
                    else:
                        dap=0
                        break
                elif a[now]=='I':
                    if a[now+1]=='T':
                        now+=2
                    else:
                        dap=0
                        break
                else:
                    dap=0
                    break
                if now==m:
                    break
            except:
                dap=0
                break
        if dap:
            print('YES')
        else:
            print('NO')