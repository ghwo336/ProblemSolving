a=0
b=0
n=int(input())
b=n//3
a=n%3
if a==1:
    b-=1
    a=2
elif a==2:
    a=1
print(a,b)