#
# @lc app=leetcode.cn id=3133 lang=python3
#
# [3133] 数组最后一个元素的最小值
#

# @lc code=start
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        i = j = 0
        while n>>j:
            if (x>>i & 1)==0:
                x |= (n>>j & 1) <<i
                j+=1
            i+=1
        return x
# @lc code=end

