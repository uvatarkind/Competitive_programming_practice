# Problem: Remove Linked List Elements - https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy= ListNode(-1)
        dummy.next =head
        prev, curr= dummy,head
        while curr:
            if curr.val== val:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return dummy.next