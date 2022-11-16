from collections import deque

def count(r):

    height = len(r)
    width = len(r[0])

    visited = [[False for iii in range(width)] for jjj in range(height)]
    distance = [[0 for iii in range(width)] for jjj in range(height)]
    
    def traverse(cur_y, cur_x):

        visited[cur_y][cur_x] = True
        working = deque()
        cur_pos = tuple((cur_y, cur_x))
        working.append(cur_pos)

        while len(working) > 0:

            new_y, new_x = working.popleft()

            neighbors = [tuple((new_y+1, new_x)), tuple((new_y-1, new_x)), tuple((new_y, new_x+1)), tuple((new_y, new_x-1))]

            for neighbor in neighbors:

                neighbor_y, neighbor_x = neighbor

                if visited[neighbor_y][neighbor_x] or r[neighbor_y][neighbor_x] == '#':

                    continue

                working.append(neighbor)
                visited[neighbor_y][neighbor_x] = True
                distance[neighbor_y][neighbor_x] = distance[new_y][new_x] + 1


    b_y, b_x = 0, 0

    for y_coord in range(1,height-1):

        for x_coord in range(1,width-1):

            if r[y_coord][x_coord] == 'A':

                traverse(y_coord, x_coord)
            
            if r[y_coord][x_coord] == 'B':

                b_y, b_x = y_coord, x_coord

    if distance[b_y][b_x] > 0:
        return distance[b_y][b_x]
    else:
        return -1
            


if __name__ == "__main__":

    r = ["########",
         "#.A....#",
         "#.#.##.#",
         "#.##...#",
         "#...B#.#",
         "########"]

    print(count(r))