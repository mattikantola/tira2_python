from heapq import heappush, heappop, heapify

class BestRoute:

    def __init__(self, n):
        
        self.length = n + 1
        self.__adjacency_list = [[] for iii in range(n+1)]

    def add_road(self, a, b, x):

        new_route = tuple((x, b))
        self.__adjacency_list[a].append(new_route)
        new_route = tuple((x, a))
        self.__adjacency_list[b].append(new_route)

    def find_route(self, a, b):

        visited = [False for iii in range(self.length)]
        distances = [None for iii in range(self.length)]
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

                else:

                    if new_dist < cur_dist:

                        distances[destination] = new_dist
                        heappush(storage, tuple((new_dist, destination)))


        if distances[b] is not None:

            return distances[b]

        else:

            return -1


if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1,2,2)
    print(b.find_route(1,3)) # -1
    b.add_road(1,3,5)
    print(b.find_route(1,3)) # 5
    b.add_road(2,3,1)
    print(b.find_route(1,3)) # 3