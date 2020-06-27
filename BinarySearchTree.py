class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def addItems(self, data):
        if self.root is None:
            self.root = Node(data)
            return
        else:
            temp = self.root
            while temp is not None:
                if temp.data < data and temp.right is None:
                    temp.right = Node(data)
                    return
                elif temp.data > data and temp.left is None:
                    temp.left = Node(data)
                    return
                else:
                    if temp.data > data:
                        temp = temp.left
                    else:
                        temp = temp.right

    def search(self, data):
        temp = self.root
        while temp is not None:
            if temp.data == data:
                print("Found")
                return
            elif temp.data < data:
                temp = temp.right
            else:
                temp = temp.left
        print("Not Found")
        return

    def printnodes(self):
        output = self.in_order_traverse(self.root, "")
        print(output)

    def in_order_traverse(self, node, traversal):
        if node is not None:
            traversal = self.in_order_traverse(node.left, traversal)
            traversal += str(node.data) + "-->"
            traversal = self.in_order_traverse(node.right, traversal)
        return traversal


if __name__ == "__main__":
    BST = BinaryTree()
    BST.addItems(18)
    BST.addItems(11)
    BST.addItems(9)
    BST.addItems(12)
    BST.addItems(13)
    BST.addItems(20)
    BST.addItems(25)
    BST.addItems(30)
    BST.search(31)
    BST.printnodes()

