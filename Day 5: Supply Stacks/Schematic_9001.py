import numpy as np


class Schematic:
    num_columns = 0
    num_rows = 0

    def __init__(self, schematic_array):
        self.num_rows = int(len(schematic_array)) - 1
        self.num_columns = int(schematic_array[-1].split(' ')[-1])
        self.schematic = np.full([self.num_rows, self.num_columns], ' ')

        for row_no in range(self.num_rows):
            row_lines = schematic_array[row_no].rstrip('\n')
            row = row_lines.split(' ')

            for col_no in range(self.num_columns):
                element = row[col_no][1]
                self.schematic[row_no][col_no] = ' ' if element == '0' else element

    def move_crate(self, move_line):
        move_line_array = move_line.split(' ')
        no_crates = int(move_line_array[1])
        source = int(move_line_array[3]) - 1
        destination = int(move_line_array[5]) - 1

        selected_crates = self.get_crate(source, no_crates)
        self.place_crates(selected_crates, destination)
        self.clean_row()

    def get_crate(self, source, no_crates):
        row_no = 0
        crates = []
        while row_no < self.num_rows and len(crates) < no_crates:
            element = self.schematic[row_no][source]
            if element != ' ':
                self.schematic[row_no][source] = ' '
                crates.append(element)
            row_no += 1

        return crates

    def place_crates(self, crates, destination):
        row_no = 0
        while row_no < self.num_rows:
            element = self.schematic[row_no][destination]
            if element != ' ':
                self.fill_column(crates, row_no - 1, destination)
                break
            row_no += 1
        if row_no >= self.num_rows:
            while len(crates) > 0:
                self.fill_column(crates, row_no - 1, destination)

    def fill_column(self, crates, initial_row_no, destination):
        row_no = initial_row_no
        while len(crates) > 0:
            if row_no < 0:
                self.add_row()
                row_no += 1
            self.schematic[row_no][destination] = crates.pop()
            row_no -= 1

    def add_row(self):
        additional_matrix = np.full([1, self.num_columns], ' ')
        self.schematic = np.vstack((additional_matrix, self.schematic))
        self.num_rows += 1

    def clean_row(self):
        empty = True

        while empty:
            for element in self.schematic[0]:
                if element != ' ':
                    empty = False

            if empty:
                self.schematic = np.delete(self.schematic, 0, axis=0)
                self.num_rows -= 1
