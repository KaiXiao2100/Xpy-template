#
# @lc app=leetcode.cn id=1882 lang=python3
#
# [1882] 使用服务器处理任务
# 二刷(重点)

# @lc code=start
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n,m = len(servers),len(tasks)
        heap1,heap2 = [],[]
        for i,h in enumerate(servers):
            heappush(heap1,(h,i))
        
        res = [-1]*m
        for i,t in enumerate(tasks):
            while heap2 and heap2[0][0]<=i:
                end,w,index = heappop(heap2)
                heappush(heap1,(w,index))
            
            if heap1:
                w,index = heappop(heap1)
                res[i] = index
                heappush(heap2,(i+t,w,index))
            else:
                end,w,index=heappop(heap2)
                res[i] = index
                heappush(heap2,(end+t,w,index))

        return res



# @lc code=end

