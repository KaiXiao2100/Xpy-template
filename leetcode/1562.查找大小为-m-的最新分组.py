#
# @lc app=leetcode.cn id=1562 lang=python3
#
# [1562] 查找大小为 M 的最新分组
# 

# @lc code=start
class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        fa = list(range(n+1))
        ans = -1
        res = 0 # 维护出现m长度的次数
        l = [0] * (n+1) # 维护每个节点的长度


        def find(x):
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]

        for i,x in enumerate(arr):
            x = x-1
            root = find(x+1)
            fa[x] = root

            if l[x] == m:
                res -= 1
            if l[root]==m:
                res -= 1
            
            l[root] += l[x]+1
            if l[root] == m:
                res += 1
            if res>0:
                ans = i
        return ans + 1 if ans > -1 else -1


# @lc code=end

