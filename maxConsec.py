class Solution:

    def maxConsec(self, nums):
        C = []
        count = 0
        nums.append(0)
        for i in nums:
            if i==1:
                count += 1
            if i==0:
                C.append(count)
                count = 0
        return max(C)


s = Solution()
print(s.maxConsec([0, 1, 0, 1, 1, 1]))
