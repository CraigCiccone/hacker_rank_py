# MEDIUM

# Node is defined as
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    if check_bst(root, None, None):
        return "Yes"
    return "No"


def check_bst(node, low, high) -> bool:
    if node is None:
        return True
    elif low is not None and node.data < low.data:
        return False
    elif high is not None and node.data > high.data:
        return False

    return check_bst(node.left, low, node) and check_bst(node.right, node, high)


if __name__ == "__main__":
    root1 = Node(3)
    root1.left = Node(2)
    root1.right = Node(4)
    root1.left.left = Node(1)
    root1.right.left = Node(5)
    root1.right.right = Node(6)
    print(checkBST(root1))  # No

    root2 = Node(3)
    root2.left = Node(2)
    root2.right = Node(5)
    root2.left.left = Node(1)
    root2.right.left = Node(6)
    root2.right.right = Node(1)
    print(checkBST(root2))  # No

    root3 = Node(4)
    root3.left = Node(2)
    root3.right = Node(6)
    root3.left.left = Node(1)
    root3.left.right = Node(3)
    root3.right.left = Node(5)
    root3.right.right = Node(7)
    print(checkBST(root3))  # Yes

    root4 = Node(1)
    root4.left = Node(2)
    root4.right = Node(4)
    root4.left.left = Node(3)
    root4.left.right = Node(5)
    root4.right.left = Node(6)
    root4.right.right = Node(7)
    print(checkBST(root4))  # No
