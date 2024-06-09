#
# @lc app=leetcode.cn id=2516 lang=python3
#
# [2516] 每种字符至少取 K 个
#

# @lc code=start
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        j = n = len(s)
        c = Counter()
        while c['a'] < k or c['b'] < k or c['c'] < k:
            if j == 0: return -1  # 所有字母都取也无法满足要求
            j -= 1
            c[s[j]] += 1
        ans = n - j  # 左侧没有取字符
        for i, ch in enumerate(s):
            c[ch] += 1
            while j < n and c[s[j]] > k:  # 维护 j 的最大下标
                c[s[j]] -= 1
                j += 1
            ans = min(ans, i + 1 + n - j)
            if j == n: break
        return ans
# @lc code=end

