class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        answer = [[0]*n for i in range(n)]
        m=1
        i, j, k=0, 0, 0
        while True:
            for j in range(k, n-k):
                answer[i][j]=m
                if m==n**2:
                    return answer
                m+=1
            for i in range(k+1, n-k):
                answer[i][j]=m
                if m==n**2:
                    return answer
                m+=1
            for j in range(n-k-2, -1+k, -1):
                answer[i][j]=m
                if m==n**2:
                    return answer
                m+=1
            for i in range(n-k-2, k, -1):
                answer[i][j]=m
                if m==n**2:
                    return answer
                m+=1
            k+=1