n=int(input())
for x in range (n):
    li=list(map(int,input().split()))
    print(*li)
    s=set(li)
    
    if 17 in s and 18 in s:
        print("both")
    elif 17 in s:
        print("zack")
    elif 18 in s:
        print("mack")
    else:
        print("none")
    print("")