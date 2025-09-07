t=int(input())
for x in range(t):
    a=int(input())
    print(f'Case {x+1}:')
    for y in range(1,a+1):
        start=y
        end=a-y
        if start<=end:
            if end<=6:
                print(f'({start},{end})')