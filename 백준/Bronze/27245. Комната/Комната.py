w=int(input())
r=int(input())
h=int(input())
if min(w,r)>=2*h and max(w,r)<=2*min(w,r):
    print("good")
else:
    print("bad")