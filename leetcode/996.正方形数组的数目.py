#
# @lc app=leetcode.cn id=996 lang=python3
#
# [996] 正方形数组的数目
# 

# @lc code=start
class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        def is_perfect_square(el):
            if el<0:
                return False
            return math.sqrt(el)%1==0
        
        @cache
        def dfs(j: int,pre: int)->int:
            if bin(j).count("1")==0:
                return 1
            res = 0
            for x in range(j.bit_length()):
                if (1<<x)&j>0:
                    if pre<0:
                        res += dfs(j^(1<<x),nums[x])
                    else:
                        cur = nums[x] + pre
                        if is_perfect_square(cur):
                            res += dfs(j^(1<<x),nums[x])
            return res
        n = len(nums)
        mask = (1<<n) - 1
        counter = Counter(nums)
        rep = 1
        for k,v in counter.items():
            while v:
                rep *= v
                v -= 1
        return dfs(mask,-1)//rep   #所有排列数//重复数字换位方案数


# @lc code=end

