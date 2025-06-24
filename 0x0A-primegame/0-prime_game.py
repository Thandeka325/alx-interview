#!/usr/bin/python3
"""
Prime Game Winner Module
"""


def isWinner(x, nums):
    """
    Determines the winner of each round and returns the overall winner.
    Maria always starts first.
    """
    if not nums or x < 1:
        return None

    max_n = max(nums)
    # Sieve of Eratosthenes to get prime counts up to max_n
    is_prime = [False, False] + [True for _ in range(2, max_n + 1)]
    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Precompute number of primes up to index i
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if is_prime[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
