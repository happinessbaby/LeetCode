class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        evens= []
        odds = []
        for i in range(len(nums)):
            if (nums[i] & 1)==1:
                odds.append(nums[i])
            else:
                evens.append(nums[i])
        return evens+odds
                
                
                