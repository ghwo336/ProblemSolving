import math
def cal(n):
    a=0.0
    a+=((n**2)*((100-n)**16)/10**36)*math.comb(18,2)
    a+=((n**3)*((100-n)**15)/10**36)*math.comb(18,3)
    a+=((n**5)*((100-n)**13)/10**36)*math.comb(18,5)
    a+=((n**7)*((100-n)**11)/10**36)*math.comb(18,7)
    a+=((n**11)*((100-n)**7)/10**36)*math.comb(18,11)
    a+=((n**13)*((100-n)**5)/10**36)*math.comb(18,13)
    a+=((n**17)*((100-n)**1)/10**36)*math.comb(18,17)

    return 1-a


c=int(input())
d=int(input())
print(1.0-cal(c)*cal(d))
    