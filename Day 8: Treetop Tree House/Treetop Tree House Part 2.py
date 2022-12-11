import sys

input_file = sys.argv[1]


def calculate_left_score(cur_x, cur_y, grid):
    score = 0
    for y in range(cur_y - 1, -1, -1):
        score += 1
        if grid[cur_x][y] >= grid[cur_x][cur_y]:
            break

    return score


def calculate_right_score(cur_x, cur_y, grid):
    score = 0
    for y in range(cur_y + 1, len(grid[cur_x])):
        score += 1
        if grid[cur_x][y] >= grid[cur_x][cur_y]:
            break

    return score


def calculate_top_score(cur_x, cur_y, grid):
    score = 0
    for x in range(cur_x - 1, -1, -1):
        score += 1
        if grid[x][cur_y] >= grid[cur_x][cur_y]:
            break

    return score


def calculate_bottom_score(cur_x, cur_y, grid):
    score = 0
    for x in range(cur_x + 1, len(grid)):
        score += 1
        if grid[x][cur_y] >= grid[cur_x][cur_y]:
            break

    return score


if __name__ == '__main__':
    with open(input_file, 'r') as fd:
        lines = fd.readlines()

        grid = list(map(lambda line: line.rstrip('\n'), lines))

        all_scores = {}

        for x in range(0, len(grid)):
            for y in range(0, len(grid[x])):
                score_top = calculate_top_score(x, y, grid)
                score_bottom = calculate_bottom_score(x, y, grid)
                score_left = calculate_left_score(x, y, grid)
                score_right = calculate_right_score(x, y, grid)

                total_score = score_top * score_bottom * score_left * score_right

                all_scores[f'[{x}, {y}]'] = total_score

        print(dict(sorted(all_scores.items(), key=lambda x:x[1])))
