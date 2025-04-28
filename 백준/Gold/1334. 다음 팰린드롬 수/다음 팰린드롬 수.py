n=input()
l=len(n)
#f는 무지성 앞의수로 만든 펠린드롬
f=''
#짝수
if l%2==0:
    front=''
    for x in range(l//2):
        f+=n[x]
    front=f
    f=f+f[::-1]
    #커졌잖아 한 잔해
    if f>n:
        print(f)
    #문제 상황 안커졌을 때
    else:
        if len(front)==len(str(int(front)+1)):
            fiv=str(int(front)+1)
            print(fiv+fiv[::-1])
            # 여기는 9789 처러
        else:
            print(int(f)+2)
            #9999같은거 처리
else:
    #front는 앞의 수
    front=''
    #mid는 가운데 수
    mid=n[l//2]
    for x in range(l//2):
        f+=n[x]
    front=f
    f=f+mid+f[::-1]
    #커졌잖아 한 잔해
    if f>n:
        print(f)
    # 문제상황 안 커졌을 때
    else:
        if n=='9':
            print(11)
        else:
            if mid!='9':
                print(front+str(int(mid)+1)+front[::-1])
            else:
                if len(str(int(front)+1))==len(front):
                    front=str(int(front)+1)
                    print(front+'0'+front[::-1])
                else:
                    print(int(f)+2)
    
    
    
    
