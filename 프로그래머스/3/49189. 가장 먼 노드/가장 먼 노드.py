from collections import deque
def solution(n, edge):
    graph=[[] for _ in range(n+1)]
    answer = 0
    for x in edge:
        graph[x[0]].append(x[1])
        graph[x[1]].append(x[0])
    dp=[20001 for _ in range(n+1)]
    dq=deque()
    dq.append((1,0))
    while dq:
        now,dis=dq.popleft()
        if dp[now]>dis:
            dp[now]=dis
            for x in graph[now]:
                if dis+1<dp[x]:
                    dq.append((x,dis+1))
    fiv= max(dp[1:])
    for x in dp:
        if x==fiv:
            answer+=1
    return answer