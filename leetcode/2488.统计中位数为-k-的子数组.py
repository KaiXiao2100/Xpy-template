#
# @lc app=leetcode.cn id=2488 lang=python3
#
# [2488] 统计中位数为 K 的子数组
# 二刷 (新题)

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = nums.index(k)
        cnt,x = Counter({0:1}),0
        for i in range(pos-1,-1,-1):
            x += 1 if nums[i] < k else -1
            cnt[x] += 1
        
        ans,x = cnt[0]+cnt[-1],0
        for i in range(pos+1,len(nums)):
            x += 1 if nums[i]>k else -1
            ans += cnt[x] + cnt[x-1]
        return ans



# @lc code=end

