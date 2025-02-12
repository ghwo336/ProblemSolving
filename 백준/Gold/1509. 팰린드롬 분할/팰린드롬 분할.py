a=input()
l=len(a)

#isPal[n][m]==n번부터 m 번까지 펠린드롬인가?
isPal=[[False for _ in range(l)] for _ in range(l)]
dp=[2500 for _ in range(l+1)]
dp[-1]=0

#길이가 1인 펠린드롬 저장
for x in range(l):
    isPal[x][x]=True
    
# 길이가 2인 펠린드롬 저장
for x in range(1,l):
    if a[x]==a[x-1]:
        isPal[x-1][x]=True

#길이가 3 이상인 펠린드롬 저장: palen= 펠린드롬 길이
for palen in range(3,l+1):
    for start in range(l-palen+1):
        end=start+palen-1
        if a[start]==a[end] and isPal[start+1][end-1]:
            isPal[start][end]=True

#dp 갱신

for end in range(l):
    for start in range(end+1):
        if isPal[start][end]:
            dp[end]=min(dp[end],dp[start-1]+1)
        else:
            dp[end]=min(dp[end],dp[end-1]+1)

print(dp[-2])