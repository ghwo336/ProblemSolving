p=int(input())
while True:
    n=int(input())
    if n==0:
        break
    if n%p==0:
        print(f'{n} is a multiple of {p}.')
    else:
        print(f'{n} is NOT a multiple of {p}.')