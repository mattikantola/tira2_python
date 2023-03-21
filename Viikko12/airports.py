class Airports:
    def __init__(self,n):
        
        self.size = n+1
        self.access = [[1 for iii in range(n+1)] for jjj in range(n+1)]

    def add_link(self,a,b):
        
        self.access[a][a] = 0
        self.access[b][b] = 0
        self.access[a][b] = 0

    def check(self):
        
        for vali in range(1, self.size):

            for alku in range(1, self.size):

                for loppu in range(1, self.size):

                    if self.access[alku][loppu] == 0:

                        continue

                    elif self.access[alku][vali] == 0 and self.access[vali][loppu] == 0:

                        self.access[alku][loppu] = 0

        for rivi in self.access[1:]:

            for corrected in rivi[1:]:

                if corrected == 1:

                    return False
                
        return True

if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1,2)
    a.add_link(2,3)
    a.add_link(1,3)
    a.add_link(4,5)
    print(a.check()) # False
    a.add_link(3,5)
    a.add_link(1,4)
    print(a.check()) # False
    a.add_link(5,1)
    print(a.check()) # True