#flag height = k
#special jumping step = j
#default junmping step = 1

#Q: what is the min steps to get to the top

def flag(k, j):
    dp = [0 for i in range(j)]
    dp[1] = 1

    for i in range(2, k + 1):
        if i - j >= 0 and i % j == 0:
            dp[i % j] = min(dp[(i - j) % j], dp[(i - 1) % j]) + 1
        else:
            dp[i % j] = dp[(i - 1) % j] + 1
    return dp[k % j]

print flag(10, 5)