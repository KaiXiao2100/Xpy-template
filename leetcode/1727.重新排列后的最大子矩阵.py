#
# @lc app=leetcode.cn id=1727 lang=python3
#
# [1727] 重新排列后的最大子矩阵
# 二刷

# @lc code=start
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m,n=len(matrix),len(matrix[0])
        res=0
        arr=[0]*(n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    arr[j]+=1
                else:
                    arr[j]=0
                    
            tmp=sorted(arr,reverse=True)
            for j in range(n):
                res=max(res,tmp[j]*(j+1))
            
        return res

# @lc code=end

