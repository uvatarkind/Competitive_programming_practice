# Problem: Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        count=0
        while curr:
            count+=1
            curr=curr.next
        if count==n:
            head=head.next
            return head
        count= count-n-1
        curr=head

        for _ in range(count):
            curr=curr.next
        if curr==None or curr.next==None:
            return None
        curr.next= curr.next.next
        return head
        
