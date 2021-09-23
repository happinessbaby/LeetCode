import math

class Solution:


    def breakPalindrome(self, palindrome):
        n = len(palindrome)
        remove = n-2
        if n==1:
            return ''
        for i in range(n-1):
            if palindrome[i] !='a':
                check = palindrome[:i]+'a'+palindrome[i+1:]
                if check[:math.floor(n/2)]==check[math.ceil(n/2):][::-1]:
                    continue
                else:
                    remove = i
                    break
        if remove == n-2 and palindrome[-1]=='a':
            return palindrome[:-1]+'b'
        return palindrome[:i]+'a'+palindrome[i+1:]




s = Solution()
print(s.breakPalindrome('aaaaa'))
