class Solution:

    def intersect(self, nums1, nums2):
        if len(nums1) > len(nums2):
            bigger, smaller = nums1, nums2
        else: bigger, smaller = nums2, nums1
        return [bigger.pop(bigger.index(a)) for a in smaller if a in bigger]


s = Solution()
print(s.intersect([9, 4, 9, 8, 4], [4, 9, 4, 5]))
print(s.intersect([1, 2, 3], [3, 4, 5]))
