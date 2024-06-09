#
# @lc app=leetcode.cn id=2147 lang=python3
#
# [2147] 分隔长廊的方案数
# 二刷

# @lc code=start
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        ans, cnt_s, pre = 1, 0, 0
        for i, ch in enumerate(corridor):
            if ch == 'S':
                # 对第 3,5,7,... 个座位，可以在其到其左侧最近座位之间的任意一个位置放置屏风
                cnt_s += 1
                if cnt_s >= 3 and cnt_s % 2:
                    ans = ans * (i - pre) % 1000000007
                pre = i  # 记录上一个座位的位置
        return ans if cnt_s and cnt_s % 2 == 0 else 0  
# @lc code=end

