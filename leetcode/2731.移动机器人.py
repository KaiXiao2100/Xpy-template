#
# @lc app=leetcode.cn id=2731 lang=python3
#
# [2731] 移动机器人
# 

# @lc code=start
class Solution:
    def sumDistance(self, nums: List[int], s: str, d: int) -> int:
        for i, c in enumerate(s):
            nums[i] += d if c == 'R' else -d
        nums.sort()

        ans = s = 0
        for i, x in enumerate(nums):
            ans += i * x - s
            s += x
        return ans % (10 ** 9 + 7)

# @lc code=end

