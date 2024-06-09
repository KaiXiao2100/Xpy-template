#
# @lc app=leetcode.cn id=2411 lang=python3
#
# [2411] 按位或最大的最小子数组长度
#

# @lc code=start
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i, x in enumerate(nums):
            ans[i] = 1
            for j in range(i - 1, -1, -1):
                if (nums[j] | x) == nums[j]:
                    break
                nums[j] |= x
                ans[j] = i - j + 1
        return ans

# @lc code=end

