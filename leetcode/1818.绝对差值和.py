#
# @lc app=leetcode.cn id=1818 lang=python3
#
# [1818] 绝对差值和
#

# @lc code=start
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        arr = sorted(nums1)
        n = len(nums1)
        total = 0
        for i in range(n):
            diff = abs(nums1[i]-nums2[i])
            total += diff
        if not total:
            return 0
        
        ans = inf
        for i in range(n):
            p1 = bisect_left(arr,nums2[i])
            if p1 > 0:
                ans = min(ans, total - abs(nums1[i] - nums2[i]) + abs(arr[p1-1] - nums2[i]))

            if p1 < n:
                ans = min(ans, total - abs(nums1[i] - nums2[i]) + abs(arr[p1] - nums2[i]))            
        return ans%(10**9+7)


# @lc code=end

