def create(n):

    result = []
    charset = "ABC"
    working = ['']*n

    def sequence(k):

        if k==n:

            result.append("".join(working))

        else:

            for character in charset:

                if k > 0:

                    if working[k-1] == character:

                        continue

                    else:

                        working[k] = character

                        sequence(k+1)

                else:

                    working[k] = character

                    sequence(k+1)


    sequence(0)
    return result

if __name__ == "__main__":

    print(create(1))
    print(create(2))
    print(len(create(5)))
                