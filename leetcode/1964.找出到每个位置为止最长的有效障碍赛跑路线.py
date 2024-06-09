#
# @lc app=leetcode.cn id=1964 lang=python3
#
# [1964] 找出到每个位置为止最长的有效障碍赛跑路线
#

# @lc code=start
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []
        g = []
        # def lower_bound(g: List[int],x: int)->int:
        #     l ,r= -1 , len(g)
        #     while l+1<r:
        #         mid = (l+r)//2
        #         if g[mid]>=x:
        #             r = mid
        #         else:
        #             l = mid
        #     return l+1
        for x in obstacles:
            j = bisect_left(g,x+1)
            if j==len(g):
                g.append(x)
            else:
                g[j] = x
            ans.append(j+1)
        return ans


# @lc code=end

