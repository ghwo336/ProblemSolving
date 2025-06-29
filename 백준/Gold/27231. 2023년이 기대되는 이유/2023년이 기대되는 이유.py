

t=int(input())
for _ in range(t):
    st=set()
    n=list(input())
    l=len(n)
    if (len(n)==1 and n[0]!='1'):
        print(1)
    elif set(n)=={'1'} or set(n)=={'1', '0'}:
        print("Hello, BOJ 2023!")
    else:
        def b(index,path):
            if index == len(n):
                st.add(sum(map(int,path)))
                return
            path[-1] += n[index]
            b(index+1,path[:])
            path[-1]=path[-1][:-1]
            path.append(n[index])
            b(index+1,path[:])
            path.pop()
        b(1,[n[0]])
        fiv=max(st)
        li=list(map(int,n))
        dap=0
        for m in range(1,36):
            f=0
            for x in li:
                f+=x**m
            if f>fiv:
                break
            if f in st:
                dap+=1
        print(dap)

            
        