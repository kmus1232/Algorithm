class Node:
    def __init__(self, val):
        self.val = val
        self.up = None
        self.down = None
        self.now_in_list = True


class LinkedList:
    def __init__(self, n, k):
        self.node_arr = [Node(i) for i in range(n)]
        for i in range(n):
            if i < n - 1:
                self.node_arr[i].down = self.node_arr[i + 1]
            if i > 0:
                self.node_arr[i].up = self.node_arr[i - 1]
        self.head = self.node_arr[0]
        self.tail = self.node_arr[-1]
        self.curr = self.node_arr[k]
        self.del_stack = []
        self.restore = None
        self.tmp = None

    def D_X(self, x):
        for i in range(x):
            self.curr = self.curr.down

    def U_X(self, x):
        for i in range(x):
            self.curr = self.curr.up

    def C(self):
        self.del_stack.append(self.curr)
        self.curr.now_in_list = False
        if self.curr == self.head:
            self.curr = self.curr.down
            self.head = self.curr
            self.curr.up = None
        elif self.curr == self.tail:
            self.curr = self.curr.up
            self.tail = self.curr
            self.curr.down = None
        else:
            self.curr.up.down = self.curr.down
            self.curr.down.up = self.curr.up
            self.curr = self.curr.down

    def Z(self):
        self.restore = self.del_stack.pop()
        self.restore.now_in_list = True
        if self.restore.up is not None:
            if self.restore.down is not None:  # head, tail이 아닌 노드
                self.tmp = self.node_arr[self.restore.up.val]
                self.tmp.down.up = self.restore
                self.tmp.down = self.restore
            else:  # tail 노드
                self.tmp = self.node_arr[self.restore.up.val]
                self.tmp.down = self.restore
                self.tail = self.restore
        else:  # head 노드
            self.tmp = self.node_arr[self.restore.down.val]
            self.tmp.up = self.restore
            self.head = self.restore

    def check_nodes_in_list(self):
        rst = ""
        for node in self.node_arr:
            if node.now_in_list:
                rst += "O"
            else:
                rst += "X"
        return rst


def solution(n, k, cmd):
    linked_list = LinkedList(n, k)
    for c in cmd:
        if c[0] == "C":
            linked_list.C()
        elif c[0] == "Z":
            linked_list.Z()
        else:
            c, n = c.split()
            n = int(n)
            if c == "D":
                linked_list.D_X(n)
            else:
                linked_list.U_X(n)

    return linked_list.check_nodes_in_list()