# -*- coding: utf-8 -*-
# 留给读者练习，如果实在想不出，在第 5 章栈里 stack.py 会有实现
class Node(object):
    __slots__ = ('value', 'prev', 'next')   # save memory ; 使用slots可以让内存使用减少3.5倍！！# 通过 (200 - 4) / ((60 - 4) * 1.0) 计算得来
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next
class CircularDoubleLinkedList(object):
    """循环双端链表 ADT
    多了个循环其实就是把 root 的 prev 指向 tail 节点，串起来
    """
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0
    def __len__(self):
        return self.length
    def headnode(self):
        return self.root.next
    def tailnode(self):
        return self.root.prev
    def append(self, value):    # O(1), 你发现一般不用 for 循环的就是 O(1)，有限个步骤
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root
        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1
    def appendleft(self, value):
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        if self.root.next is self.root:   # empty
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1
    def remove(self, node):      # O(1)，传入node 而不是 value 我们就能实现 O(1) 删除
        """remove
        :param node  # 在 lru_cache 里实际上根据key 保存了整个node:
        """
        if node is self.root:
            return
        else:    #
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node
    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode
    def __iter__(self):
        for node in self.iter_node():
            yield node.value
    def iter_node_reverse(self):
        """相比单链表独有的反序遍历"""
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode
class EmptyError(Exception):
    """自定义异常"""
    pass
class Deque(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_link_list = CircularDoubleLinkedList()
    def append(self, value):    # O(1)
        """ 队尾添加元素 """
        return self._item_link_list.append(value)
    def appendleft(self, value):    # O(1)
        """ 队尾添加元素 """
        return self._item_link_list.appendleft(value)
    def pop(self):
        """队列右边删除元素"""
        if len(self) <= 0:
            raise EmptyError('empty queue')
        return self._item_link_list.remove(self._item_link_list.tailnode()).value
    def popleft(self):
        """队列左边删除元素"""
        if len(self) <= 0:
            raise EmptyError('empty queue')
        return self._item_link_list.remove(self._item_link_list.headnode()).value
    def __iter__(self):
        for node in self._item_link_list.iter_node():
            yield node.value
    def __len__(self):
        return len(self._item_link_list)
def test_deque():
    q = Deque()
    q.append(0)
    q.append(1)
    q.append(2)
    q.appendleft(8)
    q.appendleft(9)
    q.appendleft(10)
    print list(q)
    assert len(q) == 6
    print q.pop()
    print q.popleft()
    assert q.pop() == 1
    assert q.popleft() == 9
test_deque()