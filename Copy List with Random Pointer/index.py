"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def insertAtTail(self, head_tail, data):
        newNode = Node(data)
        if head_tail[0] is None:
            head_tail[0] = newNode
            head_tail[1] = newNode
        else:
            head_tail[1].next = newNode
            head_tail[1] = newNode
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
         # Step 1: Create Cloned List
        cloneHead = [None, None]  # cloneHead[0] -> head, cloneHead[1] -> tail
        temp = head
        while temp:
            self.insertAtTail(cloneHead, temp.val)
            temp = temp.next

        # Step 2: Store the mapping of the originalNode and cloneNode
        mapping = {}
        originalNode = head
        cloneNode = cloneHead[0]
        while originalNode and cloneNode:
            mapping[originalNode] = cloneNode
            originalNode = originalNode.next
            cloneNode = cloneNode.next

        # Step 3: Join the Random nodes based on mappings of the original and Cloned Nodes
        originalNode = head
        cloneNode = cloneHead[0]
        while originalNode and cloneNode:
            if originalNode.random:
                cloneNode.random = mapping[originalNode.random]
            cloneNode = cloneNode.next
            originalNode = originalNode.next

        return cloneHead[0]
