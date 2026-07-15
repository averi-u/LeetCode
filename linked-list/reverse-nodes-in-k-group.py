# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        out = Optional[ListNode]
        i = 0
        tem_linked_list = Optional[ListNode]

        while(head.next != None):
            dat = head.next
            
            # i is index of enumerated data
            if (i+1)%k == 0:
                for _ in range(k):
                    new_node = ListNode(dat.val)
                    new_node.next = tem_linked_list
                    tem_linked_list = Optional[ListNode]
            
            for _ in range(k):
                out_node = ListNode(tem_linked_list.val)
                out.next = out_node
            
        return out