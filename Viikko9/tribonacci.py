from datetime import datetime

class Tribonacci:

    def __init__(self):

        self.__cache = {0:0, 1:1, 2:2}

    def count(self, nnn):

        if nnn not in self.__cache:

            self.__cache[nnn] = self.count(nnn-1) + self.count(nnn-2) + self.count(nnn-3)

        return self.__cache[nnn]


if __name__ == "__main__":

    first, second = Tribonacci(), Tribonacci()
    print(first.count(10))
    start = datetime.now()
    print(second.count(30))
    end = datetime.now()
    print((end-start).microseconds)