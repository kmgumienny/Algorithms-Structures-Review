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


def example1():

    def linear_search():
        beasts = ['Centaur', 'Godzilla', 'Mosura', 'Minotaur', 'Hydra', 'Nessie']

        # This will search in Linear Time
        print(beasts.index('Godzilla'))

    linear_search()


def example2():

    def breadth_first_search(a_tree):
        current_node = a_tree.root
        visited = []
        queue = [current_node]
        while len(queue) > 0:
            current_node = queue.pop(0)
            visited.append(current_node)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        for node in visited:
            print(node.value, end=' ')

        print()

    breadth_first_search(tree)


def example3():

    def breadth_first_search_recursive(queue, visited):
        if len(queue) == 0:
            return visited
        current_node = queue.pop(0)
        visited.append(current_node)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)
        return breadth_first_search_recursive(queue, visited)

    visited_list = breadth_first_search_recursive([tree.root], [])

    for node in visited_list:
        print(node.value, end=' ')
    print()


def example4():

    def depth_first_search_in_order(a_node, visited):
        if a_node.left is not None:
            depth_first_search_in_order(a_node.left, visited)
        visited.append(a_node)
        if a_node.right is not None:
            depth_first_search_in_order(a_node.right, visited)
        return visited

    visited_list = depth_first_search_in_order(tree.root, [])

    for node in visited_list:
        print(node.value, end=' ')


def example5():

    def depth_first_search_pre_order(a_node, visited):
        visited.append(a_node)
        if a_node.left is not None:
            depth_first_search_pre_order(a_node.left, visited)
        if a_node.right is not None:
            depth_first_search_pre_order(a_node.right, visited)
        return visited

    visited_list = depth_first_search_pre_order(tree.root, [])

    for node in visited_list:
        print(node.value, end=' ')


def example5():

    def depth_first_search_post_order(a_node, visited):
        if a_node.left is not None:
            depth_first_search_post_order(a_node.left, visited)
        if a_node.right is not None:
            depth_first_search_post_order(a_node.right, visited)
        visited.append(a_node)
        return visited

    visited_list = depth_first_search_post_order(tree.root, [])

    for node in visited_list:
        print(node.value, end=' ')


# example1()
tree = BinarySearchTree()
tree.insert(9)
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
# example2()
# example3()
# example4()
example5()
