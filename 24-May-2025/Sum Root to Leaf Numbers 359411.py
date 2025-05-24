# Problem: Sum Root to Leaf Numbers - https://leetcode.com/problems/sum-root-to-leaf-numbers/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        def rec(node, path):
            if not node:
                return 0
            else:
                path= path*10 + node.val
                if not node.left and not node.right:
                    return path
                else:
                    return rec(node.left, path)+ rec(node.right, path) 
        return rec(root,0)