#!/usr/bin/python3
"""
Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    """
    if x < 1 or not nums:
        return None
    marias_wins, bens_wins = 0, 0
    # generate primes with a limit of the maximum number in nums
    n = max(nums)
    primeNums = [True for _ in range(1, n + 1, 1)]
    primeNums[0] = False
    for i, is_prime in enumerate(primeNums, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primeNums[j - 1] = False
    # filter the number of primes less than n in nums for each round
    for _, n in zip(range(x), nums):
        primeNums_count = len(list(filter(lambda x: x, primeNums[0: n])))
        bens_wins += primeNums_count % 2 == 0
        marias_wins += primeNums_count % 2 == 1
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
