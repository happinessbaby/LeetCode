class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # stack = []
        # start_count=0
        # end_idx = len(nums)-1
        # start_idx = 0
        # prev = 0
        # for i in range(len(nums)-1, -1, -1):
        #     while stack and nums[i]<stack[-1]:
        #         prev = stack.pop()
        #     stack.append(nums[i])
        #     if len(set(stack))>1 and start_count==0:
        #         start_idx = i
        #         end_idx = i+len(stack)
        #         start_count+=1
        #     elif len(set(stack))>1 and start_count>0:
        #         start_idx = i
        # return end_idx-start_idx
        local_min = float("inf")
        local_max = -float("inf")
        for i in range(len(nums)-1):  
            if nums[i+1] < nums[i]:
                local_min = min(local_min, nums[i+1])
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1]>nums[i]:
                local_max = max(local_max, nums[i-1])
        for j in range(len(nums)):
            if nums[j]>local_min:
                break
        for k in range(len(nums)-1, -1, -1):
            if nums[k]<local_max:
                break
        return k-j+1 if k-j>0 else 0
            
                
            
            
            
            