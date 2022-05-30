class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mask = [0]*len(words)
        max_len = 0
        for i in range(len(words)):
            for char in words[i]:
                mask[i] |= 1<<(ord(char)-ord('a'))
            for j in range(i):
                if mask[i]&mask[j]==0:
                    max_len = max(max_len, len(words[i])*len(words[j]))
        return max_len