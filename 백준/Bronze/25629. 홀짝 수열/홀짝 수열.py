N=int(input())
li=list(map(int,input().split()))
odd=0
even=0
for x  in li:
    if x%2==0:
        even+=1
    else:
        odd+=1
if N%2==0:
    if even==odd:
        print(1)
    else:
        print(0)
else:
    if even==odd-1:
        print(1)
    else:
        print(0)