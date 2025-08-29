di={0:350.34,
   1:230.90,
   2:190.55,
   3:125.30,
   4:180.90}

t=int(input())
for x in range(t):
    dap=0.00
    li=list(map(int,input().split()))
    for y in range(5):
        dap+=li[y]*di[y]
    print(f'${dap:.2f}')