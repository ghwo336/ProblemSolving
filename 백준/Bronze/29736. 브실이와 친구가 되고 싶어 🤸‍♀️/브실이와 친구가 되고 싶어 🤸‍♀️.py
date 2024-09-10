a,b=map(int,input().split())
k,x=map(int,input().split())
if k-x>b:
    print("IMPOSSIBLE")
elif k+x<a:
    print("IMPOSSIBLE")
else:
    start=max(k-x,a)
    end=min(k+x,b)
    print(end-start+1)