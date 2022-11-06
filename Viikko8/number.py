from datetime import datetime
def count(n):

    suotuisia = [0]

    def subsum(ylaraja, summa):

        if summa == n or ylaraja == 1:

            suotuisia[0] += 1
            return

        else:

            for iii in range(1, ylaraja+1):

                if summa + iii > n:
                    return
                else:
                    subsum(iii, summa+iii)

    
    subsum(n,0)
    return suotuisia[0]

if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    alku = datetime.now()
    print(count(100)) # 53174
    loppu = datetime.now()
    print((loppu-alku).seconds, (loppu-alku).microseconds)