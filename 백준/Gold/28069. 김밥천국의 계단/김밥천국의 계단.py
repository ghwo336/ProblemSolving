from collections import deque
n,k=map(int,input().split())
dp=[1000002 for _ in range(n+1)]
q=deque()
q.append((0,0))
while q:
    now,num=q.popleft()
    if now+1<=n and dp[now+1]>num+1:
        dp[now+1]=num+1
        q.append((now+1,num+1))
    if now+now//2<=n and dp[now+now//2]>num+1:
        dp[now+now//2]=num+1
        q.append((now+now//2,num+1))

if dp[n]<=k:
    print("minigimbob")
else:
    print("water")
        
    
    
