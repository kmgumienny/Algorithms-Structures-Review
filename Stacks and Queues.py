def example1():

    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None

    class Stack:

        def __init__(self):
            self.top = None
            self.bottom = None
            self.length = 0

        def peek(self):
            if self.top is not None:
                print(self.top.value)

        def push(self, value):
            new_node = Node(value)
            if self.top is None:
                self.top = new_node
                self.bottom = new_node
            else:
                new_node.next = self.top
                self.top = new_node
            self.length += 1

        def pop(self):
            if self.top is not None:
                self.top = self.top.next
                self.length -= 1
            else:
                print("Stack is empty")


    my_stack = Stack()
    my_stack.push("Discord")
    my_stack.peek()
    my_stack.push("Udemy")
    my_stack.peek()
    my_stack.push("Google")
    my_stack.peek()
    my_stack.pop()
    my_stack.peek()
    my_stack.pop()
    my_stack.peek()
    my_stack.pop()


# example1()


def example2():

    class Node:

        def __init__(self, value):
            self.value = value

    class Stack:

        def __init__(self):
            self.array = []

        def peek(self):
            length = len(self.array)
            if length > 0:
                print(self.array[length - 1].value)

        def push(self, value):
            new_node = Node(value)
            self.array.append(new_node)

        def pop(self):
            length = len(self.array)
            if length > 0:
                self.array.remove(self.array[length - 1])
            else:
                print("Stack is empty")


    my_stack = Stack()
    my_stack.push("Discord")
    my_stack.peek()
    my_stack.push("Udemy")
    my_stack.peek()
    my_stack.push("Google")
    my_stack.peek()
    my_stack.pop()
    my_stack.peek()
    my_stack.pop()
    my_stack.peek()
    my_stack.pop()


# example2()


def example3():

    class Node:

        def __init__(self, value):
            self.value = value
            self.next = None

    class Queue:

        def __init__(self):
            self.first = None
            self.last = None
            self.length = 0

        def peek(self):
            current_node = self.first
            while current_node is not None:
                print(current_node.value, end=' ')
                current_node = current_node.next
            print("\n")

        def enqueue(self, value):
            new_node = Node(value)
            if self.first is None:
                self.first = new_node
                self.last = new_node
            else:
                self.last.next = new_node
                self.last = new_node
            self.length += 1

        def dequeue(self):
            if self.first is not None:
                self.first = self.first.next
                self.length -= 1
            else:
                print("Queue is empty")

    my_queue = Queue()
    my_queue.enqueue("Joy")
    my_queue.peek()
    my_queue.enqueue("Matt")
    my_queue.peek()
    my_queue.enqueue("Pavel")
    my_queue.peek()
    my_queue.enqueue("Samir")
    my_queue.peek()
    my_queue.dequeue()
    my_queue.peek()
    my_queue.dequeue()
    my_queue.peek()
    my_queue.dequeue()
    my_queue.peek()
    my_queue.dequeue()


example3()
