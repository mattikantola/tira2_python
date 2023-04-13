from math import inf
from collections import deque
from copy import deepcopy

class Planets:
    def __init__(self,n):
        
        self.size = n+1
        self.adjacency = [[-1 for jjj in range(self.size)] for iii in range(self.size)]
        self.visited = [False for iii in range(self.size)]
        self.backup = []

    def add_teleport(self, a, b):

        if self.adjacency[a][b] == -1:
            self.adjacency[a][b] = 0
        self.adjacency[a][b] += 1
        self.adjacency[b][a] = max(0, self.adjacency[b][a])

    def bfs(self, start, stop, parents):

        self.visited = [False for iii in range(self.size)]
        self.visited[start] = True
        storage = deque()
        storage.append(start)

        while storage:

            new_node = storage.popleft()

            neighbors = self.backup[new_node]

            for index, neighbor in enumerate(neighbors):

                if not self.visited[index] and neighbor > 0:

                    storage.append(index)
                    parents[index] = new_node
                    self.visited[index] = True                    
                    
                    if index == stop:
                        
                        return True
        
        return False
    
    def calculate(self):

        parents = [-1]*self.size
        max_flow = 0
        self.backup = deepcopy(self.adjacency)
        while self.bfs(1, self.size-1, parents):

            path_flow = inf
            node = self.size - 1
            while node != 1:
                parent = parents[node]
                path_flow = min(path_flow, self.backup[parent][node])
                node = parent

            node = self.size - 1
            while node != 1:
                parent = parents[node]
                self.backup[parent][node] -= path_flow
                self.backup[node][parent] += path_flow
                node = parent

            max_flow += path_flow

        return max_flow
    
if __name__ == "__main__":
    p = Planets(5)
    print(p.calculate()) # 0
    p.add_teleport(1,2)
    p.add_teleport(2,5)
    print(p.calculate()) # 1
    p.add_teleport(1,5)
    print(p.calculate()) # 2