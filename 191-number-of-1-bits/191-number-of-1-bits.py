class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        # while n>0:
        #     count+=n&1
        #     n=n>>1
        # while n>0:
        #     count+=n%2
        #     n=n>>1
        while n:
            n = n&(n-1)
            count+=1
        return count
                