
while True:
    r0,w0,c,r=map(int,input().split())
    if r0+w0+c+r==0:
        break
    fiv=c*w0-r0
    if fiv%r==0:
        print(max(0,fiv//r))
    else:
        print(max(0,fiv//r+1))