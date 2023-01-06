# 냅색 DP

N, K = map(int, input().split())

# N,K의 2차열배열 만들기
dp = [[0]*(K+1) for _ in range(N+1)]

obj = [(0, 0)]

for _ in range(N):
  obj.append(tuple(map(int, input().split())))

for i in range(1, N+1):
  for j in range(1, K+1):
    W = obj[i][0]
    V = obj[i][1]
    if W <= j:
      dp[i][j] = max(V+dp[i-1][j-W], dp[i-1][j])
    else: 
        dp[i][j] = dp[i-1][j]
    
print(dp[N][K])




