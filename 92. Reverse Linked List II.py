# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        leftPrev, cur = dummy, head

        # 1. to reach the left valued node
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next

        # 2. to reverse the required part
        # cur = "left", leftPrev = "node before left"
        prev = None
        for i in range(right - left + 1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp

        # 3. cleanup and connect 
        leftPrev.next.next = cur
        leftPrev.next = prev

        return dummy.next

