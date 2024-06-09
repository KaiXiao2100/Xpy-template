#
# @lc app=leetcode.cn id=2350 lang=python3
#
# [2350] 不可能得到的最短骰子序列
# 二刷

# @lc code=start
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        mark = [0]*(k+1)
        ans,left = 1,k
        for v in rolls:
            if mark[v] < ans:
                mark[v] = ans
                left -= 1
                if left == 0:
                    left = k
                    ans += 1
        return ans


# @lc code=end

