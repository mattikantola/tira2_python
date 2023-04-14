from collections import deque

def count(r):
    
    size = len(r)

    parent_grid_initial = [[(yyy,xxx) for xxx in range(size)] for yyy in range(size)]
    flow_grid = [[[0,0] for iii in range(size)] for jjj in range(size)] 

    for yyy in range(size):

        for xxx in range(size):

            if r[yyy][xxx] == "#":
                continue
            elif r[yyy+1][xxx] == ".":
                flow_grid[yyy][xxx][0] = 1
            elif r[yyy][xxx+1] == ".":
                flow_grid[yyy][xxx][1] = 1

    path_count = 0

    def bfs(parent_grid_working):

        visited = [[False for iii in range(size)] for jjj in range(size)]
        visited[0][0] = True
        storage = deque()
        storage.append([0,0])

        while storage:
            new_square = storage.popleft()
            new_y, new_x = new_square
            neighbors = [[new_y+1,new_x],[new_y,new_x+1]]
            for neighbor in neighbors:

                neighbor_y, neighbor_x = neighbor

                if visited[neighbor_y][neighbor_x] or r[neighbor_y][neighbor_x] == '#': #ruutu on käyty läpi tai se on seinä

                    continue

                storage.append(neighbor)
                visited[neighbor_y][neighbor_x] = True
                parent_grid_working[neighbor_y][neighbor_x] = (new_y, new_x)

                if new_y == size-1 and new_x == size-1:
                    return True

        return False
    
    while bfs(parent_grid_initial):

        path_flow = 2
        node_y, node_x = size-1, size-1

        while node_y > 0 and node_x > 0:

            parent_y, parent_x = parent_grid_initial[node_y][node_x]
            path_
        

if __name__ == "__main__":
    r = [".....",
         ".###.",
         "...#.",
         "##.#.",
         "....."]
    print(count(r)) # 2