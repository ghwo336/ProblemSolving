n=int(input())
a=1
b=1
while n>a*b:
    a+=1
    if n>a*b:
        b+=1
print(a,b)