t=int(input())

def sol(st,limit,target):
    if limit==1:
        print(st)
        return
    for x in range(10):
        now=str(x)+st
        if len(now)>limit:
            return
        if int(now)**3%(10**limit)==target:
            print(int(now))
            return
        if str(target)[-len(now):]==str(int(now)**3)[-len(now):]:
            sol(now,limit,target)

for _ in range(t):
    s=input()
    if s[-1]=='1':
        sol('1',len(s),int(s))
    if s[-1]=='3':
        sol('7',len(s),int(s))
    if s[-1]=='7':
        sol('3',len(s),int(s))
    if s[-1]=='9':
        sol('9',len(s),int(s))
        
        