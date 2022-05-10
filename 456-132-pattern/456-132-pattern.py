class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        second = -float("inf")
        stack = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i]<second:
                return True
            while stack and stack[-1]<nums[i]:
                second = stack.pop()
            stack.append(nums[i])
        return False
                
        
            