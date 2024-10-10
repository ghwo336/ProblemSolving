storage={'*','+','-','/'}
N=int(input())
st=[]
di=dict()
s=input()
for x in range(N):
    di[chr(65+x)]=int(input())
for x in s:
    if x in storage:
        second=st.pop()
        first=st.pop()
        if x=='*':
            st.append(first*second)
        elif x=='+':
            st.append(first+second)
        elif x=='-':
            st.append(first-second)
        else:
            st.append(first/second)
    else:
        st.append(di[x])
dap=st.pop()
print(f'{dap:.2f}')