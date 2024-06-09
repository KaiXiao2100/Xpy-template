#
# @lc app=leetcode.cn id=1696 lang=python3
#
# [1696] 跳跃游戏 VI
# 

# @lc code=start
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = [0] * n
        q = deque([0])
        for i in range(n):
            if i - q[0] > k:
                q.popleft()
            f[i] = nums[i] + f[q[0]]
            while q and f[q[-1]] <= f[i]:
                q.pop()
            q.append(i)
        return f[-1]

            
# @lc code=end

