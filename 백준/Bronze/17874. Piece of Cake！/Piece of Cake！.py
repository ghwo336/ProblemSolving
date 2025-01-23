a,b,c= map(int,input().split())
rm=max(b*c,(a-b)*c,b*(a-c),(a-b)*(a-c))
print(4*rm)