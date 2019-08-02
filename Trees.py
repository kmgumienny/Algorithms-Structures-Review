def example1():

    class Node:

        def __init__(self, value):
            self.value = value
            self.right = None
            self.left = None

    class BinarySearchTree:

        def __init__(self):
            self.root = None

        def insert(self, value):
            if not isinstance(value, int):
                print("Integers only!")
                return
            new_node = Node(value)
            if self.root is None:
                self.root = new_node
            else:
                current_tree_node = self.root
                while current_tree_node is not None:
                    if current_tree_node.value >= new_node.value:
                        if current_tree_node.left is None:
                            current_tree_node.left = new_node
                            return
                        else:
                            current_tree_node = current_tree_node.left
                    if current_tree_node.value <= new_node.value:
                        if current_tree_node.right is None:
                            current_tree_node.right = new_node
                            return
                        else:
                            current_tree_node = current_tree_node.right

        def lookup(self, value):
            if not isinstance(value, int):
                print("Integers only!")
                return
            current_tree_node = self.root
            if current_tree_node is None:
                print("Tree not yet instantiated.")
            else:
                while current_tree_node is not None:
                    if current_tree_node.value == value:
                        print("{} Found".format(value))
                        return
                    elif current_tree_node.value > value:
                        current_tree_node = current_tree_node.left
                    elif current_tree_node.value < value:
                        current_tree_node = current_tree_node.right
                print("{} not in Tree".format(value))

        def remove(self, value):
            if self.root is None:
                print("Nothing to delete")
                return

            current_node = self.root
            parent_node = None
            while current_node is not None:
                if value < current_node.value:
                    parent_node = current_node
                    current_node = current_node.left
                elif value > current_node.value:
                    parent_node = current_node
                    current_node = current_node.right
                elif value == current_node.value:
                    # No right child
                    if current_node.right is None:
                        if parent_node is None:
                            self.root = current_node.left
                        else:
                            if current_node.value < parent_node.value:
                                parent_node.left = current_node.left
                            elif current_node.value > parent_node.value:
                                parent_node.right = current_node.left
                    # Right child with no left child
                    elif current_node.right.left is None:
                        current_node.right.left = current_node.left
                        if parent_node is None:
                            self.root = current_node.right
                        else:
                            if current_node.value < parent_node.value:
                                parent_node.left = current_node.right
                            elif current_node.value > parent_node.value:
                                parent_node.right = current_node.right
                    # Right child with a left child
                    else:
                        leftmost = current_node.right.left
                        leftmost_parent = current_node.right
                        while leftmost.left is not None:
                            leftmost_parent = leftmost
                            leftmost = leftmost.left
                        leftmost_parent.left = leftmost.right
                        leftmost.left = current_node.left
                        leftmost.right = current_node.right

                        if parent_node is None:
                            self.root = leftmost
                        else:
                            if current_node.value < parent_node.value:
                                parent_node.left = leftmost
                            elif current_node.value > parent_node.value:
                                parent_node.right = leftmost

            print("Did not find the value")

    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    tree.lookup(170)
    tree.lookup(1)
    tree.lookup(15)
    tree.lookup(60)


example1()
