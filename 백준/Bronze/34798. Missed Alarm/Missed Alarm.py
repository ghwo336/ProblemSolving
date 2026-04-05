a,b=map(int,input().split(':'))
c,d=map(int,input().split(':'))
if a>c:
    print('NO')
elif a==c and b>d:
    print('NO')
else:
    print('YES')
