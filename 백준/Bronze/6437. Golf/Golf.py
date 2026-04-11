dap=0
while True:
    a,b=map(int,input().split())
    dap+=1
    if a==0:
        break
    print(f'Hole #{dap}')
    if b==1:
        print("Hole-in-one.")
    elif b==a-3:
        print('Double eagle.')
    elif b==a-2:
        print('Eagle.')
    elif b==a-1:
        print('Birdie.')
    elif b==a:
        print('Par.')
    elif b==a+1:
        print('Bogey.')
    else:
        print('Double Bogey.')
    print('')