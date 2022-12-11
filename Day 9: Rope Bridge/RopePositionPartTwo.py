import numpy as numpy

RIGHT = 'R'
UP = 'U'
DOWN = 'D'
LEFT = 'L'

tail_no = 9


def is_adjacent(adjacency):
    if adjacency[0] < -1 or adjacency[0] > 1:
        return False
    if adjacency[1] < -1 or adjacency[1] > 1:
        return False
    return True


class RopePositionPartTwo:
    def __init__(self):
        self.pos = [[0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0], [0,0]]
        self.tail_visited = []

    def get_tail_visited(self):
        self.tail_visited.append(self.pos[tail_no])
        return set(map(lambda xs: tuple(xs), self.tail_visited))

    def move_rope(self, movement):
        direction = movement[0]
        steps = int(movement[1])

        for num in range(steps):
            self.move_head(direction)
            for tail in range(1, 10):
                self.move_tail(tail - 1, tail)

    def move_head(self, direction):
        head_row = self.pos[0][0]
        head_col = self.pos[0][1]

        # self.grid[head_row, head_col] = '.'

        if direction == UP:
            head_row += 1
        elif direction == DOWN:
            head_row -= 1
        elif direction == LEFT:
            head_col -= 1
        elif direction == RIGHT:
            head_col += 1

        self.pos[0] = [head_row, head_col]

    def move_tail(self, knot_before, knot_after):
        prev_row = self.pos[tail_no][0]
        prev_col = self.pos[tail_no][1]

        adjacency = self.get_tail_adjacency(knot_before, knot_after)

        if not is_adjacent(adjacency):
            if adjacency[0] == 0:
                self.move_tail_horizontally(adjacency[1], knot_after)
            elif adjacency[1] == 0:
                self.move_tail_vertically(adjacency[0], knot_after)
            else:
                self.move_tail_diagonally(adjacency, knot_after)
            self.tail_visited.append([prev_row, prev_col])

    def move_tail_vertically(self, adjacency_row, knot_after):
        if adjacency_row < -1:
            self.pos[knot_after][0] -= 1
        elif adjacency_row > 1:
            self.pos[knot_after][0] += 1

    def move_tail_horizontally(self, adjacency_col, knot_after):
        if adjacency_col < -1:
            self.pos[knot_after][1] -= 1
        elif adjacency_col > 1:
            self.pos[knot_after][1] += 1

    def move_tail_diagonally(self, adjacency, knot_after):
        adjacency_row = adjacency[0]
        adjacency_col = adjacency[1]

        if adjacency_row < 0:
            self.pos[knot_after][0] -= 1
        elif adjacency_row > 0:
            self.pos[knot_after][0] += 1

        if adjacency_col < 0:
            self.pos[knot_after][1] -= 1
        elif adjacency_col > 0:
            self.pos[knot_after][1] += 1

    def get_tail_adjacency(self, knot_before, knot_after):
        tail_row = self.pos[knot_after][0]
        tail_col = self.pos[knot_after][1]

        head_row = self.pos[knot_before][0]
        head_col = self.pos[knot_before][1]

        return [head_row - tail_row, head_col - tail_col]
