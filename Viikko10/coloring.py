''' 
Verkko, jota väritetään kahdella värillä niin, etteivät vierussolmut saa olla saman väriset. Verkkoon voi lisätä
solmuja ja tarkistaa syvyyshaulla, onko väritys mahdollista toteuttaa.
'''


class Coloring:

    def __init__(self, n):

        self.length = n + 1
        self.integrity = True
        self.__adjacency_list = [[] for iii in range(n+1)]

    def add_edge(self, a, b):

        self.__adjacency_list[a].append(b)
        self.__adjacency_list[b].append(a)


    def check(self):

        self.integrity = True
        color_list = [False for iii in range(self.length)]
        visited = [False for iii in range(self.length)]
        color_list[1] = True

        def traverse(node, color=True):

            if not visited[node]:
                visited[node] = True
                color_list[node] = not color
                for neighbor in self.__adjacency_list[node]:
                    if color_list[node] == color_list[neighbor] and visited[neighbor]: #ollaan tilanteessa, jossa
                                                                                        # vierussolmu on väritetty samalla värillä
                                                                                        # kuin solmu, jota käsitellään. Tämä on merkki
                                                                                        # värityksen epäonnistumisesta.
                        self.integrity = False
                    traverse(neighbor, color_list[node])

        for iii in range(self.length):

            if not visited[iii]:
                traverse(iii)

        return self.integrity

if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(3,4)
    c.add_edge(1,4)
    print(c.check()) # True
    c.add_edge(2,4)
    print(c.check()) # False