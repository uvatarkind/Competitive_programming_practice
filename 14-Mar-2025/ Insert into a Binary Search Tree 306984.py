# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val,None,None)
        
        def insert(node):
            if node:
                if node.val<val:

                    if node.right==None:
                        node.right=TreeNode(val,None,None)
                    else:
                        return insert(node.right)
                else:
                    if node.left==None:
                        node.left=TreeNode(val,None,None)
                    else:
                        return insert(node.left)
                
        insert(root)
        return root


        