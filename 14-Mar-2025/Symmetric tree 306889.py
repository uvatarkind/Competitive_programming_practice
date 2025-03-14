# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l=[]
        r=[]
        def left(node):
            if node:    
                l.append(node.val)
                left(node.left)
                
                left(node.right)
            else:
                l.append(None)
        left(root.left)
        def right(node):
            if node:
                r.append(node.val)
                right(node.right)
                
                right(node.left)
            else:
                r.append(None)
        right(root.right)
        if r==l:
            return True
        else:
            return False
        

        
                

           