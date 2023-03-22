class Components:
    def __init__(self,n):
        
        self.size = n+1
        self.adjacency = [[] for iii in range(self.size)]

    def add_road(self,a,b):
        
        self.adjacency[a].append(b)
        self.adjacency[b].append(a)

    def count(self):
        
        visited = [False for iii in range(self.size)]

        def traverse(node):

            if visited[node]:
                return
            else:
                visited[node] = True
                for neighbor in self.adjacency[node]:
                    traverse(neighbor)

        component_count = 0

        for iii in range(1, self.size):

            if visited[iii]:
                continue
            traverse(iii)
            component_count += 1

        return component_count

if __name__ == "__main__":
    c = Components(5)
    print(c.count()) # 5
    c.add_road(1,2)
    c.add_road(1,3)
    print(c.count()) # 3
    c.add_road(2,3)
    print(c.count()) # 3
    c.add_road(4,5)
    print(c.count()) # 2