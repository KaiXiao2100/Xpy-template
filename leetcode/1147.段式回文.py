#
# @lc app=leetcode.cn id=1147 lang=python3
#
# [1147] 段式回文
#

# @lc code=start
class Solution:
    def longestDecomposition(self, text: str) -> int:
        if text == "":
            return 0
        for i in range(1, len(text) // 2 + 1):  # 枚举前后缀长度
            if text[:i] == text[-i:]:  # 立刻分割
                return 2 + self.longestDecomposition(text[i:-i])
        return 1  # 无法分割
    
        # n = len(text)
        # g = [[False]*n for _ in range(n)]
        
        # @cache
        # def dfs(i: int,j: int)->int:
        #     if i>j:
        #         return 0
        #     if i==j:
        #         return 1
        #     res = 1
        #     k = j-i+1
        #     for l in range(1,k//2 + 1):
        #         if text[i:i+l] == text[j-l+1:j+1]:
        #             res = max(res,dfs(i+l,j-l)+2)
        #     return res

        # return dfs(0,n-1)

# @lc code=end

