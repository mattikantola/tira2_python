class LongPath:
    def __init__(self,n):
        
        self.size = n + 1
        self.adjacency = [[] for iii in range(self.size)]


    def add_edge(self,a,b):
        
        self.adjacency[a].append(b)
        self.adjacency[b].append(a)

    def calculate(self):
        
        cache = {iii:0 for iii in range(self.size)}
        max_path = 0

if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1,2)
    l.add_edge(1,3)
    l.add_edge(2,4)
    l.add_edge(3,4)
    print(l.calculate()) # 2
    l.add_edge(3,2)
    print(l.calculate()) # 3