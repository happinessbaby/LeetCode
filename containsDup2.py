

class Solution:

    def containsNearbyDuplicate(self, nums, k):
        idx = {}
        for i in range(len(nums)):
            if nums[i] not in idx:
                idx[nums[i]]=i
            else:
                if i-idx[nums[i]] <= k:
                    return True
                else:
                    idx[nums[i]]=i
        return False

s = Solution()
print(s.containsNearbyDuplicate([1,2,3,1], 3))
