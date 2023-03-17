from heapq import heappush, heappop
from math import inf

def calculate(t):

    def make_connections(t):

        adjacency_list = [[] for iii in range(len(t))]

        for iii in range(len(t)):

            if iii - t[iii] >= 0:

                route = tuple((t[iii], iii-t[iii]))
                adjacency_list[iii].append(route)

            if t[iii] + iii < len(t):

                route = tuple((t[iii], t[iii]+iii))
                adjacency_list[iii].append(route)

        return adjacency_list

    
    adjlist = make_connections(t)

    distances = [inf for iii in range(len(t))]

    visited = [False for iii in range(len(t))]

    storage = []

    distances[0] = 0

    heappush(storage, tuple((0, 0)))

    while True:

        try:

            elem = heappop(storage)

        except IndexError:

            break

        node = elem[1]

        if visited[node]:
            continue
        visited[node] = True

        for arch in adjlist[node]:

            dist, destination = arch[0], arch[1]

            cur_dist = distances[destination]

            new_dist = distances[node] + dist

            if new_dist < cur_dist:

                distances[destination] = new_dist

                heappush(storage, tuple((new_dist, destination)))


    if distances[-1] == inf:

        return -1

    else:

        return distances[-1]


if __name__ == "__main__":
    print(calculate([1,1,1,1])) # 3
    print(calculate([3,2,1])) # -1
    print(calculate([3,5,2,2,2,3,5])) # 10
    print(calculate([7,5,3,1,4,2,4,6,1])) # 32