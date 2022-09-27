#lc easy
'''
Given the head of a LinkedList with a cycle, find the length of the cycle.
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                pos = slow
                len = 0
                while True:
                    pos = pos.next
                    len += 1
                    if pos == slow:
                        break
                return len
        