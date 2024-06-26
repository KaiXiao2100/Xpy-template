#
# @lc app=leetcode.cn id=2564 lang=python3
#
# [2564] 子字符串异或查询
#   二刷(重点)

# @lc code=start
class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:
        n, m = len(s), {}
        if (i := s.find('0')) >= 0:
            m[0] = (i, i)  # 这样下面就可以直接跳过 '0' 了，效率更高

        #预处理出所有数字最先出现的位置
        for l, c in enumerate(s):
            if c == '0': continue
            x = 0
            for r in range(l, min(l + 30, n)):
                x = (x << 1) | (ord(s[r]) & 1)
                if x not in m:
                    m[x] = (l, r)
        NOT_FOUND = (-1, -1)
        return [m.get(x ^ y, NOT_FOUND) for x, y in queries]



# @lc code=end

