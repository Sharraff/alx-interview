#!/usr/bin/python3
"""Make Change"""


def makeChange(coins, total):
    """Sort the coins and reduce the total based on the largest coin"""
    coins.sort()
    neededCoins = 0
    while total > 0:
        if coins:
            coin = coins.pop()
        else:
            return -1
        neededCoins += (total // coin)
        total %= coin
    return neededCoins
