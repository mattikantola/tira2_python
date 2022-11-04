def count(n):

    choice = [0]*(n+1)
    suotuisia = [0]

    def subsum(ylaraja, summa):

        if summa == n:

            suotuisia[0] += 1

        else:

            for iii in range(1, ylaraja+1):

                if summa + iii > n:
                    return
                else:
                    choice[iii] += 1
                    subsum(iii, summa+iii)
                    choice[iii] -= 1
    
    subsum(n,0)
    return suotuisia[0]

if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    print(count(42)) # 53174