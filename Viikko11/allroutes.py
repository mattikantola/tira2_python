'''Kaupunkien välille voi lisätä yhteyksiä ja tarvittaessa selvittää lyhimmät etäisyydet kaikkien kaupunkien välillä
Floyd-Warshall-algoritmilla'''

from math import inf

class AllRoutes:

    def __init__(self, n):

        self.size = n + 1
        self.distances = [[inf for iii in range(self.size)] for jjj in range(self.size)]

    def add_road(self, a, b, x):

        if x < self.distances[a][b]:

            self.distances[a][b] = x
            self.distances[b][a] = x

    def get_table(self):

        for iii in range(self.size):

            self.distances[iii][iii] = 0

        for k in range(1, self.size):

            for i in range(1, self.size):

                for j in range(1, self.size):

                    self.distances[i][j] = min(self.distances[i][j], self.distances[i][k] + self.distances[k][j])

        result = []

        for row in self.distances[1:]:

            real_data = row[1:]

            for iii in range(len(real_data)):

                if real_data[iii] == inf:

                    real_data[iii] = - 1

            result.append(real_data)

        return result


if __name__ == "__main__":
    a = AllRoutes(4)
    a.add_road(1,2,2)
    a.add_road(1,3,5)
    a.add_road(2,3,1)
    print(a.get_table())
    # [[0,2,3,-1],[2,0,1,-1],[3,1,0,-1],[-1,-1,-1,0]]