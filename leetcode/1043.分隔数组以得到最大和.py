#
# @lc app=leetcode.cn id=1043 lang=python3
#
# [1043] 分隔数组以得到最大和
#

# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)

        @cache
        def dfs(i: int)->int:
            if i == n:
                return 0
            res = 0
            for j in range(i,min(i+k,n)):
                res = max(res,dfs(j+1) + max(arr[i:j+1])*(j-i+1))
            return res
        return dfs(0)


# @lc code=end

