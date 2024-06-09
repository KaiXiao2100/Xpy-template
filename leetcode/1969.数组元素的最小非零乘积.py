#
# @lc app=leetcode.cn id=1969 lang=python3
#
# [1969] 数组元素的最小非零乘积
# 二刷

# @lc code=start
class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10**9+7
        k = (1<<p)-1
        return k*pow(k-1,k>>1,mod)%mod
        

# @lc code=end

