def count(r):

    height = len(r)
    width = len(r[0])
    breaks = [[-1 for iii in range(width)] for jjj in range(height)]

    def traverse(y,x):

        if r[y][x] == 'B':

            return breaks[y][x]
        
        elif r[y][x] == -1:

            traverse()