class Cycles:
    def __init__(self,n):

        self.adjacency = [[] for iii in range(n+1)]
        self.size = n
        self.start = None

    def add_edge(self,a,b):
        
        self.adjacency[a].append(b)

    def check(self):

        visited = [0 for iii in range(self.size+1)]

        def traverse(node):

           if visited[node] == 2:
               return
           if visited[node] == 1:
               return True
           else:
                visited[node] = 1
                for neighbor in self.adjacency[node]:
                    if traverse(neighbor):
                        return True
                visited[node] = 2
    
        for node in range(1, self.size+1):

            if visited[node] == 2:
                continue
            else:
                if traverse(node) == True:
                    return True
                
        return False

            

if __name__ == "__main__":
    c = Cycles(5)
    c.add_edge(5,3)
    c.add_edge(5,1)
    c.add_edge(1,4)
    c.add_edge(1,2)
    c.add_edge(1,3)
    print(c.check())
    print(c.check())
    c.add_edge(4,5)
    print(c.check())
    c.add_edge(2,5)