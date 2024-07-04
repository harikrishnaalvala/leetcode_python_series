class MinStack(object):

    def __init__(self):
        self.top_node = None
        self.stack = []


    def push(self, val: int) -> None:
        if self.top_node is None or val < self.top_node[1]:
            node = (val, val)
        else:
            node = (val, self.top_node[1])
        self.top_node = node
        self.stack.append(node)

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.top_node = self.stack[-1]
        else:
            self.top_node = None

    def top(self) -> int:
        if self.top_node is None:
            return None
        else:
            return self.top_node[0]

    def getMin(self) -> int:
        if self.top_node is None:
            return None
        else:
            return self.top_node[1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
