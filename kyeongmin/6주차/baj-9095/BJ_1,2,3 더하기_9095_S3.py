import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    dp = [0] * 100
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4,12):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
        if N == i: break
    
    print(dp[N])