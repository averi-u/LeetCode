# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> 
        Optional[ListNode], k: int) -> Optional[ListNode]:
        
            if head is None or k == 1:
                return head

            dummy = ListNode(0, head)
            group_prev = dummy

            while True:
                # 1) Find the end of the next k-group
                kth = group_prev
                for _ in range(k):
                    kth = kth.next
                    if kth is None:
                        return dummy.next  # less than k nodes left, done

                group_start = group_prev.next
                group_next = kth.next  # node after the group

                # 2) Reverse the group [group_start .. kth]
                prev = group_next
                curr = group_start
                while curr is not group_next:
                    nxt = curr.next
                    curr.next = prev
                    prev = curr
                    curr = nxt

                # 3) Reconnect: group_prev -> kth (new head), group_start (new tail) -> group_next
                group_prev.next = kth
                group_prev = group_start