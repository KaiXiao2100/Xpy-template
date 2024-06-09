#
# @lc app=leetcode.cn id=940 lang=python3
#
# [940] 不同的子序列 II
# 二刷

# @lc code=start
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9+7
        f = [[0]*26 for _ in range(len(s)+1)]
        for i,c in enumerate(s,1):
            c = ord(c)-ord('a')
            f[i] = f[i-1].copy()
            f[i][c] = (1+sum(f[i-1]))%mod
        return sum(f[-1])%mod
# @lc code=end

