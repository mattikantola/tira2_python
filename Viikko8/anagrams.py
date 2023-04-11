def create(s):

    '''Anagrammit muodostetaan peruuttavalla haulla ja cache-hajautustaulu mahdollistaa sen, että samaa anagrammia ei muodosteta
    kahdesti '''

    characters = sorted(s)

    result = []

    cache = set()

    working = ['']*len(s)

    included = [False]*len(s)

    def sequence(k):

        if k == len(s):

            candidate = "".join(working)

            if candidate not in cache:

                cache.add(candidate)

                result.append(candidate)

        else:

            for iii in range(len(characters)):

                if not included[iii]:

                    included[iii] = True

                    working[k] = characters[iii]

                    sequence(k+1)

                    included[iii] = False

    sequence(0)

    return result

if __name__ == "__main__":
    print(create("ab")) # [ab,ba]
    print(create("abac")) # [aabc,aacb,abac,abca,acab,acba,baac,baca,bcaa,caab,caba,cbaa]
    print(len(create("aybabtu"))) # 1260