# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def rec(node, curr_max, curr_min):
            if not node:
                return curr_max - curr_min
            else:
                curr_max= max(curr_max, node.val)
                curr_min =min(curr_min, node.val)

                left= rec(node.left,curr_max, curr_min)
                right= rec(node.right,curr_max, curr_min)

                return max(left,right)
        return rec(root, root.val, root.val)


                
            
