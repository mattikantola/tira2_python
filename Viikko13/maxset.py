class MaxSet:
    def __init__(self,n):
    
        self.n = n + 1  
        self.sizes = [1 for iii in range(self.n)]
        self.parents = [iii for iii in range(self.n)]
        self.max_size = 1

    def merge(self,a,b):
        
        def edustaja(x):

            while x != self.parents[x]:
                x = self.parents[x]
            return x
        
        a = edustaja(a)
        b = edustaja(b)
        if a == b:
             return
        if self.sizes[a] < self.sizes[b]:
            a,b = b,a
        self.parents[b] = a
        self.sizes[a] += self.sizes[b]
        self.max_size = max(self.sizes[a], self.max_size)

    def get_max(self):
        
        return self.max_size

if __name__ == "__main__":
        m = MaxSet(5)
        m.merge(4,5)
        m.merge(2,3)
        print(m.get_max())
        print(m.get_max())
        m.merge(4,5)
        m.merge(3,4)
        m.merge(2,5)
        m.merge(4,5)
        print(m.get_max())
        m.merge(3,4)