class Solution:
    # notes: to reitterate the problem is asking to find the smallest number of coins to make up a given amount
    #        with the ability to choose any number of each coin

    # approch:
    # we run a dfs on the given coins
    # if the a coin is greater than the target amount, we return -1
    #
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in dp:
                return dp[amount]

            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            dp[amount] = res
            return res

        minCoins = dfs(amount)
        return -1 if minCoins == float("inf") else minCoins
