class LRUCache:
    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.MRU = self.Node(-1, -1)
        self.LRU = self.Node(-1, -1)
        self.MRU.next = self.LRU
        self.LRU.prev = self.MRU

    def addNode(self, newNode):
        temp = self.MRU.next
        self.MRU.next = newNode
        newNode.prev = self.MRU
        newNode.next = temp
        temp.prev = newNode

    def deleteNode(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key not in self.hashMap:
            return -1
        self.put(key, self.hashMap[key].val)
        return self.hashMap[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            node = self.hashMap[key]
            self.deleteNode(node)
            node.val = value
            self.addNode(node)
            self.hashMap[key] = self.MRU.next
        else:
            if len(self.hashMap) == self.capacity:
                prev = self.LRU.prev
                self.deleteNode(prev)
                del self.hashMap[prev.key]
            newNode = self.Node(key, value)
            self.addNode(newNode)
            self.hashMap[key] = self.MRU.next
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
