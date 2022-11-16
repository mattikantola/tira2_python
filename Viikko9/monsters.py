def count(r):

    n = len(r)

    hirviot = [[-1]*(n) for iii in range(n)]

    def traverse(y,x,monsut=0):


        if y > n - 1 or x > n - 1 or r[y][x] == '#':
            return
        
        uudet_monsut = monsut

        if r[y][x] == '@':
            uudet_monsut += 1

        if hirviot[y][x] == -1:

            hirviot[y][x] = uudet_monsut

        else:

            if uudet_monsut >= hirviot[y][x]:

                return

            else:

                hirviot[y][x] = uudet_monsut

        traverse(y+1, x, uudet_monsut)

        traverse(y,x+1,uudet_monsut)


    traverse(0,0)

    return hirviot[-1][-1]

if __name__ == "__main__":
    r = ["....@",
         "@##.#",
         ".##@#",
         ".@..#",
         "###@."]
    print(count(r))