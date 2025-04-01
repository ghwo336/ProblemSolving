a=input()
if a[0]=='"' and a[-1]=='"'and a!='""' and len(a)>=2:
    print(a[1:len(a)-1])
else:
    print("CE")