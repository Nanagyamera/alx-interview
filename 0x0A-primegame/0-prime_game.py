#!/usr/bin/python3
"""
Prime game module.
"""

def is_prime(num):
    if num <= 1:
        return False
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            return False
    return True

def isWinner(x, nums):
    if x < 1 or not nums:
        return None
    
    marias_wins, bens_wins = 0, 0

    for n in nums:
        # Determine the number of prime numbers in the range [1, n]
        primes_count = sum(1 for i in range(2, n + 1) if is_prime(i))
        
        # Update wins for Maria and Ben based on the count of prime numbers
        if primes_count % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
