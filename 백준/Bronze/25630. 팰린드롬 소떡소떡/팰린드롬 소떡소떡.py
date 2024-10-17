N=int(input())
s=input()
dap=0
for x in range(N//2):
    if s[x]!=s[N-1-x]:
        dap+=1
print(dap)



