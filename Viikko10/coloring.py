from collections import deque

class Coloring:

    class Node:

        def __init__(self, color = 0): #0 is no color, 1 is the first and 2 is the second

            self.color = color
            self.visited = False
            self.neighbors = []

    def __init__(self, n):

        self.elements = [Coloring.Node() for node in range(0, n+1)]

    def add_edge(self, a, b):

        self.elements[a].neighbors.append(b)
        self.elements[b].neighbors.append(a)

    def check(self):

        def traverse(begin): # begin variable is an integer position of the node list

            working = deque()
            working.append(begin)
            self.elements[begin].visited = True

            while len(working) > 0:

                node = working.popleft()

                for neighbor in self.elements[node].neighbors:

                    


