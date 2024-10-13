a,b=map(int,input().split())
if a==b:
    if a==0:
        print("Not a moose")
    else:
        print("Even",2*a)
else:
    print("Odd",max(a,b)*2)