#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
# 二刷

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0  # 二叉搜索树可以为空

        def dfs(node: Optional[TreeNode]) -> Tuple:
            if node is None:
                return inf, -inf, 0

            l_min, l_max, l_sum = dfs(node.left)  # 递归左子树
            r_min, r_max, r_sum = dfs(node.right)  # 递归右子树
            x = node.val
            if x <= l_max or x >= r_min:  # 不是二叉搜索树
                return -inf, inf, 0

            s = l_sum + r_sum + x  # 这棵子树的所有节点值之和
            nonlocal ans
            ans = max(ans, s)

            return min(l_min, x), max(r_max, x), s

        dfs(root)
        return ans

# @lc code=end

