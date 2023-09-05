#!/usr/bin/python3
"""
Prime game module.
"""


def isWinner(x, nums):
    # Define a function to determine if a number is prime
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Initialize a dictionary to store game results for each round
    results = {}

    # Iterate through each round
    for n in nums:
        # Initialize a dictionary to memoize game results for this round
        memo = {}

        # Define a recursive function to determine the winner of the game
        def can_win(num):
            # Check if this game state has already been calculated
            if num in memo:
                return memo[num]

            # If the number is 1, the player cannot make a move and loses
            if num == 1:
                memo[num] = False
            else:
                # Assume the current player loses
                memo[num] = False

                # Check if there is a prime number that can be chosen
                for i in range(2, num + 1):
                    if is_prime(i):
                        """
                        If a prime number is found, check the subgame
                        after removing multiples
                        """
                        subgame_result = can_win(num - i)
                        if not subgame_result:
                            """
                            If the subgame result is False, the
                            current player wins
                            """
                            memo[num] = True
                            break

            return memo[num]

        # Calculate the winner for the current round
        winner = "Maria" if can_win(n) else "Ben"

        # Store the result for this round
        results[n] = winner

    # Count the number of rounds won by each player
    maria_wins = results.values().count("Maria")
    ben_wins = results.values().count("Ben")

    # Determine the overall winner based on the number of rounds won
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
