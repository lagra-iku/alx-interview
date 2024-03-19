#!/usr/bin/env python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n,
write a method that calculates the fewest number of
operations needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    if n == 1:
        return 0
    opns = 0
    current = 1
    i = 0
    while current < n:
        if n % current == 0:
            i = current
            opns += 1
        current += i
        opns += 1
    if current == n:
        return opns
    else:
        return 0
