from collections import Counter

class Solution:


    def maxNumberOfBalloons(self, text):
        ca, cb, cl, cn, co = 0, 0, 0, 0, 0
        for x in text:
            if x=='a':
                ca+=1
            if x =='b':
                cb+=1
            if x == 'l':
                cl+=1
            if x=='n':
                cn+=1
            if x=='o':
                co+=1
        return min([cb, ca, cl//2, co//2, cn])


    def maxNumberOfBalloons2(self, text: str) -> int:
        balloons = ['a', 'b', 'o', 'l', 'n']
        count = dict(Counter(list(filter(lambda x: x in balloons, text))).items())
        if len(count) < 5: return 0
        return min([count['a'], count['b'], count['l']//2, count['n'], count['o']//2])




s = Solution()
print(s.maxNumberOfBalloons2("balloonballoon"))
