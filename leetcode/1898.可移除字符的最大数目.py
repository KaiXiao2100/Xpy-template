#
# @lc app=leetcode.cn id=1898 lang=python3
#
# [1898] 可移除字符的最大数目
#

# @lc code=start
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def check(index):
            temp = list(s)
            for i in range(index):
                temp[removable[i]] = ""
            ss = "".join(temp)
            id = 0
            for i in range(len(ss)):
                if ss[i]==p[id]:
                    id+=1
                if id==len(p):
                    return True
            return False
        left,right = 0,len(removable)+1
        while left<right:
            mid = (left+right)//2
            if check(mid):
                left = mid+1
            else:
                right = mid
        return left-1
        
# @lc code=end

