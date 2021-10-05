class Solution:
    def sortArrayByParityII(self, nums):
        answer, even, odd = [], [], []
        for i in range(len(nums)):
            if i%2==0 and nums[i]%2==0:
                answer.append(nums[i])
            if i%2!=0 and nums[i]%2!=0:
                answer.append(nums[i])
            if i%2 ==0 and nums[i]%2!=0:
                odd.append(nums[i])
                if len(even)!=0:
                    answer.append(even.pop())
                else:
                    answer.append('e')
            if i%2!=0 and nums[i]%2==0:
                even.append(nums[i])
                if len(odd)!=0:
                    answer.append(odd.pop())
                else:
                    answer.append('o')
        while len(odd)>0:
            answer[answer.index('o')]= odd.pop()
        while len(even)>0:
            answer[answer.index('e')]= even.pop()
        return answer

s = Solution()
print(s.sortArrayByParityII([648,831,560,986,192,424,997,829,897,843]))
