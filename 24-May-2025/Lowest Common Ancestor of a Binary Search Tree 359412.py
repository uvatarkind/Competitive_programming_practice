# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def rec(node):
            if not node:
                return None
            if p.val< node.val and q.val<node.val:
                return rec(node.left)
            elif p.val> node.val and q.val> node.val:
                return rec(node.right)
            else:
                return node
        
        return rec(root)
            




        