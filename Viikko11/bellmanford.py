import random
import time
from math import inf

class Graph:

    def __init__(self, size=5000):

        self.size = size+1
        self.__edgelist = []

    def add_edge(self, start, end, weight):

        new_edge = tuple((start, end, weight))
        self.__edgelist.append(new_edge)

    def make_edges(self):

        for iii in range(1, self.size):

            for jjj in range(1, self.size):

                if iii < jjj and jjj-iii < 10:

                    weight = random.randint(1,1000)
                    self.add_edge(iii, jjj, weight)


        random.shuffle(self.__edgelist)

    def best_route(self, a, b):

        distances = [inf for iii in range(self.size)]
        distances[a] = 0

        while True:

            change = False

            for edge in self.__edgelist:

                start, end, weight = edge

                cur = distances[end]
                new = distances[start] + weight

                if new < cur:

                    distances[end] = new
                    change = True
            
            if not change:
                break

        if distances[b] == inf:
            return -1
        else:
            return distances[b]


if __name__ == "__main__":

    c = Graph()
    c.make_edges()
    start = time.time()
    print(c.best_route(1, 1337))
    stop = time.time()
    elapsed = stop-start
    print(elapsed, ' s')