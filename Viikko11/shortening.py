from math import inf

'''
Koodi lentää kohta seinään
'''

class Shortening:

    def __init__(self, n):

        self.size = n + 1
        self.edgelist = []

    def add_edge(self, a, b, x):

        new_edge = tuple((a, b, x))
        self.edgelist.append(new_edge)

    def check(self, a, b):

        distances = [inf for iii in range(self.size)]
        distances[a] = 0
        iii = 1
        change_b = False

        change = True

        while change:
            
            change = False
            for edge in self.edgelist:

                start, stop, weight = edge[0:3]

                cur = distances[stop]
                new = distances[start] + weight

                if new < cur:

                    distances[stop] = new
                    change = True
                    if stop == b and iii > self.size + 1:
                        change_b = True
                    

            iii += 1

            if iii > self.size + 3:
                break

        return change_b


if __name__ == "__main__":
    s = Shortening(5)
    print(s.check(3,4))
    print(s.check(5,3))
    s.add_edge(3,4,3)
    print(s.check(3,5))
    s.add_edge(4,1,9)
    print(s.check(2,3))
    print(s.check(4,3))
    print(s.check(2,1))
    s.add_edge(3,1,-4)
    s.add_edge(2,4,8)
    print(s.check(5,3))
    print(s.check(4,1))
    print(s.check(2,5))
    print(s.check(4,5))
    print(s.check(5,3))
    s.add_edge(2,3,-5)
    s.add_edge(2,4,7)
    s.add_edge(4,2,1)
    s.add_edge(3,4,-9)
    print(s.check(4,5))
