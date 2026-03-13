# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
        def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
            templist = []
            tempHead = head
            if head == None:
                return head
            returnhead = head.next
            #for node in tempHead:
            #    templist[i] = node
            #    i = i + 1
            size = 0
            while tempHead:
                templist.append(tempHead)
                #print(templist[size].val)
                tempHead = tempHead.next
                size += 1
            x = 0
            #print(size)
            if len(templist) == 1:
                return head
            for item in templist:
                if x + 1 < size:
                    tempNode = templist[x]
                    templist[x] = templist[x+1]
                    templist[x+1] = tempNode
                x = x + 2
            #print(templist[0].val)    
            #print(templist[1].val)   
            #print(templist[2].val)    
            #print(templist[3].val)   
            j = 1
            for item in templist:
                if (j < size): 
                    #j = 1 <= size --> Node 1.next = templist[1] 
                    #j = 2 <= size --> Node 2.next = templist[2]
                    #j = 3 <= size --> Node 3.next = templist[3]
                    #j = 4 <= size --> Node 4.next = None
                    item.next = templist[j]
                else:
                    item.next = None
                j = j + 1
            return returnhead