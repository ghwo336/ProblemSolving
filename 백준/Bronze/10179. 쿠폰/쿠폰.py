t=int(input())
for x in range(t):
    a=float(input())
    b=int(a*1000);
    b=b*4//5
    if (b%10>=5):
        b-=b%10;
        b+=10;
    else:
        b-=b%10;
    print(f"${b/1000:.2f}")