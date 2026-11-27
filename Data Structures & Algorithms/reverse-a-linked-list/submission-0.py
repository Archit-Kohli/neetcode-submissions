# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        prev = head
        if not head.next:
            return head
        cur = head.next
        while cur:
            # print(prev.val, cur.val)
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head.next = None
        return prev
