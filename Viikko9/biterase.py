def count(s):

    cache = {}

    def seek_and_destroy(bitstring):

        if len(bitstring) == 0:

            return 1

        else:

            partitions = 0

            for iii in range(len(bitstring)-1):

                if bitstring[iii] == bitstring[iii+1]:

                    new_bitstring = bitstring[:iii] + bitstring[iii+2:]

                    if new_bitstring not in cache:

                        cache[new_bitstring] = seek_and_destroy(new_bitstring)

                    partitions += cache[new_bitstring]

            return partitions
    
    return seek_and_destroy(s)


if __name__ == "__main__":
    print(count("1100")) # 2
    print(count("1001")) # 1
    print(count("100111")) # 5
    print(count("11001")) # 0
    print(count("1100110011100111")) # 113925