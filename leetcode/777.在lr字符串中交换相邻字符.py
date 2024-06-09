#
# @lc app=leetcode.cn id=777 lang=python3
#
# [777] 在LR字符串中交换相邻字符
# 

# @lc code=start
class Solution:
    def canTransform(self, start: str, target: str) -> bool:
        if start.replace('X', '') != target.replace('X', ''): return False
        j = 0
        for i, c in enumerate(start):
            if c == 'X': continue
            while target[j] == 'X': j += 1
            if i != j and (c == 'L') != (i > j): return False
            j += 1
        return True

        # 通俗写法
        # n = len(start)
        # i = j = 0
        # while 1:
        #     while i < n and start[i] == 'X':
        #         i += 1
        #     while j < n and end[j] == 'X':
        #         j += 1
        #     if i >= n and j >= n:
        #         return True
        #     if i >= n or j >= n or start[i] != end[j]:
        #         return False
        #     if start[i] == 'L' and i < j:
        #         return False
        #     if start[i] == 'R' and i > j:
        #         return False
        #     i, j = i + 1, j + 1




# @lc code=end

