class Node:

    def __init__(self, info, left, right):
        if (left != None and not isinstance(left, Node)) or (right != None and not isinstance(right, Node)):
            raise Exception('Not a node')
        if (left and left.info > info) or (right and right.info < info):
            raise Exception(
                'Left node has to be lower than current node and right node has to be higher than current node. Please correct')
        self.left = left
        self.right = right
        self.info = info


def test_tree():
    lleft = Node(10, None, None)
    lright = Node(20, None, None)
    left = Node(15, lleft, lright)
    rleft = Node(30, None, None)
    rright = Node(40, None, None)
    right = Node(35, rleft, rright)
    root = Node(25, left, right)
    return root


def print_tree(root):
    if root:
        if root.left:
            print_tree(root.left)
        print root.info
        if root.right:
            print_tree(root.right)


def find_in_tree(root, data):
    if root:
        if data > root.info:
            find_in_tree(root.right, data)
        elif data < root.info:
            find_in_tree(root.left, data)
        else:
            print 'Found'
    else:
        print 'Not Found'


def insert_in_tree(root, node):
    if root:
        if node.info > root.info:
            if root.right:
                return insert_in_tree(root.right, node)
            else:
                root.right = node
        elif node.info < root.info:
            if root.left:
                return insert_in_tree(root.left, node)
            else:
                root.left = node
        else:
            print 'exists'


def delete_node(root, data):
    if not root:
        print 'Cant be deleted'
    else:
        if data < root.info:
            root.left = delete_node(root.left, data)
        elif data > root.info:
            root.right = delete_node(root.right, data)
        else:
            if root.right and root.left:
                substitute = find_substitute(root.right)
                root.info = substitute.info
                root.right = delete_node(root.right, substitute.info)
            else:
                temp = root
                if not root.right:
                    root = root.left
                elif not root.left:
                    root = root.right
                del temp
        return root


def find_substitute(root):
    if root.left:
        return find_substitute(root.left)
    return root


if __name__ == '__main__':
    root = test_tree()
    print_tree(root)
    # print 'finding'
    #find_in_tree(root, 40)
    node = Node(45, None, None)
    node2 = Node(32, None, None)
    print 'inserting'
    insert_in_tree(root, node)
    insert_in_tree(root, node2)
    #find_in_tree(root, 25)
    print_tree(root)
    print 'deleting'
    delete_node(root, 25)
    print_tree(root)
