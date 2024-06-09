#
# @lc app=leetcode.cn id=2831 lang=python3
#
# [2831] 找出最长等值子数组
# 二刷（重点）

# @lc code=start
class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        pos_lists = defaultdict(list)
        for i, x in enumerate(nums):
            pos_lists[x].append(i - len(pos_lists[x]))

        ans = 0
        for pos in pos_lists.values():
            if len(pos) <= ans:
                continue  # 无法让 ans 变得更大
            left = 0
            for right, p in enumerate(pos):
                while p - pos[left] > k:  # 要删除的数太多了
                    left += 1
                ans = max(ans, right - left + 1)
        return ans


        # n = len(nums)

        # cnt = defaultdict(list)
        # for i,a in enumerate(nums):
        #     cnt[a].append(i)
        
        # def check(m: int)->int:
        #     ans = 1
        #     for a in cnt.keys():
        #         t = k
        #         arr = cnt[a]
        #         l,r = 0,0
        #         while r<len(arr)-1:
        #             need = arr[r+1]-arr[r]-1
        #             while l<r and need>t:
        #                 t += arr[l+1]-arr[l]-1
        #                 l +=1
        #             if need <= t:
        #                 t -= need
        #                 r += 1
        #                 ans = max(ans,r-l+1)
        #             else:
        #                 t = k
        #                 r += 1
        #                 l = r
        #     return ans>=m
                    
        # l,r = 1,max(len(cnt[a]) for a in cnt.keys())
        # while l<=r:
        #     m = (l+r)//2
        #     if check(m):
        #         l = m+1
        #     else:
        #         r = m-1
        # return r

# @lc code=end

