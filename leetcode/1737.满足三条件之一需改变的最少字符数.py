#
# @lc app=leetcode.cn id=1737 lang=python3
#
# [1737] 满足三条件之一需改变的最少字符数
# 二刷

# @lc code=start
class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        counter1,counter2=[0]*26,[0]*26
        for c in a: counter1[ord(c)-ord('a')]+=1
        for c in b: counter2[ord(c)-ord('a')]+=1

        way1=min(sum(counter1[i:])+sum(counter2[:i]) for i in range(1,26))
        way2=min(sum(counter2[i:])+sum(counter1[:i]) for i in range(1,26))
        way3=min(len(a)+len(b)-counter1[i]-counter2[i] for i in range(26))
        return min(way1,way2,way3)



# @lc code=end

