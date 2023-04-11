class Download:
    def __init__(self,n):
        
        self.size = n+1
        self.adjacency = [[-1 for jjj in range(self.size)] for iii in range(self.size)]

    def add_link(self, a, b, x):

        self.adjacency[a][b] = x
        self.adjacency[b][a] = 0

if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1,4)) # 0
    d.add_link(1,2,5)
    d.add_link(2,4,6)
    d.add_link(1,4,2)
    print(d.calculate(1,4)) # 7
    d.add_link(1,3,4)
    d.add_link(3,2,2)
    print(d.calculate(1,4)) # 8