class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = [[x.count("0"), x.count("1")] for x in strs]
        dp = [[0]*(n+1) for _ in range(m+1)]
        for zero, one in memo:
            for i in range(m, zero-1, -1):
                for j in range(n, one-1, -1):
                    dp[i][j]=max(dp[i][j], 1+dp[i-zero][j-one])
        return dp[-1][-1]
        