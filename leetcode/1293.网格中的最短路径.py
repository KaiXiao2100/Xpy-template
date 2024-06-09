#
# @lc app=leetcode.cn id=1293 lang=python3
#
# [1293] 网格中的最短路径
# 

# @lc code=start
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        dist=[[inf]*n for _ in range(m)]
        stack = [[0, 0, 0, 0]]
        dirs=[[-1,0],[0,1],[1,0],[0,-1]]

        while stack:
            dis,cost,i,j = heappop(stack)
            if i==m-1 and j==n-1:
                return dis
            for d in dirs:
                x,y = i+d[0],j+d[1]
                if 0<=x<m and 0<=y<n:
                    if dist[x][y]>cost+1 and cost+grid[x][y]<=k:
                        dist[x][y]=cost+1
                        heappush(stack, [dis + 1, cost + grid[x][y], x, y])

        return -1

# @lc code=end

