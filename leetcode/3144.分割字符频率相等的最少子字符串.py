#
# @lc app=leetcode.cn id=3144 lang=python3
#
# [3144] 分割字符频率相等的最少子字符串
#

# @lc code=start
class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        n = len(s)

        @cache
        def dfs(i: int)->int:
            if i==n:
                return 0
            res = inf
            cnt = Counter()
            for j in range(i,n):
                cnt[s[j]] = cnt[s[j]] + 1
                if (j - i + 1) % len(cnt):
                    continue
                if len(set(cnt.values())) == 1:
                    res = min(res,dfs(j+1)+1)
            return res
        return dfs(0)


# @lc code=end

