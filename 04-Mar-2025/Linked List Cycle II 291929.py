# Problem: Linked List Cycle II - https://leetcode.com/problems/linked-list-cycle-ii/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=fast=head

        while fast and fast.next:

            fast=fast.next.next
            slow=slow.next

            if slow == fast:
                count=0
                ptr=head
                while slow!=ptr:
                    count+=1
                    slow=slow.next
                    ptr=ptr.next
                print("tail connects to node index",count)

                return slow
        return None
