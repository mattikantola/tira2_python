from datetime import datetime

def some_function(n):

    if n <= 2:

        return n

    else:

        return some_function(n-1) + some_function(n-2) + some_function(n-3)

if __name__ == "__main__":

    start = datetime.now()
    result = some_function(30)
    end = datetime.now()
    print(result)
    print((end-start).seconds)