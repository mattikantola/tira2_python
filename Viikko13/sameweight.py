'''
Painotettuun verkkoon voi lisätä kaaria ja tarkoitus on tutkia, onko verkon kaikilla virittävillä puilla sama
paino. Tämä tehdään union-find-rakenteella. Koska on tehotonta etsiä kaikki virittävät puut, etsitään suurin
ja pienin, joiden painoja verrataan keskenään. Jos nämä ovat samat, ovat kaikki virittävät puut samanpainoisia.
'''

class SameWeight:
    def __init__(self,n):
        
        self.size = n + 1
        self.parents = [iii for iii in range(self.size)]
        self.components = [1 for iii in range(self.size)]
        self.max_size = 0
        self.edges = []

    def add_edge(self,a,b,x):
        
        self.edges.append(tuple([a,b,x]))

    def check(self):
        
        def edustaja(x):

            while x != self.parents[x]:
                x = self.parents[x]
            return x
        
        def samat(a,b):

            return edustaja(a) == edustaja(b)
        
        def merge(a,b):

            a, b = edustaja(a), edustaja(b)

            if a == b:
                return
            if self.components[a] < self.components[b]:
                a, b = b, a
            self.parents[b] = a
            self.components[a] += self.components[b]
            self.max_size = max(self.max_size, self.components[a])

        def min_length():

            arches = sorted(self.edges, key=lambda x: x[2])
            minimum = 0

            for arch in arches:

                start, stop, weight = arch
                if samat(start, stop):
                    continue
                else:
                    merge(start, stop)
                    minimum += weight

            self.parents = [iii for iii in range(self.size)]
            self.components = [1 for iii in range(self.size)]

            if self.max_size == self.size-1:
                return minimum
            else:
                return -1

        def max_length():

            arches = sorted(self.edges, key=lambda x: x[2], reverse=True) #poikkeaa minimistä siten, että aloitetaan
                                                                            #painavimmista kaarista, jolloin löydetään
                                                                            #niin painava virittävä puu kuin mahdollista.
            maximum = 0

            for arch in arches:

                start, stop, weight = arch
                if samat(start, stop):
                    continue
                else:
                    merge(start, stop)
                    maximum += weight

            self.parents = [iii for iii in range(self.size)]
            self.components = [1 for iii in range(self.size)]

            if self.max_size == self.size-1:
                return maximum
            else:
                return -1

        maximum = max_length()
        if maximum == -1:
            return True
        minimum = min_length()
        if minimum == -1:
            return True
        return minimum == maximum

if __name__ == "__main__":
    s = SameWeight(4)
    s.add_edge(1,2,2)
    s.add_edge(1,3,3)
    print(s.check()) # True
    s.add_edge(1,4,3)
    print(s.check()) # True
    s.add_edge(3,4,3)
    print(s.check()) # True
    s.add_edge(2,4,1)
    print(s.check()) # False