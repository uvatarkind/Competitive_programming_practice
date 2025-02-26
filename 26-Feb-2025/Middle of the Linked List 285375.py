# Problem: Middle of the Linked List - https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head)
        cur = head
        count = 0
        while cur:
            print(cur.val)
            count+=1
            cur = cur.next
        mid = count//2 
        cur = head
        
        for _ in range(mid):
            cur = cur.next
        return cur