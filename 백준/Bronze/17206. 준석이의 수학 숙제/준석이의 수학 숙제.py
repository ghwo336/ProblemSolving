n=int(input())
li=list(map(int,input().split()))
for x in li:
    dap=0
    three=(x//3)*3
    seven=(x//7)*7
    cha=(x//21)*21
    dap+=((3+three)*(x//3)//2)
    dap+=((7+seven)*(x//7)//2)
    dap-=((21+cha)*(x//21)//2)
    print(dap)