start=int(input())
n=int(input())
for x in range(n):
    a=input()
    b=int(input())
    if a=='+':
        start+=b
    else:
        start-=b
print(start)