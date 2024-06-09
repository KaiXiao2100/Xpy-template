#
# @lc app=leetcode.cn id=765 lang=python3
#
# [765] 情侣牵手
# 二刷  bfs/并查集

# @lc code=start
class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        graph = [[] for _ in range(len(row)//2)]
        for i in range(0,len(row),2):
            graph[row[i]//2].append(row[i+1]//2)
            graph[row[i+1]//2].append(row[i]//2)
        visited = [False] * (len(row)//2)
        ans = 0
        for i in range(len(row)//2):
            if visited[i]:
                continue
            q = []
            q.append(i)
            visited[i] = True
            thisCnt = 0
            while q:
                thisCnt += 1
                thisPeople = q.pop()
                for nextPeople in graph[thisPeople]:
                    if not visited[nextPeople]:
                        visited[nextPeople] = True
                        q.append(nextPeople)
            ans += thisCnt - 1
        return ans
    
    # def getf(self, f, x):
    #     if f[x] == x:
    #         return x
    #     newf = self.getf(f, f[x])
    #     f[x] = newf
    #     return newf

    # def add(self, f, x, y):
    #     fx = self.getf(f, x)
    #     fy = self.getf(f, y)
    #     f[fx] = fy

    # def minSwapsCouples(self, row: List[int]) -> int:
    #     n = len(row)
    #     tot = n // 2
    #     f = [i for i in range(tot)]

    #     for i in range(0, n, 2):
    #         l = row[i] // 2
    #         r = row[i + 1] // 2
    #         self.add(f, l, r)

    #     m = {}
    #     for i in range(tot):
    #         fx = self.getf(f, i)
    #         if fx in m:
    #             m[fx] += 1
    #         else:
    #             m[fx] = 1

    #     ret = 0
    #     for f, sz in m.items():
    #         ret += sz - 1

    #     return ret



# @lc code=end

