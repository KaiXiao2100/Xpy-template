#
# @lc app=leetcode.cn id=1482 lang=python3
#
# [1482] 制作 m 束花所需的最少天数
#

# @lc code=start
class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m*k:
            return -1

        def check(mid: int)->bool:
            cnt = 0
            x = 0
            for a in bloomDay:
                if a<=mid:
                    x += 1
                    if x==k:
                        cnt += 1
                        if cnt == m:
                            return True
                        x = 0
                else:
                    x = 0
            return cnt >= m

        l,r = 1,max(bloomDay)
        while l<=r:
            mid = (l+r)//2
            if check(mid):
                r = mid-1
            else:
                l = mid+1

        return r+1
# @lc code=end

