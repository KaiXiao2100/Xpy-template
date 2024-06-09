#
# @lc app=leetcode.cn id=1537 lang=python3
#
# [1537] 最大得分
# 二刷

# @lc code=start
class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1,sum2,i,j,INF = 0,0,0,0,10**9+7
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<nums2[j]:
                sum1 += nums1[i]
                i +=1
            elif nums2[j]<nums1[i]:
                sum2 += nums2[j]
                j+=1
            else:
                sum1 = sum2 = (max(sum1,sum2) + nums1[i])%INF
                i += 1
                j += 1

        sum1, sum2 = sum1 + sum(nums1[i:]), sum2 + sum(nums2[j:])
        return max(sum1,sum2)%INF


# @lc code=end

