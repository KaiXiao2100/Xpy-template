#
# @lc app=leetcode.cn id=1793 lang=python3
#
# [1793] 好子数组的最大分数
#

# @lc code=start
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = min_h = nums[k]
        i = j = k
        for _ in range(n - 1):
            if j == n - 1 or i and nums[i - 1] > nums[j + 1]:
                i -= 1
                min_h = min(min_h, nums[i])
            else:
                j += 1
                min_h = min(min_h, nums[j])
            ans = max(ans, min_h * (j - i + 1))
        return ans

        # n = len(nums)
        # left = [-1]*n
        # st = []
        # for i,x in enumerate(nums):
        #     while st and x <= nums[st[-1]]:
        #         st.pop()
        #     if st:
        #         left[i] = st[-1]
        #     st.append(i)
        
        # right = [n]*n
        # st.clear()
        # for i in range(n-1,-1,-1):
        #     x = nums[i]
        #     while st and x<=nums[st[-1]]:
        #         st.pop()
        #     if st:
        #         right[i] = st[-1]
        #     st.append(i)
        
        # ans = 0
        # for h, l, r in zip(nums, left, right):
        #     if l < k < r:  # 相比 84 题多了这一行
        #         ans = max(ans, h * (r - l - 1))

        # return ans
# @lc code=end

