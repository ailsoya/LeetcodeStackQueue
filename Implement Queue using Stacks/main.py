class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def pop(self):
        if self.is_empty():
            return IndexError

        poped_val = self.head.value
        self.head = self.head.next
        return poped_val

    def peek(self):
        if self.is_empty():
            return IndexError

        return self.head.value

    def is_empty(self):
        return self.head is None

class MyQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()


    def push(self, x: int) -> None:
        self.stack_in.push(x)

    def pop(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

        return self.stack_out.pop()

    def peek(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
