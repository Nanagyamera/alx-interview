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

    # Create a memoization table to store the results of subproblems
    memo = [float('inf')] * (total + 1)
    memo[0] = 0

    def dp(amount):
        if memo[amount] != float('inf'):
            return memo[amount]

        for coin in coins:
            if amount - coin >= 0:
                memo[amount] = min(memo[amount], dp(amount - coin) + 1)

        return memo[amount]

    result = dp(total)
    return result if result != float('inf') else -1
