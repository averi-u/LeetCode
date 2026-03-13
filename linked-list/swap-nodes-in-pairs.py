# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
        def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to simplify head swaps
        dummy = ListNode(0, head)
        prev = dummy

        # While there are at least two nodes to swap
        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # Rewire pointers to swap first and second
            first.next = second.next
            second.next = first
            prev.next = second

            # Move prev to the end of the swapped pair
            prev = first

        return dummy.next