#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    iswinner method
    """

    def sieve(n):
        """
        sieve method
        """
        prime = [True for _ in range(n + 1)]
        p = 2
        while (p * p <= n):
            if prime[p]:
                for i in range(p * p, n + 1, p):
                    prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if prime[p]]

    def play_game(n):
        """ play_game method """
        primes = sieve(n)
        return 'Maria' if len(primes) % 2 != 0 else 'Ben'

    maria_wins = ben_wins = 0
    for n in nums:
        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
