import random

def subsequence(n):

    numbers = list(range(1, n+1))
    random.shuffle(numbers)

    nnn = len(numbers)

    longest = [1]*nnn

    for iii in range(nnn):

        for jjj in range(iii):

            if numbers[jjj] < numbers[iii] and longest[jjj] + 1 > longest[iii]:

                longest[iii] = longest[jjj] + 1

    return max(longest)   

if __name__ == "__main__":

    print(subsequence(5000))