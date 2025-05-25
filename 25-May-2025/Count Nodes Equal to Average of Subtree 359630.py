# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count=0
        def rec(node):
            nonlocal count
            if not node:
                return 0,0
            summ1, count1 = rec(node.left)
            summ2, count2 = rec(node.right)

            if (summ1+summ2+node.val) // (count1 + count2 +1) == node.val:
                count+=1
            return summ1+summ2+node.val, count1 + count2 +1

        rec(root)
        return count