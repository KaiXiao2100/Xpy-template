#
# @lc app=leetcode.cn id=2509 lang=python3
#
# [2509] 查询树中环的长度
# 二刷 ，最近公共祖先

# @lc code=start
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        for i, (a, b) in enumerate(queries):
            if a > b: a, b = b, a  # 保证 a <= b
            d = b.bit_length() - a.bit_length()
            queries[i] = d + (a ^ (b >> d)).bit_length() * 2 + 1
        return queries

        # ans = []
        # for i, (a, b) in enumerate(queries):
        #     res = 1
        #     while a != b:
        #         if a > b: a //= 2
        #         else: b //= 2
        #         res += 1
        #     ans.append(res)

        # return ans


# @lc code=end

