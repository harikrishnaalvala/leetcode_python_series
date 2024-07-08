# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        newList = ListNode()
        new = newList

        while n:
            # Find list with smallest value:
            smallestNode = ListNode(float('inf'))
            smallestIndex = -1
            for i in range(n):
                listNode = lists[i]
                if listNode and listNode.val < smallestNode.val:
                    smallestNode = listNode
                    smallestIndex = i
            
            if smallestIndex == -1:
                break
            
            new.next = ListNode(smallestNode.val)
            new = new.next

            if smallestNode.next:
                lists[smallestIndex] = smallestNode.next
            else:
                lists.pop(smallestIndex)
                n-=1
                
        return newList.next
