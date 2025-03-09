# Problem: Reverse Nodes in k-Group - https://leetcode.com/problems/reverse-nodes-in-k-group/

# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def segment_reverser(self, left:Optional[ListNode],right:Optional[ListNode])->tuple:
        prev, curr = None, left
        next_node = None
        while curr and prev != right:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return (prev,left)


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        cur = head
        count = 0
        lft = head
        prev = None
        dummy = ListNode(0)
        dummy.next = head
        next_seg = None
        while cur:
            count+=1
            if count == k:
                next_seg=cur.next
                left,right = self.segment_reverser(lft,cur)
                if prev:
                    prev.next = left
                else:
                    dummy.next = left
                right.next = next_seg
                prev = right
                lft = next_seg
                count = 0
                cur = next_seg
            else:
                cur = cur.next
        return dummy.next