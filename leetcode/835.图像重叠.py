#
# @lc app=leetcode.cn id=835 lang=python3
#
# [835] 图像重叠
# 二刷

# @lc code=start
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        cnt = defaultdict(int)
        one=[]
        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    one.append([i,j])
        
        for i in range(n):
            for j in range(n):
                if img2[i][j]:
                    for a,b in one:
                        cnt[(i-a,j-b)] += 1
        
        return max(cnt.values()) if cnt else 0


# @lc code=end

