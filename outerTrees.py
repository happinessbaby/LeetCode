import math


class Solution:


    def sort_trees(self, init_pt, trees):
        slopes= {}
        trees = sorted(sorted(trees[1:], key=lambda x:x[0]), key=lambda x:x[1], reverse=True)
        for i in trees:
            try:
                slope = (init_pt[1]-i[1])/(init_pt[0]-i[0])
                d = math.sqrt((init_pt[1]-i[1])**2 + (init_pt[0]-i[0])**2)
                slopes[slope, d] = i
            except ZeroDivisionError:
                d = i[1] - init_pt[1]
                slopes[-999999999, d] = i
        max_slope = abs(next(iter(slopes))[0])
        positives, negatives = [], []
        for key, value in slopes.items():
            if key[0] >= 0: positives.append([key, value])
            else: negatives.append([key, value])
        if len(positives) == 0:
            for n in negatives:
                if abs(n[0][0]) >= max_slope:
                    positives.append(n)
            for p in positives: negatives.remove(p)
        if len(negatives) == 0:
            for p in positives:
                if p[0][0] >= max_slope:
                    negatives.append(p)
            for n in negatives: positives.remove(n)
        sortedP = sorted(sorted(positives, key=lambda x:x[0][1]),key=lambda x:x[0][0])
        sortedN = sorted(sorted(negatives, key=lambda x:x[0][1],reverse=True),key=lambda x:x[0][0])
        sortedP.extend(sortedN)
        return [sortedP[i][1] for i in range(len(sortedP))]

    def outerTrees(self, trees):
        if len(trees) <= 1: return trees
        answer = []
        sorted_trees = sorted(sorted(trees, key = lambda x:x[0]), key=lambda x:x[1])
        init_pt = sorted_trees[0]
        T = self.sort_trees(init_pt, sorted_trees)
        T.append(init_pt)
        answer.append(init_pt)
        pt = T.pop(0)
        answer.append(pt)
        while len(T) > 1:
            cross_p = (T[0][0]-pt[0])*(T[1][1]-pt[1])-(T[0][1]-pt[1])*(T[1][0]-pt[0])
            if cross_p < 0: T.pop(0); T.insert(0, pt); answer.pop(); pt = answer[-1]
            else: pt = T.pop(0); answer.append(pt)
        return answer


s = Solution()
print(s.outerTrees([[0,2],[0,4],[0,5],[0,9],[2,1],[2,2],[2,3],[2,5],[3,1],[3,2],[3,6],[3,9],[4,2],[4,5],[5,8],[5,9],[6,3],[7,9],[8,1],[8,2],[8,5],[8,7],[9,0],[9,1],[9,6]]))
