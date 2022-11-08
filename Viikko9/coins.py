def count(numbers):


    n = len(numbers)
    s = sum(numbers)
    sums = set()
    choice = [False]*(s+1)
    choice[0] = True

    for iii in range(n):

        for jjj in range(s, -1, -1):

            if choice[jjj]:

                choice[jjj+numbers[iii]] = True

    return len([iii for iii in choice if iii]) - 1        

if __name__ == "__main__":
    print(count([3,4,5])) # 7
    print(count([1,1,2])) # 4
    print(count([2,2,2,3,3,3])) # 13
    print(count([42,5,5,100,1,3,3,7])) # 91