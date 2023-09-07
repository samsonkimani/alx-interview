#!/usr/bin/python3

def primes(n):
    """Return a list of prime numbers between 1 and n inclusive."""
    prime = []
    sieve = [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            prime.append(p)
            for i in range(p, n + 1, p):
                sieve[i] = False
    return prime

def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.
    """
    if x is None or nums is None or x == 0 or not nums:
        return None
    
    Maria = Ben = 0
    for limit in nums:
        prime_count = len(primes(limit))
        if prime_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None

