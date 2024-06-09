#
# @lc app=leetcode.cn id=2925 lang=python3
#
# [2925] 在树上执行操作以后得到的最大分数
#

# @lc code=start
class Solution:
    def maximumScoreAfterOperations(self, edges: List[List[int]], values: List[int]) -> int:
        g = [[] for _ in values]
        g[0].append(-1)  # 避免误把根节点当作叶子
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(x: int, fa: int) -> int:
            if len(g[x]) == 1:  # x 是叶子
                return values[x]
            loss = 0  # 第二种情况
            for y in g[x]:
                if y != fa:
                    loss += dfs(y, x)  # 计算以 y 为根的子树是健康时，失去的最小分数
            return min(values[x], loss)  
        return sum(values) - dfs(0,-1)

# @lc code=end

