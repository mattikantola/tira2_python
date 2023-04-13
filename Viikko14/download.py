from math import inf
from collections import deque
from copy import deepcopy

class Download:
    def __init__(self,n):
        
        self.size = n+1
        self.adjacency = [[-1 for jjj in range(self.size)] for iii in range(self.size)]
        self.visited = [False for iii in range(self.size)]
        self.backup = []

    def add_link(self, a, b, x):

        if self.adjacency[a][b] == -1:
            self.adjacency[a][b] = 0
        self.adjacency[a][b] += x
        self.adjacency[b][a] = max(0, self.adjacency[b][a])


    def bfs(self, start, stop, parents):

        '''
        Polut etsitään leveyshaulla, jossa lisäksi pidetään kirjaa siitä, mikä on polun edellinen
        solmu. Tätä tietoa käytetään hyväksi, kun muodostetaan täydennyspolkuja ja peruutetaan
        polkua taaksepäin.
        '''

        self.visited = [False for iii in range(self.size)]
        self.visited[start] = True
        storage = deque()
        storage.append(start)

        while storage:

            new_node = storage.popleft()

            neighbors = self.backup[new_node]

            for index, neighbor in enumerate(neighbors):

                if not self.visited[index] and neighbor > 0:

                    storage.append(index)
                    parents[index] = new_node
                    self.visited[index] = True                    
                    
                    if index == stop:
                        
                        #on päästy kohdesolmuun
                        return True
        
        return False #ei olla päästy kohdesolmuun
    
    def calculate(self, start, stop):

        parents = [-1]*self.size
        max_flow = 0
        self.backup = deepcopy(self.adjacency) #työverkko täydennyspolkujen muodostusta varten
        while self.bfs(start, stop, parents): #aina kun leveyshaku löytää polun lähteen ja
                                            #kohteen välille, voidaan algoritmia jatkaa ja
                                            #päivittää työverkkoa.

            path_flow = inf
            node = stop
            while node != start:
                parent = parents[node] 
                path_flow = min(path_flow, self.backup[parent][node]) #polun virtaus on joko se itse
                                                                        #tai juuri tässä käsitellyn
                                                                        #kaaren paino, pienempi
                                                                        #määrää (pullonkaula-ajatus)
                node = parent

            node = stop
            while node != start: #peruutetaan ja vähennetään alkuperäisistä kaarista saatu minimipaino
                                #samalla, kun käänteisiin kaariin lisätään kyseinen minimipaino.
                                #ideana on muodostaa täydennyspolut, joita pitkin voidaan kulkea
                                #algoritmin seuraavassa vaiheessa.
                parent = parents[node]
                self.backup[parent][node] -= path_flow 
                self.backup[node][parent] += path_flow
                node = parent

            max_flow += path_flow #tältä polulta on löydetty virtaus, joka kasvattaa maksimivirtausta

        return max_flow

if __name__ == "__main__":
    d = Download(5)
    print(d.calculate(3,4))
    d.add_link(5,3,6)
    print(d.calculate(5,4))
    print(d.calculate(4,5))
    print(d.calculate(5,1))
    d.add_link(5,4,9)
    d.add_link(1,2,10)
    print(d.calculate(3,1))
    print(d.calculate(2,4))
    print(d.calculate(5,4))
    d.add_link(5,2,9)
    print(d.calculate(1,5))
    d.add_link(3,5,2)
    d.add_link(1,3,2)
    d.add_link(5,4,9)
    print(d.calculate(5,4))
    print(d.calculate(2,3))
    print(d.calculate(1,3))
    print(d.calculate(3,2))
    print(d.calculate(5,4))
    print(d.calculate(4,5))
    d.add_link(4,3,9)
    print(d.calculate(4,5))
    print(d.calculate(2,4))
    print(d.calculate(4,5))
    d.add_link(5,1,6)
    d.add_link(3,5,3)
    d.add_link(4,5,2)
    print(d.calculate(3,4))
    d.add_link(5,3,3)