#
# @lc app=leetcode.cn id=2398 lang=python3
#
# [2398] 预算内的最多机器人数目
#

# @lc code=start
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        ps = [0]
        for a in runningCosts:
            ps.append(ps[-1]+a)

        ans = 0
        l,r = 0,0
        q = deque([])#递减
        
        while r<n:
            time = chargeTimes[r]
            while len(q)>0 and chargeTimes[q[-1]] <= time:
                q.pop()
            q.append(r)
            total = chargeTimes[q[0]] + (r-l+1)*(ps[r+1] - ps[l])
            while total > budget:
                while len(q)>0 and q[0] <= l:
                    q.popleft()
                l+=1
                if len(q)>0:
                    total = chargeTimes[q[0]] + (r-l+1)*(ps[r+1] - ps[l])
                else:
                    total = 0
            ans = max(ans,r-l+1)
            r+=1
        return ans

# @lc code=end

