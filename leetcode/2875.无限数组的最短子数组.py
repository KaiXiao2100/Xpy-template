#
# @lc app=leetcode.cn id=2875 lang=python3
#
# [2875] 无限数组的最短子数组
#
#理解题意：并非从数组中任选，而是只能按顺序循环选择，并且在一个循环内无法重复选择一个数字

# @lc code=start
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        n = len(nums)
        ans = inf
        left = s = 0
        for right in range(n*2):
            s += nums[right%n]
            while s > target%total:
                s -= nums[left%n]
                left += 1
            if s==target%total:
                ans = min(ans,right-left+1)
        return ans + target//total * n if ans < inf else -1
# @lc code=end

