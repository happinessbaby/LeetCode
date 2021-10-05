
#Given an integer array nums and two integers k and t,
# return true if there are two distinct indices i and j in the array such that
# abs(nums[i] - nums[j]) <= t and abs(i - j) <= k.



class Solution:


    def duplicate(self, nums, k, t):
        if k == 0 or len(nums)<=1:
            return False
        idx = []
        for i in range(len(nums)):
            idx.append([nums[i], i])
        idx = iter(sorted(idx))
        prev = next(iter(idx))
        curr = next(iter(idx))
        x = 0 #takes cycle into subcycle mode
        while True:
            if abs(prev[0]-curr[0]) <= t:
                if abs(prev[1]-curr[1])<=k:
                    return True
                else:
                    try:
                        x+=1
                        if x==1:
                            copy_p = curr
                            curr = next(iter(idx))
                            copy_c = curr
                        if x>1:
                            curr = next(iter(idx))
                    except StopIteration:
                        if x > 1:
                             prev = copy_p
                             curr = copy_c
                             x = 0
                        else:
                            break
            elif abs(prev[0]-curr[0]) > t:
                try:
                    if x==0:
                        prev = curr
                        curr = next(iter(idx))
                    if x>=1:
                        prev = copy_p
                        curr = copy_c
                        x = 0
                except StopIteration:
                    break
        return False



s = Solution()
print(s.duplicate([3,6,0,4], 2, 2))
