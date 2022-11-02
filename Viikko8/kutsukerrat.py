def some_function(n):

    if n <= 2:

        return 1

    else:

        return 1 + some_function(n-1) + some_function(n-2) + some_function(n-3)

if __name__ == "__main__":

    print(some_function(5))
    print(some_function(10))
    print(some_function(30))
