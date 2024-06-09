#
# @lc app=leetcode.cn id=1733 lang=python3
#
# [1733] 需要教语言的最少人数
# 二刷

# @lc code=start
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        ability = [set(lang) for lang in languages]
        friendships = [[x, y] for x, y in friendships if len(ability[x - 1].intersection(ability[y - 1])) == 0]

        ans = len(languages)
        for i in range(1, n + 1):
            cur = set()
            for x, y in friendships:
                if i not in ability[x - 1]:
                    cur.add(x)
                if i not in ability[y - 1]:
                    cur.add(y)

            ans = ans if ans < len(cur) else len(cur)
        return ans


# @lc code=end

