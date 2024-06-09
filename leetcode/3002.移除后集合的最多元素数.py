#
# @lc app=leetcode.cn id=3002 lang=python3
#
# [3002] 移除后集合的最多元素数
#二刷

# @lc code=start
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        common = len(set1 & set2)
        
        n1 = len(set1)
        n2 = len(set2)
        ans = n1+n2-common

        m = len(nums1)//2
        if n1>m:
            mn = min(n1-m,common)
            ans -= n1 - mn - m
            common -= mn
        
        if n2>m:
            n2 -= min(n2-m,common)
            ans -= n2-m
        return ans


# @lc code=end

