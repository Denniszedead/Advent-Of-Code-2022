opponent_rock = 'A'
opponent_paper = 'B'
opponent_scissors = 'C'

player_rock = 'X'
player_paper = 'Y'
player_scissors = 'Z'


player_lose = 'X'
player_draw = 'Y'
player_win = 'Z'


class Shape:
    point = None

    def play(self, opponent):
        pass


class Scissors(Shape):
    point = 3

    def play(self, opponent):
        point_gained = 0

        if isinstance(opponent, Scissors):
            point_gained = 3
        elif isinstance(opponent, Paper):
            point_gained = 6
        elif isinstance(opponent, Rock):
            point_gained = 0

        return self.point + point_gained


class Paper(Shape):
    point = 2

    def play(self, opponent):
        point_gained = 0

        if isinstance(opponent, Scissors):
            point_gained = 0
        elif isinstance(opponent, Paper):
            point_gained = 3
        elif isinstance(opponent, Rock):
            point_gained = 6

        return self.point + point_gained


class Rock(Shape):
    point = 1

    def play(self, opponent):
        point_gained = 0

        if isinstance(opponent, Scissors):
            point_gained = 6
        elif isinstance(opponent, Paper):
            point_gained = 0
        elif isinstance(opponent, Rock):
            point_gained = 3

        return self.point + point_gained


def opponent_shape(code):
    if code == opponent_rock:
        return Rock()
    elif code == opponent_paper:
        return Paper()
    elif code == opponent_scissors:
        return Scissors()


def player_shape(code):
    if code == player_rock:
        return Rock()
    elif code == player_paper:
        return Paper()
    elif code == player_scissors:
        return Scissors()


def player_state(code, opponent_selected_shape):
    if code == player_win:
        return win_state(opponent_selected_shape)
    elif code == player_draw:
        return draw_sate(opponent_selected_shape)
    elif code == player_lose:
        return lose_sate(opponent_selected_shape)


def win_state(opponent_selected_shape):
    win_points = 6
    if isinstance(opponent_selected_shape, Rock):
        return win_points + Paper.point
    elif isinstance(opponent_selected_shape, Paper):
        return win_points + Scissors.point
    elif isinstance(opponent_selected_shape, Scissors):
        return win_points + Rock.point


def draw_sate(opponent_selected_shape):
    draw_points = 3
    if isinstance(opponent_selected_shape, Rock):
        return draw_points + Rock.point
    elif isinstance(opponent_selected_shape, Paper):
        return draw_points + Paper.point
    elif isinstance(opponent_selected_shape, Scissors):
        return draw_points + Scissors.point


def lose_sate(opponent_selected_shape):
    lose_points = 0
    if isinstance(opponent_selected_shape, Rock):
        return lose_points + Scissors.point
    elif isinstance(opponent_selected_shape, Paper):
        return lose_points + Rock.point
    elif isinstance(opponent_selected_shape, Scissors):
        return lose_points + Paper.point
