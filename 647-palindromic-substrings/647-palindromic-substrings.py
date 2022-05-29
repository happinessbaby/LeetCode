class Solution:
    def countSubstrings(self, s: str) -> int:
        def countPalindrome(l, r):
            count=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
                count+=1
            return count
        total_count = 0
        for i in range(len(s)):
            total_count+=countPalindrome(i, i)
            total_count+=countPalindrome(i, i+1)
        return total_count
            