import math

li=list(map(int,input().split()))


def sol():
    d=[]
    d.append([abs(li[0]-li[2]),abs(li[1]-li[3])])
    d.append([abs(li[0]-li[4]),abs(li[1]-li[5])])
    d.append([abs(li[2]-li[4]),abs(li[5]-li[3])])
    a1=d[0]
    a2=d[1]
    if (a1[0]//math.gcd(a1[0],a1[1])==a2[0]//math.gcd(a2[0],a2[1]) and a1[1]//math.gcd(a1[0],a1[1])==a2[1]//math.gcd(a2[0],a2[1])):
        print(-1.0)
        return;
    if a1[0]==0 and a2[0]==0:
        print(-1.0)
        return
    realD=[]
    realD.append(d[0][0]**2+d[0][1]**2)
    realD.append(d[1][0]**2+d[1][1]**2)
    realD.append(d[2][0]**2+d[2][1]**2)


    print((max(realD)**0.5-min(realD)**0.5)*2)

sol()