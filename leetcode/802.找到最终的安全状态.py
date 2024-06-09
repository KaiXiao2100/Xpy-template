#
# @lc app=leetcode.cn id=802 lang=python3
#
# [802] 找到最终的安全状态
# 二刷

# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n =len(graph)
        out = [0]*n
        edges = defaultdict(list)
        for i,nodes in enumerate(graph):
            for node in nodes:
                edges[node].append(i)
                out[i] += 1
        q = deque()
        for i in range(n):
            if not out[i]:
                q.append(i)
        while q:
            node = q.popleft()
            for front in edges[node]:
                out[front] -= 1
                if not out[front]:
                    q.append(front)
        return [i for i in range(n) if not out[i]]
# @lc code=end

