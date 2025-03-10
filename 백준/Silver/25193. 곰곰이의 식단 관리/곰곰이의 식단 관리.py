import math
n=int(input())
c=0
d=0
a=input()
for x in a:
    if x=="C":
        c+=1
    else:
        d+=1
print(math.ceil(c/(d+1)))