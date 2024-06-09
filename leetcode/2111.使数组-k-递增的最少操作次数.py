#
# @lc app=leetcode.cn id=2111 lang=python3
#
# [2111] 使数组 K 递增的最少操作次数
# 

# @lc code=start
class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
        ans = 0
        for i in range(k):
            q = []
            idx = i
            mx = 0
            while idx<n:
                a = arr[idx]
                j = bisect_left(q,a+1)
                if j==len(q):
                    q.append(a)
                else:
                    q[j] = a
                mx = max(mx,len(q))
                idx += k
            ans += mx
        return n-ans



# @lc code=end

