'''
Tehtävänä on union-find -rakenteen avulla selvittää seuraava asia: jos kartalla on kaupunkeja ja ehdotuksia niitä
yhdistäviksi teiksi ja ehdotuksilla on hinnat, niin mikä on pienin kustannus kaikkien kaupunkien yhdistämiseen?
'''


class NewRoads:
    
    def __init__(self,n):
        
        self.n = n + 1
        self.sizes = [1 for iii in range(self.n)]
        self.parents = [iii for iii in range(self.n)]
        self.max_size = 0
        self.minimum = 0
        self.roads = []

    def add_road(self, a, b, x):

        self.roads.append(tuple([a,b,x]))

    def min_cost(self):

        arches = sorted(self.roads, key=lambda x: x[2])
        self.minimum = 0

        ''' 
        Union-find-rakenteella pidetään yllä tietoa kaupunki-tieverkon komponenttirakenteesta ja yhdistellään
        tarvittaessa komponentteja.
        '''

        def edustaja(x):

            while self.parents[x] != x:
                x = self.parents[x]
            return x
        
        def samassa(a,b):

            return edustaja(a) == edustaja(b)
        
        def merge(a,b):

            a, b = edustaja(a), edustaja(b)
            if a == b:
                return
            if self.sizes[a] < self.sizes[b]:
                a,b = b,a
            self.parents[b] = a
            self.sizes[a] += self.sizes[b]
            self.max_size = max(self.max_size, self.sizes[a])
            
        for arch in arches:

            start, stop, weight = arch

            if samassa(start, stop):
                continue
            else:
                merge(start,stop)
                self.minimum += weight

        self.sizes = [1 for iii in range(self.n)]
        self.parents = [iii for iii in range(self.n)]

        if self.max_size == self.n - 1:
            return self.minimum
        else:
            return -1

if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1,2,2)
    n.add_road(1,3,5)
    print(n.min_cost()) # -1
    n.add_road(3,4,4)
    print(n.min_cost()) # 11
    n.add_road(2,3,1)
    print(n.min_cost()) # 7