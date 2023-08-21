#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet
    a given amount total
    """
    if total <= 0:
        return 0
    
    # Initialize an array to store the minimum number of coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Calculate the minimum number of coins needed for each total
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[total] if dp[total] != float('inf') else -1
