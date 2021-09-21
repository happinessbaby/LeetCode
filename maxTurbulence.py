class Solution:


    def maxTurbulenceSize(self, arr):
        if len(set(arr)) == 1: return 1
        turbu, max = 0, 0
        for i in range(2, len(arr))[::-1]:
            if (arr[i-2]-arr[i-1]<0 and arr[i-1]-arr[i]>0) or (arr[i-2]-arr[i-1]>0 and arr[i-1]-arr[i]< 0):
                turbu+=1
                if turbu > max:
                    max = turbu
            else: turbu=0
        return max+2



s = Solution()
print(s.maxTurbulenceSize([2,0,2,4,2,5,0,1,2,3]))
print(s.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
print(s.maxTurbulenceSize([0, 0]))
