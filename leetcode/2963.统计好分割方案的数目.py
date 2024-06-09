#
# @lc app=leetcode.cn id=2963 lang=python3
#
# [2963] 统计好分割方案的数目
# 二刷

# @lc code=start
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        ps = {}
        for i,x in enumerate(nums):
            if x in ps:
                ps[x][1] = i
            else:
                ps[x] = [i,i]
        
        a = sorted(ps.values(),key=lambda p:p[0])
        m = 0
        max_r = a[0][1]
        for left,right in a[1:]:
            if left>max_r:
                m += 1
            max_r = max(max_r,right)
        return pow(2,m,10**9+7)

# @lc code=end

