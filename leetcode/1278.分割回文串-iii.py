#
# @lc app=leetcode.cn id=1278 lang=python3
#
# [1278] 分割回文串 III
#

# @lc code=start
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        cost = [[0] * n for _ in range(n)]
        for span in range(2, n + 1):
            for i in range(n - span + 1):
                j = i + span - 1
                cost[i][j] = cost[i + 1][j - 1] + (0 if s[i] == s[j] else 1)

        f = [[10**9] * (k + 1) for _ in range(n + 1)]
        f[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(k, i) + 1):
                if j == 1:
                    f[i][j] = cost[0][i - 1]
                else:
                    for i0 in range(j - 1, i):
                        f[i][j] = min(f[i][j], f[i0][j - 1] + cost[i0][i - 1])
        
        return f[n][k]



        # n = len(s)
        # def cost(l, r):
        #     ret, i, j = 0, l, r
        #     while i < j:
        #         ret += (0 if s[i] == s[j] else 1)
        #         i += 1
        #         j -= 1
        #     return ret

        # @cache
        # def dfs(i: int,c: int)->int:
        #     if i==n:
        #         return 0 if c==0 else inf
        #     if c==0:
        #         return inf
        #     res = inf
        #     for j in range(i,n-c+1):
        #         res = min(res,dfs(j+1,c-1)+cost(i,j))
        #     return res
        # return dfs(0,k)

# @lc code=end

