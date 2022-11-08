def find(t):

    n = len(t)

    longest = [1]*n

    for iii in range(n):

        for jjj in range(iii):

            if abs(t[jjj]-t[iii]) <= 1 and longest[jjj] + 1 > longest[iii]:

                longest[iii] = longest[jjj] + 1

    return max(longest)


if __name__ == "__main__":
    print(find([1,2,3,4,5])) # 5
    print(find([5,5,5,5,5])) # 5
    print(find([5,2,3,8,2,4,1])) # 4
    print(find([1,3,5,7,9])) # 1