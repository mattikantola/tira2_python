def count(r):

    height = len(r)
    width = len(r[0])

    visited = [[False for iii in range(width)] for jjj in range(height)]

    def traverse(y,x):

        if y < 0 or x < 0 or y>=height or x >= width:

            return

        if r[y][x] == '#':

            return

        if not visited[y][x]:
            visited[y][x] = True

            traverse(y+1,x)
            traverse(y-1,x)
            traverse(y,x+1)
            traverse(y,x-1)


    result = 0

    for row_number in range(1,height):

        for column_number in range(1, width):

            if not visited[row_number][column_number] and r[row_number][column_number] != '#':
                traverse(row_number, column_number)
                result += 1

    return result

if __name__ == "__main__":

    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3
