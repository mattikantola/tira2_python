def count(n, a, b):

    ''' Tarkoitus on hyppiä n-pituista listaa a:n tai b:n verran oikealle ja palauttaa niiden hyppelyiden
    määrä, joilla on mahdollista päästä täsmälleen listan loppuun. Välitulosten käyttö pelastaa tilanteelta, 
    jossa samassa kohdassa on jo oltu aiemmin ja tiedetään, miten siitä päästään loppuun. '''

    cache = dict()

    def reduction(k, a, b):

        if k==n:

            return 1

        elif k > n:

            return 0

        else:

            candidate = tuple((k, a, b))

            if candidate not in cache:

                cache[candidate] = reduction(k+a, a, b) + reduction(k+b, a, b)

            return cache[candidate]

    return reduction(0, a, b)


if __name__ == "__main__":
    print(count(4,1,2)) # 5
    print(count(10,2,5)) # 2
    print(count(10,6,7)) # 0
    print(count(30,3,5)) # 58
    print(count(50,2,3)) # 525456