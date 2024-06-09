#
# @lc app=leetcode.cn id=963 lang=python3
#
# [963] 最小面积矩形 II
# 

# @lc code=start
class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        def distance(p1,p2):
            return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**0.5
        def center(p1,p2):
            return [(p1[0]+p2[0])/2,(p1[1]+p2[1])/2]
        def area(p1,p2,p3):
            return distance(p1,p3)*distance(p2,p3)

        dic = {}
        n = len(points)
        res = float('inf')
        for i in range(n):
            for j in range(i+1,n):
                dist_ij = distance(points[i],points[j])
                center_ij = center(points[i],points[j])
                Strij = ','.join([str(dist_ij)] + [str(item) for item in center_ij])
                if Strij not in dic:
                    dic[Strij] = [[points[i],points[j]]]
                else:
                    for it in dic[Strij]:
                        res = min(res,area(it[0],it[1],points[i]))
                    dic[Strij].append([points[i],points[j]])
        return res if res<float('inf') else 0

# @lc code=end

