#
# @lc app=leetcode.cn id=1463 lang=python3
#
# [1463] 摘樱桃 II
#

# @lc code=start
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])

        @cache
        def dfs(i: int,j: int,k: int)->int:
            if j<0 or k<0 or j>=n or k>=n:
                return -inf
            if i==m:
                return 0
            
            res = 0
            cnt = grid[i][j]
            if j!=k:
                cnt += grid[i][k]
            for a in [1,0,-1]:
                for b in [1,0,-1]:
                    nj = j+a
                    nk = k+b
                    res = max(res,dfs(i+1,nj,nk)+cnt)
            
            return res
        return dfs(0,0,n-1)

# @lc code=end

