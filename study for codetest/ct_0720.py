n = int(input())

dp = [0,0,1,1]
if n>=4:
    for i in range(4, n+1):
        print(dp)
        value1 = 1 + dp[i-1]
        value2 = 1 + dp[i-1]
        value3 = 1 + dp[i-1]

        if i % 3 ==0:
            value3 = 1 + dp[i//3]
        if i % 2 ==0:
            value2 = 1 + dp[i//2]
        dp.append(min(value1, value2, value3))
    
print(dp[n])