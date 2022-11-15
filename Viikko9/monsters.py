def count(r):

    n = len(r)

    hirviot = [[0]*(n+1) for iii in range(n+1)]

    for iii in range(1,n):

        for jjj in range(1,n):

            if iii == 1 and jjj == 1:

                hirviot[iii][jjj] = 0
                hirvioita = 0

            elif r[iii][jjj] == '#':

                continue

            elif r[iii][jjj] == "@":

                hirvioita += 1
                hirviot[iii][jjj] += hirvioita

            else:

                hirviot[iii][jjj] = min(hirviot[iii-1][jjj], hirviot[iii][jjj-1])

    for rivi in hirviot:
        print(rivi)

if __name__ == "__main__":
    r = ["....@",
         "@##.#",
         ".##@#",
         ".@..#",
         "###@."]
    print(count(r))