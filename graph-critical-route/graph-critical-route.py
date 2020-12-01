import copy
import unittest

class Graph:
    def __init__(self, num_nodes, num_edges, edges):
        self.graph = dict()
        for i in range(num_nodes):
            self.graph[i] = []
        
        for i in range(num_edges):
            n0, n1 = edges[i]
            self.graph[n0].append(n1)
            self.graph[n1].append(n0)
        print(self.graph)

    def remove_node(self, node):
        for connected_node in self.graph[node]:
            self.graph[connected_node].remove(node)
        self.graph.pop(node)

    def depth_first_traversal(self, node, nodes_visited):
        nodes_visited[node] = True
        for connected_node in self.graph[node]:
            if nodes_visited[connected_node] == False:
                self.depth_first_traversal(connected_node, nodes_visited)

    def breadth_first_traversal(self, node, nodes_visited):
        queue = []
        queue.append(node)
        nodes_visited[node] = True

        while queue:
            n = queue.pop(0)
            for connected_node in self.graph[n]:
                if nodes_visited[connected_node] == False: 
                    queue.append(connected_node)
                    nodes_visited[connected_node] = True


    def is_connected(self):
        nodes_visited = {}
        for n in self.graph.keys():
            nodes_visited[n] = False

        # self.depth_first_traversal(list(self.graph.keys())[0], nodes_visited)
        self.breadth_first_traversal(list(self.graph.keys())[0], nodes_visited)

        if all(nodes_visited.values()):
            return True
        return False

    def is_node_critical(self, node):
        graph_copy = copy.deepcopy(self)
        graph_copy.remove_node(node)
        print(graph_copy.graph)
        if not graph_copy.is_connected():
            return True
        return False



def graph_critical_route(num_nodes, num_edges, edges):
    graph = Graph(num_nodes, num_edges, edges)
    
    critical_nodes = []
    for i in range(num_nodes):
        if graph.is_node_critical(i):
            critical_nodes.append(i)

    return critical_nodes




class Tests(unittest.TestCase):
    def test1(self):
        num_nodes = 7
        num_edges = 7
        edges = [[0, 1], [0, 2], [1, 3], [2, 3], [2, 5], [5, 6], [3, 4]]
        res = graph_critical_route(num_nodes, num_edges, edges)
        self.assertEqual(res, [2,3,5])


if __name__ == '__main__':
    unittest.main()