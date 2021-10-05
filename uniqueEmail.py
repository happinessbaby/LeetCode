import re

class Solution:


    def numUniqueEmails2(self, emails):
        unique = set()
        for l in emails:
            i = 0
            while True:
                if l[i] == '@':
                    unique.add(l)
                    break
                elif l[i] == '.':
                    l = l.replace(l[i], '', 1)
                elif l[i] == '+':
                    l = l[:i]+l[l.index('@'):]
                    unique.add(l)
                    break
                else:
                    i+=1
        return len(unique)

s = Solution()
print(s.numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
