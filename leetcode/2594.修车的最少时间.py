#
# @lc app=leetcode.cn id=2594 lang=python3
#
# [2594] 修车的最少时间
#

# @lc code=start
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 0
        right = min(ranks) * cars * cars
        while left + 1 < right:  # 开区间
            mid = (left + right) // 2
            if sum(isqrt(mid // r) for r in ranks) >= cars:
                right = mid  # 满足要求
            else:
                left = mid
        return right  # 最小的满足要求的值

# @lc code=end

