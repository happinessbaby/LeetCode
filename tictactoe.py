from collections import Counter

class Solution:


    def tictactoe(self, moves):
        total = len(moves)
        if total < 5:
            return 'Pending'
        hA = [moves[i][0] for i in range(0, len(moves), 2)]
        vA = [moves[i][1] for i in range(0, len(moves), 2)]
        hB = [moves[i][0] for i in range(1, len(moves), 2)]
        vB = [moves[i][1] for i in range(1, len(moves), 2)]
        dA = list(map(lambda x, y: abs(x-y), hA, vA))
        dB = list(map(lambda x, y: abs(x-y), hB, vB))
        if dA.count(0) == 3 or ([1, 1] in [moves[i] for i in range(0, len(moves), 2)] and dA.count(2)==2):
            return 'A'
        if dB.count(0)==3 or ([1, 1] in [moves[i] for i in range(1, len(moves), 2)] and dB.count(2)==2):
            return 'B'
        if total == 5:
            if len(set(hA))==1 or len(set(vA))==1:
                return 'A'
            else: return 'Pending'
        elif total == 6:
            if len(set(hB))==1 or len(set(vB))==1:
                return 'B'
            else: return 'Pending'
        elif total == 7:
            if 2 not in Counter(hA).values() or 2 not in Counter(vA).values():
                return 'A'
            else: return 'Pending'
        elif total == 8:
            if 2 not in Counter(hB).values() or 2 not in Counter(vB).values():
                return 'B'
            else: return 'Pending'
        else:
            if (len(set(hB))==3 and len(set(vB))==3):
                return 'Draw'
            else:
                return 'A'



s=Solution()
print(s.tictactoe([[0,2],[2,1],[0,1],[0,0],[2,2],[1,0],[2,0],[1,2]]))
