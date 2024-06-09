#
# @lc app=leetcode.cn id=1642 lang=python3
#
# [1642] 可以到达的最远建筑
# 

# @lc code=start
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        # 由于我们需要维护最大的 l 个值，因此使用小根堆
        q = list()
        # 需要使用砖块的 delta h 的和
        sumH = 0
        for i in range(1, n):
            deltaH = heights[i] - heights[i - 1]
            if deltaH > 0:
                heapq.heappush(q, deltaH)
                # 如果优先队列已满，需要拿出一个其中的最小值，改为使用砖块
                if len(q) > ladders:
                    sumH += heapq.heappop(q)
                if sumH > bricks:
                    return i - 1
        return n - 1

# @lc code=end

