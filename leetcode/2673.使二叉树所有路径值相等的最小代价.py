#
# @lc app=leetcode.cn id=2673 lang=python3
#
# [2673] 使二叉树所有路径值相等的最小代价
#

# @lc code=start
class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        for i in range(n // 2, 0, -1):  # 从最后一个非叶节点开始算
            ans += abs(cost[i * 2 - 1] - cost[i * 2])  # 两个子节点变成一样的
            cost[i - 1] += max(cost[i * 2 - 1], cost[i * 2])  # 累加路径和
        return ans

        
# @lc code=end

