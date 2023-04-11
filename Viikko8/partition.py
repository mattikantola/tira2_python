def check(t):

    '''params t: lista, jonka osituksista ollaan kiinnostuneita
        Tehdään alifunktiossa parts peruuttava haku listan osituksista ja jos löydetään sopiva ositus, niin
        tavoite on saavutettu
     '''

    choice = [0]*len(t)
    result = set()


    if sum(t) % 2 != 0:

        return False

    def parts(k):

        if k == len(t):

            candidate = t.copy()

            for iii in range(len(choice)):

                candidate[iii] *= choice[iii]

            if sum(t) == 2*sum(candidate):

                result.add(True) # one answer is found and that is enough
                return

        else:

            for iii in (0,1):

                choice[k] = iii
                parts(k+1)

    
    answer = parts(0)

    if True in result:

        return True

    else:

        return False


if __name__ == "__main__":
    print(check([3,4,5])) # False
    print(check([16,8,4,4])) # True
    print(check([9,4,8,7,6])) # True
    print(check([1,2,3,4,5,6])) # False
    print(check([1,2,3,4,5,6,7])) # True
    print(check([4,4,4,6,6])) # True
