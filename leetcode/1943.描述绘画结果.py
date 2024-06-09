#
# @lc app=leetcode.cn id=1943 lang=python3
#
# [1943] 描述绘画结果
# 二刷（断点扫描）

# @lc code=start
class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        diff = defaultdict(int)
        for a, b, c in segments:
            diff[a] += c
            diff[b] -= c

        ind = sorted(list(diff.keys()))
        n = len(ind)
        ans = []
        cur = 0
        for i in range(n - 1):
            cur += diff[ind[i]]
            if cur:
                ans.append([ind[i], ind[i + 1], cur])
        return ans

        # N=100010
        # arr=[0]*N
        # visited=set()

        # for s,e,m in segments:
        #     arr[s] += m
        #     arr[e] -= m
        #     visited.add(s)
        #     visited.add(e)
        
        # res = []
        # pre=None
        # for i in range(1,N):
        #     arr[i] += arr[i-1]
        #     if i in visited:
        #         if pre and arr[pre]:
        #             res.append([pre,i,arr[pre]])
        #         pre = i
        # return res


# @lc code=end

