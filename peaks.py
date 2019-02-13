RADIUS = 2
MIN_X = 0
MAX_X = 4

grid = [[1, 1, 10, 1, 1],
        [1, 1, 1, 1, 10],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [10, 1, 1, 1, 1]
        ]


def iterate_grid():
    for x in range(len(grid)):
        row = grid[x]
        for y in range(len(row)):
            # print(grid[x][y])
            is_peak = isPeak(grid, x, y, RADIUS)
            if is_peak:
                print(x, y, grid[x][y])


def isPeak(grid, x, y, radius):
    minX = max(x - radius, 0)
    maxX = min(x + radius, 4)
    minY = max(y - radius, 0)
    maxY = min(y + radius, 4)

    current_value = grid[x][y]

    is_peak = True

    for i in range(minX, maxX + 1):
        for j in range(minY, maxY + 1):
            if not (i == x and j == y):
                if grid[i][j] >= current_value:
                    is_peak = False
                    break

        if not is_peak:
            break
    return is_peak


# isPeak(grid, 0,0,RADIUS)
iterate_grid()
