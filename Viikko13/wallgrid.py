class WallGrid:
    def __init__(self,n):
        
        self.size = n + 1
        self.components = [[0 for iii in range(self.size)] for jjj in range(self.size)]
        self.floor = [[False for iii in range(self.size)] for jjj in range(self.size)]
        self.parents = [[(yyy,xxx) for xxx in range(self.size) for yyy in range(self.size)]]

    def remove(self,x,y):
        
        def edustaja(y, x):

            while (y, x) != self.parents[y][x]:

                y, x = self.parents[y][x]

            return y, x
        
        def merge(y1, x1, y2, x2):

            y1, x1, y2, x2 = edustaja(y1, x1), edustaja(y2, x2)

            if (y1, x1) == (y2, x2):

                return
            
            if self.components[y1][x1] < self.components[y2][x2]:
                y1, y2 = y2, y1
                x1, x2 = x2, x1
            self.parents[y2][x2] = self.parents[y1][x1]
            self.components[y1][x1] += self.components[y2][x2]

        if x in (1, self.size-2) or y in (1, self.size-2) or self.floor[y][x]:
            return
        self.floor[y][x] = True
        self.components[y][x] = 1
        for d_y, d_x in ((1,0), (-1,0), (0,1), (0,-1)):
            if self.floor[y+d_y][x+d_x] and y+d_y not in (1, self.size-2) and x+d_x not in (1, self.size-2):
                merge(y+d_y, x+d_x, y, x)

    def count(self):

        print("jee")
        return self.components       

if __name__ == "__main__":
    w = WallGrid(5)
    print(w.count()) # 0
    w.remove(2,2)
    w.remove(4,2)
    print(w.count()) # 2
    w.remove(3,2)
    print(w.count()) # 1
    w.remove(2,4)
    w.remove(2,4)
    w.remove(4,4)
    print(w.count()) # 3
    w.remove(3,3)
    print(w.count()) # 3
    w.remove(3,4)
    print(w.count()) # 1