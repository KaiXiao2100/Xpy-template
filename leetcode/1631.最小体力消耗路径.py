#
# @lc app=leetcode.cn id=1631 lang=python3
#
# [1631] 最小体力消耗路径
#

# @lc code=start
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        # 错误方法
        # m,n = len(heights),len(heights[0])
        # dirs = [[0,1],[0,-1],[-1,0],[1,0]]
        # visited = [[False]*n for _ in range(m)]

        # @cache
        # def dfs(i: int,j: int)->int:
        #     if i==m-1 and j==n-1:
        #         return 0
        #     t = 0
        #     res = inf
        #     for idx in range(4):
        #         nx = i+dirs[idx][0]
        #         ny = j+dirs[idx][1]
        #         if nx>=m or ny >= n or nx < 0 or ny < 0 or visited[nx][ny]:
        #             continue
        #         visited[nx][ny] = True
        #         diff = abs(heights[i][j] - heights[nx][ny])
        #         t = max(diff,dfs(nx,ny))
        #         res = min(res,t)
        #         visited[nx][ny] = False
        #     return res
        # visited[0][0] = True
        # return dfs(0,0)
            

# @lc code=end

