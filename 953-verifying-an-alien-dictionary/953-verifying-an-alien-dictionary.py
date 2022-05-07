class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        idx = 1
        dictionary = {}
        for l in order:
            dictionary[l]=idx
            idx+=1
        for i in range(len(words)-1):
            min_length = min(len(words[i]), len(words[i+1]))
            for j in range(min_length):
                if dictionary[words[i][j]]<dictionary[words[i+1][j]]:
                    break
                if dictionary[words[i][j]]>dictionary[words[i+1][j]]:
                    return False
                elif len(words[i])>len(words[i+1]):
                    if words[i][:min_length]==words[i+1]:
                        return False
        return True