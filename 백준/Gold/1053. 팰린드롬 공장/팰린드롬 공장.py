reals=list(input())
l=len(reals)
dap=10000000000000
for p in range(l):
    for q in range(l):
        s=[]
        for z in reals:
            s.append(z)
        s[p],s[q]=s[q],s[p]
        dp=[[0 for _ in range(l)] for _ in range(l)]
        # 길이 2인 펠린드롬 dp[a][b]==팰린드롬이 되기까지 a~b 까지 필요한 방법수
        for i in range(l-1):
            if s[i]!=s[i+1]:
                dp[i][i+1]=1
        
        #길이가 3이상
        for x in range(2,l):
            for start in range(l-x):
                dp[start][start+x]=min(dp[start+1][start+x]+1,dp[start][start+x-1]+1)
                if s[start]==s[start+x]:
                    dp[start][start+x]=min(dp[start+1][start+x-1],dp[start][start+x])
                else:
                    dp[start][start+x]=min(dp[start+1][start+x-1]+1,dp[start][start+x])
        if p!=q:
            dp[0][l-1]+=1
        dap=min(dap,dp[0][l-1])
        
print(dap)
        