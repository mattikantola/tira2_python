'''
Muodostetaan verkko numeroista 2:stä n:ään asti ja lisätään solmut vieruslistassa vierekkäin, jos jompikumpi jakaa toisen.
Komponentit etsitään aloittamalla uusi syvyyshaku jokaisesta solmusta, jossa ei ole aiemman syvyyshaun aikana käyty.
Syvyyshaku käy aina koko komponentin läpi eikä mitään muuta, jolloin syvyyshakujen määrä on komponenttien määrä.
'''


class Components:

    def __init__(self, n):

        self.__upper_bound = n
        self.__adjacency = [[] for iii in range(n+1)]

    def show_matrix(self):

        for row in self.__adjacency:

            print(row)
    
    def make_edges(self):

        for iii in range(2,self.__upper_bound+1):

            for jjj in range(iii, self.__upper_bound+1):

                if iii%jjj == 0 or jjj%iii == 0:

                    self.__adjacency[iii].append(jjj)
                    self.__adjacency[jjj].append(iii)


    def components(self):

        visited = [False]*(self.__upper_bound + 1)

        def traverse(node):


            visited[node] = True

            for neighbor in self.__adjacency[node]:

                if not visited[neighbor]:


                    traverse(neighbor)


        result = 0

        for iii in range(2, self.__upper_bound + 1):

            if not visited[iii]:

                traverse(iii)
                result += 1

        return result

if __name__ == "__main__":

    test = Components(1000)
    test.make_edges()
    print(test.components())