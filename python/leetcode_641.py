class ListNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left, self.right = left, right


class MyCircularDeque:
    def __init__(self, k: int):
        self.head, self.tail = ListNode(), ListNode()
        self.k, self.len = k, 0
        self.head.right = self.tail
        self.tail.left = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        r = self.head.right
        newNode = ListNode(value, self.head, r)
        self.head.right = newNode
        r.left = newNode
        self.len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        l = self.tail.left
        newNode = ListNode(value, l, self.tail)
        self.tail.left = newNode
        l.right = newNode
        self.len += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        r = self.head.right.right
        self.head.right = r
        r.left = self.head
        self.len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        l = self.tail.left.left
        self.tail.left = l
        l.right = self.tail
        self.len -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.right.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.left.val

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k