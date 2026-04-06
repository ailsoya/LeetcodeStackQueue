class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, val):
        node = Node(val)
        if self.tail is None:
            self.tail = node
            self.head = self.tail
        else:
            self.tail.next = node
            self.tail = self.tail.next

    def pop(self):
        if self.is_empty():
            return IndexError

        poped_val = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None

        return poped_val

    def peek(self):
        if self.is_empty():
            return IndexError

        return self.head.value

    def is_empty(self):
        return self.head is None

class MyStack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue2.push(x)

        while not self.queue1.is_empty():
            self.queue2.push(self.queue1.pop())

        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.pop()

    def top(self) -> int:
        return self.queue1.peek()

    def empty(self) -> bool:
        return self.queue1.is_empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
