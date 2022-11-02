def create(n):

    charset = "ABC"

    result = []

    working = ['']*n

    def sequence(k):

        if k==n:

            result.append("".join(working))

        else:

            for character in charset:

                working[k] = character

                sequence(k+1)

    sequence(0)

    return result

if __name__ ==  "__main__":

    print(create(1))
    print(create(2))
    print(len(create(5)))