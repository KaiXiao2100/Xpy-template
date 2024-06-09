#
# @lc app=leetcode.cn id=1760 lang=python3
#
# [1760] 袋子里最少数目的球
#

# @lc code=start
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        
        def check(m: int)->bool:
            cnt = 0
            for a in nums:
                cnt += (a+m-1)//m -1
            return cnt <= maxOperations

        l,r = 1,max(nums)
        while l<=r:
            m = (l+r)//2
            if check(m):
                r = m-1
            else:
                l = m+1

        return r+1

# @lc code=end

