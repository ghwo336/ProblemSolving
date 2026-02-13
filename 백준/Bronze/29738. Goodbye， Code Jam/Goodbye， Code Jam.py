t=int(input())
for x in range(t):
    a=int(input())
    dap=0
    if a<=25:
        dap=0
    elif a<=1000:
        dap=3
    elif a<=4500:
        dap=2
    else:
        dap=1
    if dap:
        print(f'Case #{x+1}: Round {dap}')
    else:
        print(f'Case #{x+1}: World Finals')