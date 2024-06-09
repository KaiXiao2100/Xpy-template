#
# @lc app=leetcode.cn id=1130 lang=python3
#
# [1130] 叶值的最小代价生成树
# 二刷

# @lc code=start
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # @cache
        # def dfs(i: int,j: int)->int:
        #     if i==j:
        #         return 0
        #     return min(dfs(i,k)+dfs(k+1,j)+g[i][k] * g[k+1][j] for k in range(i,j))
        
        n = len(arr)
        g = [[0]*n for _ in range(n)]
        f = [[0] * n for _ in range(n)]
        for i in range(n-1,-1,-1):
            g[i][i] = arr[i]
            for j in range(i+1,n):
                g[i][j] = max(g[i][j-1],arr[j])
                f[i][j] = min(f[i][k] + f[k+1][j] + g[i][k]*g[k+1][j] for k in range(i,j))
        return f[0][n-1]
        # return dfs(0,n-1)

# @lc code=end

