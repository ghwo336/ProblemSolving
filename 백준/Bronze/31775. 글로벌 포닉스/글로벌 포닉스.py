s1=input()
s2=input()
s3=input()
s=set()
s.add(s1[0])
s.add(s2[0])
s.add(s3[0])
if (len(s)==3 and 'l' in s and 'k' in s and 'p' in s):
    print("GLOBAL")
else:
    print("PONIX")