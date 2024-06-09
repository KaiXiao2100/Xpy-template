#
# @lc app=leetcode.cn id=1488 lang=python3
#
# [1488] 避免洪水泛滥
# 二刷  贪心+平衡树

# @lc code=start
from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1]*len(rains)
        st = SortedList()
        mp = {}
        for i,rain in enumerate(rains):
            if rain==0:
                st.add(i)
            else:
                ans[i] = -1
                if rain in mp:
                    p = st.bisect(mp[rain])
                    if p==len(st):
                        return []
                    ans[st[p]] = rain
                    st.discard(st[p])

                mp[rain] = i

        return ans

# @lc code=end

