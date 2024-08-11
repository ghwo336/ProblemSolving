a,b=map(int,input().split())
if a**2-b!=0:
    print(int(-a-(a**2-b)**0.5),int(-a+(a**2-b)**0.5))
else:
    print(int(-a+(a**2-b)**0.5))