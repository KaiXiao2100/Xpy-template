#
# @lc app=leetcode.cn id=2439 lang=python3
#
# [2439] 最小化数组中的最大值
#

# @lc code=start
class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)

        def check(m: int)->bool:
            arr = nums.copy()
            for i in range(n-1,0,-1):
                if arr[i]>m:
                    diff = arr[i]-m
                    arr[i-1] += diff
            return arr[0]<=m


        l,r = 0,max(nums)
        while l<=r:
            m = (l+r)//2
            if check(m):
                r = m-1
            else:
                l = m+1
        return r+1
# @lc code=end

