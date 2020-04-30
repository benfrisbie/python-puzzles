import unittest

class Graph:
    def __init__(self):
        self.graph = dict()

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = set()
    
    def add_edge(self, n0, n1):
        self.add_node(n0)
        self.add_node(n1)

        self.graph[n0].add(n1)
        self.graph[n1].add(n0)
    
    def depth_first_traversal(self, node, visited):
        visited[node] = True

        for adjacent in self.graph[node]:
            if visited[adjacent] == False:
                self.depth_first_traversal(adjacent, visited)

    def count_sections(self):
        count = 0

        visited = dict()
        for node in self.graph:
            visited[node] = False

        for node in self.graph:
            if visited[node] == False:
                self.depth_first_traversal(node, visited)
                count += 1
            if all(visited.values()):
                break

        return count


def island_counter(grid):
    rows = len(grid)
    cols = len(grid[0])

    g = Graph()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                g.add_node((i,j))
                # up
                if i > 0 and grid[i-1][j] == 1:
                    g.add_edge((i,j), (i-1, j))
                # down
                if i < rows-1 and grid[i+1][j] == 1:
                    g.add_edge((i,j), (i+1, j))
                # left
                if j > 0 and grid[i][j-1] == 1:
                    g.add_edge((i,j), (i, j-1))
                # right
                if j < cols-1 and grid[i][j+1] == 1:
                    g.add_edge((i,j), (i, j+1))
    
    return g.count_sections()


class Tests(unittest.TestCase):
    def test1(self):
        grid = [
            [1,1,1,1,0],
            [1,1,0,1,0],
            [1,1,0,0,0],
            [0,0,0,0,0]
        ]
        self.assertEqual(island_counter(grid), 1)

    def test2(self):
        grid = [
            [1,1,0,0,0],
            [1,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]
        ]
        self.assertEqual(island_counter(grid), 3)

    def test3(self):
        grid = [
            [1, 1, 0, 0, 0], 
            [0, 1, 0, 0, 1], 
            [1, 0, 0, 1, 1], 
            [0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 1]
        ]
        self.assertEqual(island_counter(grid), 6)

if __name__ == '__main__':
    unittest.main()