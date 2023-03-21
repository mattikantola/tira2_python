class GraphGame:
    def __init__(self,n):
        self.size = n+1
        self.adjacency = [[] for iii in range(self.size)]

    def add_link(self,a,b):
        
        self.adjacency[a].append(b)

    def winning(self,x):
        
        cache = dict()

        def winner(node):

            if node in cache:
                return cache[node]
            if len(self.adjacency[node]) == 0:
                cache[node] = 0
                return 0
            else:
                for neighbor in self.adjacency[node]:
                    if winner(neighbor) == 0:
                        cache[node] = 1
                        return 1
                cache[node] = 0
                return 0

        return winner(x)


if __name__ == "__main__":
    g = GraphGame(6)
    g.add_link(3,4)
    g.add_link(1,4)
    g.add_link(4,5)
    print(g.winning(3)) # False
    print(g.winning(1)) # False
    g.add_link(3,1)
    g.add_link(4,6)
    g.add_link(6,5)
    print(g.winning(3)) # True
    print(g.winning(1)) # False
    print(g.winning(2)) # False