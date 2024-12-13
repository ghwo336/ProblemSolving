a,b=map(int,input().split())
if b%2==0:
    b//=2
else:
    b//=2
    b+=1
if a>=b:
    print("E")
else:
    print("H")