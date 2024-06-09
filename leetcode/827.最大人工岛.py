#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] 最大人工岛
#

# @lc code=start
class UnionFind:
    def __init__(self, n: int):
        self.parents = [i for i in range(n)]
        self.sizes = [1] * n

    def find(self, x: int) -> int:
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x: int, y: int):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.parents[rx] = ry
            self.sizes[ry] += self.sizes[rx]

    def getSize(self, x: int) -> int:
        return self.sizes[x]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        fa = UnionFind(n*n)
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0: continue
                for r, c in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= r < n and 0 <= c < n and grid[r][c] == 1:
                        fa.union(r * n + c, i * n + j)
        ans = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0:
                    vis = set()
                    cur = 0
                    for r, c in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                        if 0 <= r < n and 0 <= c < n and grid[r][c] == 1:
                            node = fa.find(r * n + c)
                            if node in vis: continue
                            cur += fa.getSize(node)
                            vis.add(node)                            
                    ans = max(ans, cur + 1)
                else:
                    ans = max(ans, fa.getSize(fa.find(i*n + j)))
        return ans
# @lc code=end

