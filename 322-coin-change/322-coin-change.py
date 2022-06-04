class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [amount+1]*(amount+1)
        memo[0]=0
        for x in range(1, amount+1):
            for coin in coins:
                if x-coin>=0:
                    memo[x] = min(memo[x], 1+memo[x-coin])
        return memo[amount] if memo[amount]!=amount+1 else -1
                


                