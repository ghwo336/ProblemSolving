n=int(input())
for x in range(1,n+1):
    if x%77==0:
        print("Wiwat!")
    elif x%7==0:
        print("Hurra!")
    elif x%11==0:
        print("Super!")
    else:
        print(x)