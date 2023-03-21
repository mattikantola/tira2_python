from math import inf
from collections import deque

def count(r):

    height = len(r)
    width = len(r[0])

    visited = [[False for iii in range(width)] for jjj in range(height)]
    distances = [[inf for iii in range(width)] for jjj in range(height)]

    x_a, x_b = 0,0
    y_a, y_b = 0,0

    for y in range(1, height-1):

        for x in range(1, width-1):

            if r[y][x] == "A":
                y_a = y
                x_a = x
            if r[y][x] == "B":
                y_b = y
                x_b = x

    distances[y_a][x_a] = 0
    visited[y_a][x_a] = True
    start = tuple([y_a, x_a])
    ones = deque()
    zeros = deque()

    zeros.append(start)

    while len(ones) + len(zeros) > 0:

        if len(zeros) > 0:

            node = zeros.popleft()

        elif len(ones) > 0:

            node = ones.popleft()

        cur_y, cur_x = node

        for y_change, x_change in [(1,0), (0,1), (-1,0), (0,-1)]:

            new_y, new_x = cur_y + y_change, cur_x + x_change

            if r[new_y][new_x] == "#" or visited[new_y][new_x]: #ei mitään syytä mennä seinäruutuun tai vierailla jo valmiissa

                continue

            elif r[new_y][new_x] == "*":

                ones.append(tuple([new_y,new_x]))
                arch = 1

            else:

                zeros.append(tuple([new_y, new_x]))
                arch = 0

            visited[new_y][new_x] = True
            distances[new_y][new_x] = min(distances[new_y][new_x], distances[cur_y][cur_x]+arch)

    return distances[y_b][x_b]

if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    print(count(r)) # 2