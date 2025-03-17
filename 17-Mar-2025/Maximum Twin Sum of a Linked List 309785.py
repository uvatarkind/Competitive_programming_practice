# Problem: Maximum Twin Sum of a Linked List - https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class Solution:
    def pairSum(self, head: ListNode) -> int:
        
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        max_sum = 0
        n = len(values)
        
        for i in range(n // 2):
            twin_sum = values[i] + values[n - i - 1]
            max_sum = max(max_sum, twin_sum)
        
        return max_sum 