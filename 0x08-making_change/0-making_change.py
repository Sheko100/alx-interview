#!/usr/bin/python3
"""
Coin Change Problem
"""


def makeChange(coins, total):
    """Calculates the minimum number of coins for change"""

    if total <= 0:
        return 0

    coins.sort(reverse=True)

    total_coins = 0

    for value in coins:
        if total >= value:
            rest = total % value
            coins = (total - rest) // value
            coins_value = coins * value
            total_coins += coins
            total -= coins_value

            if total == 0:
                break

    if total > 0:
        return -1

    return total_coins
