s=int(input())
m,f,b=map(int,input().split())
if s<=240 or s<=m+f+b:
    print("high speed rail")
else:
    print("flight")