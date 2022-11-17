import random
from heapq import heappop, heappush
import time

class Graph:


    def __init__(self, size=5000):

        self.size = size+1
        self.__adjacency_list = [[] for iii in range(self.size)]

    def add_egde(self, a, b):

        route = tuple((random.randint(1, 1000), b))
        self.__adjacency_list[a].append(route)

    def make_edges(self):

        for iii in range(1, self.size):

            for jjj in range(1, self.size):

                if iii < jjj and jjj - iii < 10:

                    self.add_egde(iii, jjj)


        for neighbors in self.__adjacency_list:

            random.shuffle(neighbors)

    def best_route(self, a, b):

        visited = [False for iii in range(self.size)]
        distances = [None for iii in range(self.size)]
        distances[a] = 0

        storage = []
        heappush(storage, tuple((0, a)))

        while True:

            try:

                elem = heappop(storage)

            except IndexError:

                break

            node = elem[1]
            if visited[node]:
                continue
            visited[node] = True

            for arch in self.__adjacency_list[node]:

                dist, destination = arch[0], arch[1]

                cur_dist = distances[destination]
                new_dist = distances[node] + dist

                if cur_dist is None:

                    distances[destination] = new_dist
                    heappush(storage, tuple((new_dist, destination)))

                elif new_dist < cur_dist:

                    distances[destination] = new_dist
                    heappush(storage, tuple((new_dist, destination)))

        if distances[b] is not None:

            return distances[b]

        else:

            return -1

if __name__ == "__main__":

    c = Graph()
    c.make_edges()
    start = time.time()
    print(c.best_route(1, 1337))
    stop = time.time()
    elapsed = stop-start
    print(elapsed, " s")
