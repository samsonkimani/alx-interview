#!/usr/bin/python3
""" making changes"""

def makeChange(coins, total):
    """ make change function"""
    if total == 0:
        return 0
    if min(coins) > total:
        return -1
    dp = [-1 for i in range(0, total + 1)]
    for i in coins:
        if i > len(dp) - 1:
            continue
        dp[i] = 1
        for j in range(i + 1, total + 1):
            if dp[j - i] == -1:
                continue
            elif dp[j] == -1:
                dp[j] = dp[j - i] + 1
            else:
                dp[j] = min(dp[j], dp[j - i] + 1)
            #print(dp)
    return dp[total]
