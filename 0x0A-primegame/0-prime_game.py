#!/usr/bin/python3
"""
Prime game module.
"""


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    maria_wins, ben_wins = 0, 0

    for n in nums:
        # Determine the number of prime numbers in the range [1, n]
        primes_count = sum(1 for i in range(2, n + 1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1)))

        # Update wins for Maria and Ben based on the count of prime numbers
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    return 'Maria' if maria_wins > ben_wins else 'Ben'
