import sys

class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """
    def coinChange(self, coins, amount):
        # write your code here

        # Initialize dp array -> combination of coins
        comb = [sys.maxint] * (amount + 1)
        comb[0] = 0

        # iterate amout of money
        for i in xrange(amount + 1):

            # iterate coins
            for coin in coins:

                # if current amout is greater than coin value and we can reach
                # the diff of amout and current coin
                if i >= coin and comb[i - coin] != sys.maxint:

                    # update
                    comb[i] = min(comb[i - coin] + 1, comb[i])

        # return if we can give a feasible combination
        return comb[amount] if comb[amount] != sys.maxint else -1
