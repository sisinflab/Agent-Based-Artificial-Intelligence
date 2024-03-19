import math
import numpy as np

streets = {
    'Andria': ['Corato', 'Trani'],
    'Corato': ['Ruvo', 'Trani', 'Andria', 'Altamura'],
    'Altamura': ['Corato', 'Ruvo', 'Modugno'],
    'Ruvo': ['Corato', 'Bisceglie', 'Terlizzi', 'Altamura'],
    'Terlizzi': ['Ruvo', 'Molfetta', 'Bitonto'],
    'Bisceglie': ['Trani', 'Ruvo', 'Molfetta'],
    'Trani': ['Andria', 'Corato', 'Bisceglie'],
    'Molfetta': ['Bisceglie', 'Giovinazzo', 'Terlizzi'],
    'Giovinazzo': ['Molfetta', 'Modugno', 'Bari', 'Bitonto'],
    'Bitonto': [ 'Modugno', 'Giovinazzo', 'Terlizzi'],
    'Modugno': ['Bitonto', 'Giovinazzo', 'Bari', 'Altamura'],
    'Bari': ['Modugno', 'Giovinazzo']
}

# cities coordinates
streets_coords = {
    'Andria': (41.2316, 16.2917),
    'Corato': (41.1465, 16.4147),
    'Altamura': (40.8302, 16.5545),
    'Ruvo': (41.1146, 16.4886),
    'Terlizzi': (41.1321, 16.5461),
    'Bisceglie': (41.243, 16.5052),
    'Trani': (41.2737, 16.4162),
    'Molfetta': (41.2012, 16.5983),
    'Giovinazzo': (41.1874, 16.6682),
    'Bitonto': (41.1118, 16.6902),
    'Modugno': (41.0984, 16.7788),
    'Bari': (41.1187, 16.852)
}


class Roads:
    def __init__(self, streets, coordinates):
        self.streets = streets
        self.coordinates = coordinates

    def distance(self, start, end):
        lat_a, long_a = self.coordinates[start]
        lat_b, long_b = self.coordinates[end]
        lat_diff = abs(lat_a - lat_b)*111  # <- *111 to just convert the latitude distance in KM.
        long_diff = abs(long_a - long_b)*111 # <- *111 to just convert the longitude distance in KM.
        return math.sqrt(lat_diff**2 + long_diff**2)


class Maze:
    def __init__(self, M, N, K, V):
        self.width = N
        self.height = M
        self.n_walls = K
        self.p_walls = V

    def create_environment(self):
        maze = np.ones((self.height, self.width), dtype=int)  # <- 1: reachable element
        for i in range(self.n_walls):
            maze[self.p_walls[i][0]][self.p_walls[i][1]] = 2  # <- 2: unreachable element

        return maze
