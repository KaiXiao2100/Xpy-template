#
# @lc app=leetcode.cn id=2872 lang=python3
#
# [2872] 可以被 K 整除连通块的最大数目
# 二刷

# @lc code=start
class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        ans = 0
        def dfs(x: int,fa: int)->int:
            s = values[x]
            for y in g[x]:
                if y!=fa:
                    s += dfs(y,x)
            nonlocal ans
            ans += s%k==0
            return s
        dfs(0,-1)
        return ans


# @lc code=end

