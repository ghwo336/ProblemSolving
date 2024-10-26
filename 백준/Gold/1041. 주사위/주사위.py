N=int(input())
storage=list(map(int,input().split()))
a=[storage[0],storage[5]]
b=[storage[1],storage[4]]
c=[storage[2],storage[3]]
storage.sort()
d=[min(a),min(b),min(c)]
d.sort()
two=d[0]+d[1]
three=min(a)+min(b)+min(c)
if N==1:
    print(sum(storage)-storage[5])
else:
    print(4*three+storage[0]*(5*(N-2)**2+4*(N-2))+two*(8*N-12))