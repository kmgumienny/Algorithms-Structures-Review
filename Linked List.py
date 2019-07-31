# making our own linked list


def example1():

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:

        def __init__(self, value=None):
            if value is None:
                self.head = None
            else:
                self.head = Node(value)
            self.tail = None

        def append(self, value):
            new_node = Node(value)
            if self.head.next is None:
                self.head.next = new_node
                self.tail = new_node
                return

            current_node = self.head.next

            while True:
                if current_node.next is None:
                    new_node = new_node
                    current_node.next = new_node
                    self.tail = new_node
                    break
                else:
                    current_node = current_node.next

        def prepend(self, value):
            new_node = Node(value)
            if self.tail is None:
                self.tail = self.head
            new_node.next = self.head
            self.head = new_node

        def insert_node(self, value, index):
            new_node = Node(value)
            current_node = self.head

            if range == 0:
                new_node.next = current_node
                self.head = new_node
                if current_node.next is None:
                    self.tail = current_node


            for i in range(0, index):
                if current_node.next is not None:
                    previous_node = current_node
                    current_node = current_node.next
                else:
                    print("Index out of bounds. Adding to end of Linked List.")
                    current_node.next = new_node
                    self.tail = new_node

            new_node.next = previous_node.next
            previous_node.next = new_node
            if current_node.next is None:
                self.tail = current_node

        def delete_node(self, index):
            current_node = self.head
            if index == 0:
                self.head = current_node.next
                return

            for i in range(index):
                if current_node.next is not None:
                    previous_node = current_node
                    current_node = current_node.next
                else:
                    print("Index out of bounds.")

            if current_node.next is not None:
                previous_node.next = current_node.next
            else:
                previous_node.next = None

        def reverse(self):
            if self.head == self.tail:
                return self
            else:
                first = self.head
                self.tail = first
                second = self.head.next
                while second is not None:
                    temp = second.next
                    second.next = first
                    first = second
                    second = temp
                self.head.next = None
                self.head = first


        # Probably don't need this
        # def assign_tail(self):
        #     current_node = self.next
        #     while current_node.next is not None:
        #         current_node = current_node.next
        #     self.tail = current_node

        def print_list(self):
            current_node = self.head
            while current_node.next is not None:
                print(current_node.data)
                current_node = current_node.next
            print(current_node.data)

    my_linked_list = LinkedList(10)
    my_linked_list.append(5)            # O(n)
    my_linked_list.append(6)
    my_linked_list.prepend(19)          # O(1)
    my_linked_list.insert_node(7, 1)    # O(n)
    my_linked_list.insert_node(60, 4)
    my_linked_list.delete_node(0)       # O(n)
    my_linked_list.print_list()
    my_linked_list.reverse()
    my_linked_list.print_list()


def example2():

    class DoubleLinkedListNode:

        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None

    class DoubleLinkedList:

        def __init__(self, value):
            self.head = DoubleLinkedListNode(value)
            self.tail = None

        def append(self, value):
            new_node = DoubleLinkedListNode(value)
            if self.head.next is None:
                new_node.previous = self.head
                self.head.next = new_node
                self.tail = new_node
                return

            current_node = self.head.next

            while True:
                if current_node.next is None:
                    new_node = new_node
                    new_node.previous = current_node
                    current_node.next = new_node
                    self.tail = new_node
                    break
                else:
                    current_node = current_node.next

        def prepend(self, value):
            new_node = DoubleLinkedListNode(value)
            if self.tail is None:
                self.tail = self.head
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

        def insert_node(self, value, index):
            new_node = DoubleLinkedListNode(value)
            current_node = self.head

            if range == 0:
                new_node.next = current_node
                current_node.previous = new_node
                self.head = new_node
                if current_node.next is None:
                    self.tail = current_node
                return

            for i in range(0, index):
                if current_node.next is not None:
                    previous_node = current_node
                    current_node = current_node.next
                else:
                    print("Index out of bounds. Adding to end of Linked List.")
                    current_node.next = new_node
                    new_node.previous = current_node
                    self.tail = new_node

            new_node.next = previous_node.next
            new_node.next.previous = new_node
            previous_node.next = new_node
            if current_node.next is None:
                current_node.previous = new_node
                self.tail = current_node

        def delete_node(self, index):
            current_node = self.head
            if index == 0:
                if current_node.next is not None:
                    current_node.next.previous = None
                    self.head = current_node.next
                    return
                else:
                    self.head = None
                    return

            for i in range(index):
                if current_node.next is not None:
                    previous_node = current_node
                    current_node = current_node.next
                else:
                    print("Index out of bounds.")

            if current_node.next is not None:
                current_node.next.previous = previous_node
                previous_node.next = current_node.next
            else:
                previous_node.next = None

        # Probably don't need this
        # def assign_tail(self):
        #     current_node = self.next
        #     while current_node.next is not None:
        #         current_node = current_node.next
        #     self.tail = current_node

        def print_list(self):
            current_node = self.head
            while current_node.next is not None:
                print(current_node.data)
                current_node = current_node.next
            print(current_node.data)

    my_linked_list = DoubleLinkedList(10)
    my_linked_list.append(5)            # O(n)
    my_linked_list.append(6)
    my_linked_list.prepend(19)          # O(1)
    my_linked_list.insert_node(7, 1)    # O(n)
    my_linked_list.insert_node(60, 4)
    my_linked_list.delete_node(0)       # O(n)
    my_linked_list.print_list()


example1()
