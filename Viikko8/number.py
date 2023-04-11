from datetime import datetime
def count(n):

    ''' Dynaamisen ohjelmoinnin algoritmi, joka kertoo, kuinka monella eri tavalla voidaan luku n esittää
        itseään pienempien kokonaislukujen summana. Laskennan välitulos määrittyy vain ja ainoastaan kahdesta
        asiasta eli luvusta, joka on "suurin sallittu mukaan otettava" ja toisesta luvusta, joka on esitystavan
        siihenastinen summa. Välitulokset ovat cachessa ja niitä käytetään, mikäli ne ovat olemassa. '''

    cache = {}

    def subsum(ylaraja, summa):

        if summa == n or ylaraja == 1:

            return 1

        if summa > n:

            return 0

        else:

            working = 0

            for iii in range(1,min(ylaraja+1,n-summa+1)):

                candidate = tuple([iii, summa+iii])
                if candidate not in cache:
                    cache[candidate] = subsum(iii, summa+iii)
                working += cache[candidate]
  
            return working

    return subsum(n,0)

if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    alku = datetime.now()
    print(count(1000)) # 53174
    loppu = datetime.now()
    print((loppu-alku).seconds, "sekuntia,", (loppu-alku).microseconds, "mikrosekuntia") 