#LeetCode: https://leetcode.com/problems/coin-change/description/

# Dynamic Programming using bottom up approach. 
# If we know how to make an amount using given coins, then we can also know how to make amount + given coins.
# For Eg. If we know how make amount 10 with minimum number of coins using coins (1,2,5), then we can also know how to 
# make amount 11. It will be number of coins to make 10 plus 1 using coin of amount 1. Similarly for coin 5, to make amount 11,
# it will be number of coins to make amount 6 + 1 using coin 5. 
# The base case will be for amount 0. Amount 0 can be made using 0 coins. Building on that we can find the number of ways to 
# make any amount.


def coinChange(coins, amount):
    if amount == 0:
        return 0
    result = [float('inf')] * (amount + 1)      # float('inf'): initialising number of ways to make amount to infinity
    result[0] = 0                               # Ways to make amount 0 is 0.
    for smaller_amount in range(amount + 1):
        for coin in coins:
            if (coin <= smaller_amount) and ((result[smaller_amount - coin] + 1) < result[smaller_amount]):
                result[smaller_amount] = result[smaller_amount - coin] + 1

    if result[amount] != float('inf'):
        return result[amount]
    return -1
