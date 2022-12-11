import sys

input_file = sys.argv[1]


def check_from_left_visibility(cur_x, cur_y, grid):
    cur_tree = grid[cur_x][cur_y]

    for y in range(0, cur_y):
        if cur_tree <= grid[cur_x][y]:
            return False

    return True


def check_from_right_visibility(cur_x, cur_y, grid):
    cur_tree = grid[cur_x][cur_y]

    for y in range(cur_y + 1, len(grid[cur_x])):
        if cur_tree <= grid[cur_x][y]:
            return False

    return True


def check_from_top_visibility(cur_x, cur_y, grid):
    cur_tree = grid[cur_x][cur_y]

    for x in range(0, cur_x):
        if cur_tree <= grid[x][cur_y]:
            return False

    return True


def check_from_bottom_visibility(cur_x, cur_y, grid):
    cur_tree = grid[cur_x][cur_y]

    for x in range(cur_x + 1, len(grid)):
        if cur_tree <= grid[x][cur_y]:
            return False

    return True


if __name__ == '__main__':
    with open(input_file, 'r') as fd:
        lines = fd.readlines()

        grid = list(map(lambda line: line.rstrip('\n'), lines))

        num_col_edge = len(grid) * 2
        num_row_edge = (len(grid[0]) - 2) * 2

        total_tree_visible = num_row_edge + num_col_edge

        for x in range(1, len(grid) - 1):
            for y in range(1, len(grid[x]) - 1):
                is_visible = check_from_bottom_visibility(x, y, grid) or check_from_top_visibility(x, y, grid) \
                             or check_from_left_visibility(x, y, grid) or check_from_right_visibility(x, y, grid)

                if is_visible:
                    total_tree_visible += 1

        print(total_tree_visible)
