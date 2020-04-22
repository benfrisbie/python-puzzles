import unittest

def zombie_matrix(grid):
    row_count = len(grid)
    col_count = len(grid[0])

    zombies = []
    for i in range(row_count):
        for j in range(col_count):
            if grid[i][j] == 1:
                zombies.append((i,j))

    hours = 0
    while(True):
        new_zombies = []
        for i, j in zombies:
            if i != 0 and grid[i-1][j] == 0:
                grid[i-1][j] = 1
                new_zombies.append((i-1, j))
            if i != row_count - 1 and grid[i+1][j] == 0:
                grid[i+1][j] = 1
                new_zombies.append((i+1, j))
            if j != 0 and grid[i][j-1] == 0:
                grid[i][j-1] = 1
                new_zombies.append((i, j-1))
            if j != col_count - 1 and grid[i][j+1] == 0:
                grid[i][j+1] = 1
                new_zombies.append((i, j+1))
        zombies = new_zombies

        if not zombies:
            return hours

        hours += 1

class Tests(unittest.TestCase):
    def test1(self):
        matrix = [
            [0, 1, 1, 0, 1],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0]
        ]
        res = zombie_matrix(matrix)
        self.assertEqual(res, 2)

    def test2(self):
        matrix = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1]
        ]
        res = zombie_matrix(matrix)
        self.assertEqual(res, 8)

    def test3(self):
        matrix = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        res = zombie_matrix(matrix)
        self.assertEqual(res, 4)

if __name__ == '__main__':
    unittest.main()