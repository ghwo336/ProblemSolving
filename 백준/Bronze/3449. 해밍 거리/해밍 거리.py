t=int(input())
for _ in range(t):
    a=input()
    b=input()
    dap=0
    for x in range(len(a)):
        if a[x]!=b[x]:
            dap+=1
    print(f'Hamming distance is {dap}.')