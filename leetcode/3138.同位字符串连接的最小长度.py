#
# @lc app=leetcode.cn id=3138 lang=python3
#
# [3138] 同位字符串连接的最小长度
#

# @lc code=start
class Solution:
    def minAnagramLength(self, s: str) -> int:
        n = len(s)
        for k in range(1, n // 2 + 1):
            if n % k:
                continue
            cnt0 = Counter(s[:k])
            for i in range(k * 2, n + 1, k):
                if Counter(s[i - k: i]) != cnt0:
                    break
            else:
                return k
        return n

        # n = len(s)
        # orda = ord('a')
        # a = [ord(ch) - orda for ch in s]
        
        # for k in range(1, n):
        #     if n % k == 0:
        #         c = [0] * 26
        #         for i in range(k):
        #             c[a[i]] += 1
        #         ok = True
        #         for start in range(k, n, k):
        #             d = [0] * 26
        #             for i in range(start, start + k):
        #                 d[a[i]] += 1
        #             if c != d:
        #                 ok = False
        #                 break
        #         if ok:
        #             return k
        # return n

# @lc code=end

