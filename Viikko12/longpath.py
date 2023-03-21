class LongPath:
    def __init__(self,n):
        
        self.size = n + 1
        self.adjacency = [[] for iii in range(self.size)]

    def add_edge(self,a,b):
        
        a, b = min(a, b), max(a, b)
        self.adjacency[a].append(b)

    def calculate(self):

        cache = dict()
        
        def longest_path(node):

            if node in cache:
                return cache[node]
            if len(self.adjacency[node]) == 0: #ei mitään minne mennä
                cache[node] = 0
                return 0
            cache[node] = 1 + max([longest_path(neighbor) for neighbor in self.adjacency[node]])
            return cache[node]

        max_path = 0

        for node in range(1,self.size):
             max_path = max(max_path, longest_path(node))

        return max_path       

if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1,2)
    l.add_edge(1,3)
    l.add_edge(2,4)
    l.add_edge(3,4)
    print(l.calculate()) # 2
    l.add_edge(3,2)
    print(l.calculate()) # 3