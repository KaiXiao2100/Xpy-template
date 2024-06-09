#
# @lc app=leetcode.cn id=2434 lang=python3
#
# [2434] 使用机器人打印字典序最小的字符串
# 二刷

# @lc code=start
class Solution:
    def robotWithString(self, s: str) -> str:
        ans = []
        cnt = Counter(s)
        min = 0
        st = []
        for c in s:
            cnt[c] -= 1
            while min<25 and cnt[ascii_lowercase[min]] == 0:
                min += 1
            st.append(c)
            while st and st[-1] <= ascii_lowercase[min]:
                ans.append(st.pop())
        return ''.join(ans)


# @lc code=end

