# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        newList = ListNode()
        pq = PriorityQueue()
        for i in range(len(lists)):
            if lists[i] is not None:
                pq.put((lists[i].val, i))
        current = newList
        while not pq.empty():
            currval, currlist = pq.get()
            current.next = ListNode(currval)
            
            lists[currlist] = lists[currlist].next
            if lists[currlist] is not None:
                pq.put((lists[currlist].val, currlist))
            current = current.next
        return newList.next