n=int(input())
for x in range(n):
    dap=0
    a=input()
    s=set()
    for y in a:
        s.add(y)
    for x in range(26):
        if chr(65+x) not in s:
            dap+=(65+x)
    print(dap)
            