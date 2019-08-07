# This is an edge list
# 0 Connected to 2, 2 connected to 3, 2 connected to 1...
edge_list = [[0, 2], [2, 3], [2, 1], [1, 3]]

# Adjacent list
# 0 is connected to 2, 1 is connected to 2 and 3, 2 is connect to 0, 1, and 3...
adjacent_list = [[2], [2, 3], [0, 1, 3], [1, 2]]

# Adjacent matrix
# 0 is not connected to 0, 1, and 3.
adjacent_matrix = [
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]


def example1():

    class Graph:
        def __init__(self):
            self.number_of_nodes = 0
            self.adjacent_list = dict()

        def add_vertex(self, node):
            if node in self.adjacent_list.keys():
                print("Node {} already exists".format(node))

            else:
                self.number_of_nodes += 1
                self.adjacent_list[node] = []

        def add_edge(self, node1, node2):
            if node1 not in self.adjacent_list.keys() or node2 not in self.adjacent_list.keys():
                print("One or more of the nodes do not exist")
            else:
                self.adjacent_list[node1].append(node2)
                self.adjacent_list[node2].append(node1)

        def show_connections(self):
            print("Total number of nodes is {}.".format(self.number_of_nodes))
            for node in self.adjacent_list:
                print("{}: {}".format(node, self.adjacent_list[node]))

    my_graph = Graph()
    my_graph.add_vertex('0')
    my_graph.add_vertex('1')
    my_graph.add_vertex('2')
    my_graph.add_vertex('3')
    my_graph.add_vertex('4')
    my_graph.add_vertex('5')
    my_graph.add_vertex('6')
    my_graph.add_edge('3', '1')
    my_graph.add_edge('3', '4')
    my_graph.add_edge('4', '2')
    my_graph.add_edge('4', '5')
    my_graph.add_edge('1', '2')
    my_graph.add_edge('1', '0')
    my_graph.add_edge('0', '2')
    my_graph.add_edge('6', '5')
    my_graph.show_connections()


example1()
