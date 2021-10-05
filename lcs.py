class Solution:

    def __init__(self):
        self.memo = {}


    def lcs(self, text1, text2) -> int:
        if (text1, text2) in self.memo:
            return self.memo[(text1, text2)]
        if text1 == '' or text2 == '':
            return 0
        if text1[-1]==text2[-1]:
            self.memo[(text1, text2)]= 1 + self.lcs(text1[:-1], text2[:-1])
            return self.memo[(text1, text2)]
        else:
            self.memo[(text1, text2)]= max(self.lcs(text1[:-1], text2), self.lcs(text1, text2[:-1]))
            return self.memo[(text1, text2)]


s=Solution()
#print(s.lcs('aaba', 'abcbcba'))
print(s.lcs("pmjghexybyrgzczy", "hafcdqbgncrcbihkd"))
#print(s.lcs("oxcpqrsvwf", "shmtulqrypy"))
