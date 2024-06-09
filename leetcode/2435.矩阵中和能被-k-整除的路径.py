#
# @lc app=leetcode.cn id=2435 lang=python3
#
# [2435] 矩阵中和能被 K 整除的路径
#

# @lc code=start
class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid),len(grid[0])
        dirs = [[0,1],[1,0]]
        mod = 10**9+7
        @cache
        def dfs(i: int,j: int,x: int)->int:
            if i==m-1 and j==n-1:
                return 1 if x==0 else 0
            
            res = 0
            for a in range(2):
                nx = i+dirs[a][0]
                ny = j+dirs[a][1]
                if nx <0 or ny<0 or nx>=m or ny>=n:
                    continue
                res = (res+dfs(nx,ny,(x+grid[nx][ny])%k))%mod
            return res
        return dfs(0,0,grid[0][0]%k)

# @lc code=end

