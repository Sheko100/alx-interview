#!/usr/bin/python3
"""Module for solving a prime numbers game
"""


def isWinner(x, nums):
    """returns the winner between 2 players playing the prime game
    """
    total_ben = 0
    total_maria = 0
    winner = None

    if len(nums) < 1:
        return None

    while x > 0:
        maria = 0
        ben = 0
        maria_played = False
        num_set = list(range(1, nums[x - 1] + 1))
        for n in num_set:
            if is_prime(n):
                if not maria_played:
                    maria += 1
                    maria_played = True
                else:
                    ben += 1
                    maria_played = False

        if maria_played:
            total_maria += 1
        else:
            total_ben += 1

        x -= 1

    if total_ben > total_maria:
        winner = 'Ben'
    elif total_maria > total_ben:
        winner = 'Maria'

    return winner


def is_prime(num):
    """Determines if the passed number is a primary number or not
    """

    if num % 2 == 0 and num > 2:
        return False
    elif num == 1 or num % 2 > 1:
        return False

    return True
