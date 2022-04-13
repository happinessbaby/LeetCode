class Solution:
    def calPoints(self, ops: List[str]) -> int:
        scores = []
        for x in ops:
            try:
                scores.append(int(x))
            except ValueError:
                if x=="C":
                    scores.pop()
                elif x=="D":
                    scores.append(scores[-1]*2)
                else:
                    scores.append(scores[-1]+scores[-2])
        return sum(scores)