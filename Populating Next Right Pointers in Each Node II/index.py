"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        q = [root]
        while len(q) > 0:
            l = len(q)
            x = Node(0)
            for _ in range(l):
                r = q.pop(0)
                x.next = r
                x = x.next
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)
            x.next = None
        return root
