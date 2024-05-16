#!/usr/bin/python3
"""
Prime Game
"""


def sieve(n):
    """
    Sieve of Eratosthenes to generate primes up to n
    """
    is_prime = [True] * (n + 1)
    p = 2
    while (p * p <= n):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    prime_list = [p for p in range(2, n + 1) if is_prime[p]]
    return prime_list

def remove_multiples(set_, prime):
    """
    Remove a prime and its multiples from the set
    """
    multiples = set()
    for num in set_:
        if num % prime == 0:
            multiples.add(num)
    return set_ - multiples

def play_game(n, primes):
    """
    Simulate the game for a given n
    """
    current_set = set(range(1, n + 1))
    turn = 0  # 0 for Maria, 1 for Ben
    while True:
        move_made = False
        for prime in primes:
            if prime in current_set:
                current_set = remove_multiples(current_set, prime)
                move_made = True
                break
        if not move_made:
            return 1 - turn  # if no move is made, the last player loses
        turn = 1 - turn  # switch turns

def isWinner(x, nums):
    """
    Winner of the Game
    """
    max_n = max(nums)
    primes = sieve(max_n)
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = play_game(n, primes)
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
