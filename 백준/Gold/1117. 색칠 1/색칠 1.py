w,h,f,c,x1,y1,x2,y2=map(int,input().split())
foldw=max(w-f,f)
foldh=h//(c+1)
whole=w*h
whitev=(x2-x1)*(y2-y1)
whitev+=max(0,(min(x2,min(w-f,f))-x1)*(y2-y1))
print(whole-(whitev)*(c+1))
    