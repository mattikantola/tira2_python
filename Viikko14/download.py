from math import inf
from collections import deque
from copy import deepcopy

class Download:
    def __init__(self,n):
        
        self.size = n+1
        self.adjacency = [[-1 for jjj in range(self.size)] for iii in range(self.size)]
        self.visited = [False for iii in range(self.size)]
        self.backup = []

    def add_link(self, a, b, x):

        if self.adjacency[a][b] == -1:
            self.adjacency[a][b] = 0
        self.adjacency[a][b] += x
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
    
    def calculate(self, start, stop):

        parents = [-1]*self.size
        max_flow = 0
        self.backup = deepcopy(self.adjacency)
        while self.bfs(start, stop, parents):

            path_flow = inf
            node = stop
            while node != start:
                parent = parents[node]
                path_flow = min(path_flow, self.backup[parent][node])
                node = parent

            node = stop
            while node != start:
                parent = parents[node]
                self.backup[parent][node] -= path_flow
                self.backup[node][parent] += path_flow
                node = parent

            max_flow += path_flow

        return max_flow

if __name__ == "__main__":
    d = Download(5)
    print(d.calculate(3,4))
    d.add_link(5,3,6)
    print(d.calculate(5,4))
    print(d.calculate(4,5))
    print(d.calculate(5,1))
    d.add_link(5,4,9)
    d.add_link(1,2,10)
    print(d.calculate(3,1))
    print(d.calculate(2,4))
    print(d.calculate(5,4))
    d.add_link(5,2,9)
    print(d.calculate(1,5))
    d.add_link(3,5,2)
    d.add_link(1,3,2)
    d.add_link(5,4,9)
    print(d.calculate(5,4))
    print(d.calculate(2,3))
    print(d.calculate(1,3))
    print(d.calculate(3,2))
    print(d.calculate(5,4))
    print(d.calculate(4,5))
    d.add_link(4,3,9)
    print(d.calculate(4,5))
    print(d.calculate(2,4))
    print(d.calculate(4,5))
    d.add_link(5,1,6)
    d.add_link(3,5,3)
    d.add_link(4,5,2)
    print(d.calculate(3,4))
    d.add_link(5,3,3)