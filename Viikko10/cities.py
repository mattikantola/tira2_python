class Cities:

    def __init__(self, n):

        self.__n = n
        self.__adjlist = [[] for iii in range(n+1)]

    def add_road(self, a, b):

        self.__adjlist[a].append(b)
        self.__adjlist[b].append(a)


    def has_route(self, a, b):

        been_there = [False for iii in range(self.__n+1)]

        def traverse(node):

            been_there[node] = True

            for neighbor in self.__adjlist[node]:

                if not been_there[neighbor]:

                    traverse(neighbor)


        traverse(a)

        return been_there[b]

if __name__ == "__main__":
    c = Cities(5)
    c.add_road(1,2)
    c.add_road(1,3)
    c.add_road(4,5)
    print(c.has_route(1,5)) # False
    c.add_road(3,4)
    print(c.has_route(1,5)) # True
