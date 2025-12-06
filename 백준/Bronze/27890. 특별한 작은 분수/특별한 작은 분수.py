a,b=map(int,input().split())
for x in range(b):
    if a%2==0:
        a=int(a/2)^6
    else:
        a=int(2*a)^6
print(a)