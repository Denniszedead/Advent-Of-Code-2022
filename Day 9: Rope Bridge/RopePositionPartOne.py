import numpy as numpy

RIGHT = 'R'
UP = 'U'
DOWN = 'D'
LEFT = 'L'


def is_adjacent(adjacency):
    if adjacency[0] < -1 or adjacency[0] > 1:
        return False
    if adjacency[1] < -1 or adjacency[1] > 1:
        return False
    return True


class RopePositionPartOne:
    def __init__(self):
        self.pos_head = [0, 0]
        self.pos_tail = [0, 0]
        self.tail_visited = []

    def get_tail_visited(self):
        self.tail_visited.append(self.pos_tail)
        return set(map(lambda xs: tuple(xs), self.tail_visited))

    def move_rope(self, movement):
        direction = movement[0]
        steps = int(movement[1])

        for num in range(steps):
            self.move_head(direction)
            self.move_tail()

    def move_head(self, direction):
        head_row = self.pos_head[0]
        head_col = self.pos_head[1]

        # self.grid[head_row, head_col] = '.'

        if direction == UP:
            head_row += 1
        elif direction == DOWN:
            head_row -= 1
        elif direction == LEFT:
            head_col -= 1
        elif direction == RIGHT:
            head_col += 1

        self.pos_head = [head_row, head_col]

    def move_tail(self):
        prev_row = self.pos_tail[0]
        prev_col = self.pos_tail[1]

        adjacency = self.get_tail_adjacency()

        if not is_adjacent(adjacency):
            if adjacency[0] == 0:
                self.move_tail_horizontally(adjacency[1])
            elif adjacency[1] == 0:
                self.move_tail_vertically(adjacency[0])
            else:
                self.move_tail_diagonally(adjacency)
            self.tail_visited.append([prev_row, prev_col])

    def move_tail_vertically(self, adjacency_row):
        if adjacency_row < -1:
            self.pos_tail[0] -= 1
        elif adjacency_row > 1:
            self.pos_tail[0] += 1

    def move_tail_horizontally(self, adjacency_col):
        if adjacency_col < -1:
            self.pos_tail[1] -= 1
        elif adjacency_col > 1:
            self.pos_tail[1] += 1

    def move_tail_diagonally(self, adjacency):
        adjacency_row = adjacency[0]
        adjacency_col = adjacency[1]

        if adjacency_row < 0:
            self.pos_tail[0] -= 1
        elif adjacency_row > 0:
            self.pos_tail[0] += 1

        if adjacency_col < 0:
            self.pos_tail[1] -= 1
        elif adjacency_col > 0:
            self.pos_tail[1] += 1

    def get_tail_adjacency(self):
        tail_row = self.pos_tail[0]
        tail_col = self.pos_tail[1]

        head_row = self.pos_head[0]
        head_col = self.pos_head[1]

        return [head_row - tail_row, head_col - tail_col]
