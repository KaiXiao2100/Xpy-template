#
# @lc app=leetcode.cn id=2654 lang=python3
#
# [2654] 使数组所有元素变成 1 的最少操作次数
# 二刷 gcd性质+原地去重

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int]) -> int:

        if gcd(*nums) > 1:
            return -1
        n = len(nums)
        cnt1 = sum(x == 1 for x in nums)
        if cnt1:
            return n - cnt1

        min_size = n
        for i in range(n):
            g = 0
            for j in range(i, n):
                g = gcd(g, nums[j])
                if g == 1:
                    # 这里本来是 j-i+1，把 +1 提出来合并到 return 中
                    min_size = min(min_size, j - i)
                    break
        return min_size + n - 1

# @lc code=end

