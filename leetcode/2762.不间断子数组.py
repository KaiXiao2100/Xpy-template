#
# @lc app=leetcode.cn id=2762 lang=python3
#
# [2762] 不间断子数组
#

# @lc code=start
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        left = 0  # 连续子数组的左边界
        max_ = []  # 最大堆max_[i] = [(最大值的负值，对应的下标)]
        min_ = []  # 最小堆min_[i] = [(最小值，对应的下标)]
        ans = 0
        for right, x in enumerate(nums):  # 遍历连续子数组的右边界
            heappush(max_, (-x, right))  # x入堆
            heappush(min_, (x, right))
            while min_[0][0] + 2 < x:  # x过大了，更新最小值
                if min_[0][1] < left:  # 最大值变动导致的区间左端点右移，导致最小值不在连续区间内了，直接舍弃
                    heappop(min_)
                else:
                    left = heappop(min_)[1] + 1
            while -max_[0][0] > x + 2:  # x过小了
                if max_[0][1] < left:  # 最小值变动导致的区间左端点右移，导致最大值不在连续区间内了，直接舍弃
                    heappop(max_)
                else:
                    left = heappop(max_)[1] + 1
            ans += right - left + 1  # 当前子数组对答案的贡献即为数组的长度
        return ans
    
        # ans = left = 0
        # cnt = Counter()
        # for right, x in enumerate(nums):
        #     cnt[x] += 1
        #     while max(cnt) - min(cnt) > 2:
        #         y = nums[left]
        #         cnt[y] -= 1
        #         if cnt[y] == 0:
        #             del cnt[y]
        #         left += 1
        #     ans += right - left + 1
        # return ans



        # left = res = 0
        # maxd = deque()
        # mind = deque()
        # for right, x in enumerate(nums):
        #     while maxd and x>maxd[-1]:
        #         maxd.pop()
        #     maxd.append(x)
        #     while mind and x<mind[-1]:
        #         mind.pop()
        #     mind.append(x)
        #     while maxd[0]-mind[0]>2:
        #         y = nums[left]
        #         if y==maxd[0]:
        #             maxd.popleft()
        #         if y==mind[0]:
        #             mind.popleft()
        #         left += 1
        #     res += (right-left+1)
        # return res

# @lc code=end

