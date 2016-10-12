class Queue:

    def __init__(self, item=None):
        self.q = []
        if item:
            self.q.append(item)

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        if self.q:
            out = self.q[0]
            del self.q[0]
            return out
        return None

    def dequeue_all(self):
        while(self.q):
            print self.dequeue()

    def is_empty(self):
        return self.q == []


def test_queue():
    q = Queue()
    q.enqueue('0')
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    q.dequeue_all()


class Node:

    def __init__(self, info, left, right):
        if (left != None and not isinstance(left, Node)) or (right != None and not isinstance(right, Node)):
            raise Exception(isinstance(left, Node))
        self.left = left
        self.right = right
        self.info = info


def level_order_traversal(q):
    if q.is_empty():
        return
    node = q.dequeue()
    print node.info
    if node.left:
        q.enqueue(node.left)
    if node.right:
        q.enqueue(node.right)
    level_order_traversal(q)


def create_test_tree():
    lleft = Node('2', None, None)
    lright = Node('1', None, None)
    left = Node('4', lleft, lright)
    rright = Node('0', None, None)
    right = Node('3', None, rright)
    root = Node('5', left, right)
    return root

if __name__ == '__main__':
    test_queue()
    print 'Testing level order traversal'
    root = create_test_tree()
    q = Queue(root)
    level_order_traversal(q)
