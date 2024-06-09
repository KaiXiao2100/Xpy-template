#
# @lc app=leetcode.cn id=1416 lang=python3
#
# [1416] 恢复数组
#

# @lc code=start
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        mod = 10**9+7
        n = len(s)
        @cache
        def dfs(i: int)->int:
            if i==n:
                return 1
            if s[i] == '0':
                return 0
            res = 0
            for j in range(i,n):
                if int(s[i:j+1])<=k:
                    res = (res+dfs(j+1))%mod
                else:
                    break
            return res
        
        return dfs(0)

# @lc code=end

