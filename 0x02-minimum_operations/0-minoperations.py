#!/usr/bin/env python3

"""
finding the minimum number of operations
to copy and paste
"""


def minOperations(n: int) -> int:
    """ minoperations"""
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n = n // divisor

        else:
            divisor += 1

    return operations
