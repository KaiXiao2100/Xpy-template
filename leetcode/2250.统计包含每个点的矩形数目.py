#
# @lc app=leetcode.cn id=2250 lang=python3
#
# [2250] 统计包含每个点的矩形数目
# 二刷

# @lc code=start
class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        rectangles.sort(key=lambda r:-r[1])
        n = len(points)
        ans = [0]*n
        i,xs = 0,[]
        for (x,y), id in sorted(zip(points,range(n)),key=lambda x:-x[0][1]):
            start = i
            while i<len(rectangles) and rectangles[i][1]>=y:
                xs.append(rectangles[i][0])
                i += 1
            if start<i:
                xs.sort()
            ans[id] = i-bisect_left(xs,x)
        return ans



# @lc code=end

