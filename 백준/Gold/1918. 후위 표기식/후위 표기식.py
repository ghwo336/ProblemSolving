di={'+':1,'-':1,'*':2,'/':2,'(':0,')':0}
a=input()
st=[]
dap=''
for x in a:
    if x not in di:
        dap+=x
    else:
        if not st:
            st.append(x)
        elif x=='(':
            st.append(x)
        elif x==')':
            while st[-1]!='(':
                dap+=st.pop();
            st.pop()
        else:
            if di[st[-1]]<di[x]:
                st.append(x)
            else:
                while (st) and di[st[-1]]>=di[x]:
                    dap+=st.pop()
                st.append(x)
while st:
    dap+=st.pop()
print(dap)
        
        
