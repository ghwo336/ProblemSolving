n=int(input())
for x in range(n):
    a,b=input().split()
    a=int(a)
    start=ord(b)-65
    for y in range(a):
        k=start+y
        if k>25:
            k-=26
        print(chr(k+65)*(y+1))
    print("")
            