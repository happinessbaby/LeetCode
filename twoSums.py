


class Solution:
    def twoSum(self, nums, target):
        if len(nums)==2:
            return [0, 1]
        N = sorted(nums)
        mid = int(len(N)/2)
        k = 0
        while True:
            if mid > len(N)-2:
                i=2
                while mid-i >= 0:
                    if N[mid]+N[mid-i]<target:
                        break
                    if N[mid]+N[mid-i] == target:
                        return self.find_index(nums, N[mid], N[mid-i])
                    i+=1
            elif mid == 0:
                i = 2
                while mid+i < len(N):
                    if N[mid]+N[mid+i]>target:
                        break
                    if N[mid]+N[mid+i]==target:
                        return self.find_index(nums, N[mid], N[mid+i])
                    i+=1
            elif 0 < mid < len(N)-1:
                a= N[mid]+N[mid+1]
                b = N[mid]+N[mid-1]
                if a == target:
                    return self.find_index(nums, N[mid], N[mid+1])
                if b == target:
                    return self.find_index(nums, N[mid], N[mid-1])
                if a < target and b < target:
                    i=2
                    while True:
                        try:
                            a=N[mid] + N[mid+i]
                            if a == target:
                                return self.find_index(nums, N[mid], N[mid+i])
                            if a > target:
                                break
                            i+=1
                        except IndexError:
                            break
                elif a > target and b > target:
                    i=2
                    while True:
                        try:
                            a=N[mid] + N[mid-i]
                            if a == target:
                                return self.find_index(nums, N[mid], N[mid-i])
                            if a < target:
                                break
                            i+=1
                        except IndexError:
                            break
            k+=1
            if k%2!=0: mid = mid+k
            if k%2==0: mid = mid-k

    def find_index(self, nums, i, j):
        idx_i = [x[0] for x in enumerate(nums) if x[1] == i]
        idx_j = [x[0] for x in enumerate(nums) if x[1] == j]
        if len(idx_i)==1:
            return [idx_i[0], idx_j[0]]
        else:
            return [idx_i[0], idx_i[1]]



s = Solution()
print(s.twoSum([3, 4, 5, 6, 3, 7, 8, -10],-2))
