#method1: go from backward, see if the previous num can lead to the last number
#if not, go to the next previous, if yes, change the last number to prev number
#if at any number, no previous numbers can get to it, return false

class Solution:


    def canJump(self, nums):
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False
        i, j = 1, 1
        while True:
            if j+i > len(nums):
                return jump
            prev = nums[-(j+i)]
            if prev  < j:
                j+=1
                jump = False
            else:
                i += j
                j = 1
                jump = True


s = Solution()
print(s.canJump([1]))
