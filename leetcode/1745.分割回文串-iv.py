#
# @lc app=leetcode.cn id=1745 lang=python3
#
# [1745] 分割回文串 IV
# 二刷 manacher

# @lc code=start
class Solution:
    def checkPartitioning(self, s: str) -> bool:
        dp = [[True for __ in range(len(s))] for __ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False
        return any([dp[0][i-1] and dp[i][j] and dp[j+1][-1] for i in range(1, len(s)) for j in range(i, len(s)-1)])

        
            



# @lc code=end

