from collections import deque

class Network:

    def __init__(self, n):

        self.__n = n
        self.__adjlist = [[] for iii in range(n+1)]

    def add_link(self, a, b):

        self.__adjlist[a].append(b)
        self.__adjlist[b].append(a)


    def best_route(self, a, b):

        working = deque()
        working.append(a)

        visited = [False for iii in range(self.__n + 1)]
        distance = [0 for iii in range(self.__n + 1)]
        visited[a] = True

        while len(working) > 0:

            node = working.popleft()

            for neighbor in self.__adjlist[node]:

                if visited[neighbor]:
                    
                    continue

                working.append(neighbor)
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1

        if distance[b] == 0:

            return -1

        else:

            return distance[b]



if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2