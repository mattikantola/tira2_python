def count(n):

    cache = set()
    choice = [0]*(n+1)

    def subsum(k,h):

        if h==n:

            cache.add(tuple(choice))

        elif h > n:

            return

        else:

            for iii in range(1,n+1):

                if h + iii > n:
                    return
                choice[iii] += 1
                subsum(k+1, h+iii)
                choice[iii] -= 1


    subsum(0,0)
    return len(cache)

if __name__ == "__main__":
    print(count(4)) # 5
    print(count(5)) # 7
    print(count(8)) # 22
    print(count(42)) # 53174