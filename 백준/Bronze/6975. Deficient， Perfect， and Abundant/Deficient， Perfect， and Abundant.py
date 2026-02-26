t=int(input())
for x in range(t):
    a=int(input())
    dap=0
    for x in range(1,a):
        if a%x==0:
            dap+=x
    if dap == a:
        print(f'{a} is a perfect number.')
    elif dap < a:
        print(f'{a} is a deficient number.')
    else:
        print(f'{a} is an abundant number.')
    print('')
        