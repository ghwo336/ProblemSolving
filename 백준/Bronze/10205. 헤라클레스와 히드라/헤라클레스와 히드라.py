t=int(input())
for x in range(1,t+1):
    print(f"Data Set {x}:")
    n=int(input())
    s=input()
    for y in range(len(s)):
        if s[y]=="b":
            n-=1
        else:
            n+=1
    print(n)
    print(" ")
