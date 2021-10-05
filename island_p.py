class Solution:
    def islandPerimeter(self, grid):
        perimeter = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    adj = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
                    p = 4
                    for a in adj:
                        if a[0]<0 or a[1]<0 or a[0]>n-1 or a[1]>m-1:
                            continue
                        else:
                            if grid[a[0]][a[1]]==1:
                                p-=1
                    perimeter+=p
        return perimeter

s = Solution()
print(s.islandPerimeter([[1]]))
