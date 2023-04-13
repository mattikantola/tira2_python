from math import inf
from collections import deque
from copy import deepcopy

class Ball:
    def __init__(self,n):
        
        self.n = n
        self.size = 2*n+2
        self.adjacency = [[-1 for jjj in range(self.size)] for iii in range(self.size)]
        self.visited = [False for iii in range(self.size)]
        self.backup = []

    def add_pair(self,a,b):
        
        if self.adjacency[a][b+self.n] == -1:
            self.adjacency[a][b+self.n] = 0
        self.adjacency[a][b+self.n] += 1
        self.adjacency[b+self.n][a] = max(0, self.adjacency[b+self.n][a])
        self.adjacency[0][a] = 1
        self.adjacency[b+self.n][-1] = 1

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
                        
                        return True #Päästiin kohdesolmuun, jonka saavuttamisesta välitetään tieto
                                    #kutsujalle.
        
        return False #ei päästy kohdesolmuun
    
    def calculate(self):

        parents = [-1]*self.size
        max_flow = 0
        self.backup = deepcopy(self.adjacency) #muodostetaan kopio alkuperäisestä verkosta, jotta
                                                #voidaan käsitellä sitä sotkematta alkuperäisiä
                                                #kaaria (seuraava laskentakerta ei saa mennä pilalle)
        while self.bfs(0, self.size-1, parents):#aina kun leveyshaku löytää polun lähteen ja
                                            #kohteen välille, voidaan algoritmia jatkaa ja
                                            #päivittää työverkkoa.


            path_flow = inf
            node = self.size - 1
            while node != 0:                                            #polkua pitkin kulkevaa virtausta
                                                                        #rajoittaa joko olemassaoleva virtaus
                                                                        #tai virtaus solmun ja sen vanhemman
                                                                        #välillä.
                parent = parents[node]
                path_flow = min(path_flow, self.backup[parent][node])
                node = parent

            node = self.size - 1
            while node != 0:    #peruutetaan ja vähennetään alkuperäisistä kaarista saatu minimipaino
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
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1,2)
    print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2