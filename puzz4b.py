class Board(object):
    def __init__(self, board):
        self.board = board
        self.drawn_board = [[0 for _ in range(5)] for _ in range(5)]
    
    def __repr__(self):
        print_str = ''
        for row_ix, row in enumerate(self.board):
            print_str += ' '.join([str(i) for i in row])
            print_str += ' | '
            print_str += ' '.join([str(i) for i in self.drawn_board[row_ix]])
            print_str += '\n'
        return print_str

    @property
    def drawn_board_t(self):
        return [
            [
                self.drawn_board[col][row] 
                for col in range(len(self.drawn_board))
            ]
            for row in range(len(self.drawn_board[0]))
        ]

    def check_for_win(self, board):
        for row in board:
            if sum(row) == 5:
                return True

    def check_rows_for_win(self):
        return self.check_for_win(self.drawn_board)

    def check_cols_for_win(self):
        return self.check_for_win(self.drawn_board_t)

    def draw_number(self, number):
        for row_ix, row_arr in enumerate(self.board):
            for col_ix, col_val in enumerate(row_arr):
                if col_val == number:
                    self.drawn_board[row_ix][col_ix] = 1
    
    def calculate_score(self, last_drawn_number):
        score = 0
        for row_ix, row in enumerate(self.drawn_board):
            for col_ix, drawn_number in enumerate(row):
                if not drawn_number:
                    score += self.board[row_ix][col_ix]
        return (score * last_drawn_number)


class Game(object):
    def __init__(self, draw_order, boards):
        self.draw_order = draw_order
        self.boards = boards

    def run(self):
        for number in self.draw_order:
            boards_to_pop = []
            for board_ix, board in enumerate(self.boards):
                board.draw_number(number)
                is_winner = (
                    board.check_rows_for_win() or 
                    board.check_cols_for_win()
                )
                if is_winner:
                    if len(self.boards) == 1:
                        return board.calculate_score(number)
                    boards_to_pop.append(board_ix)
            # make sure to sort the pop indices in reverse order
            # to avoid index errors
            boards_to_pop.sort(reverse=True)
            for pop_ix in boards_to_pop:
                board = self.boards.pop(pop_ix)


def execute_game(): 
    with open('inputs/input4.txt') as fh:
        lines = fh.readlines()
        boards = []
        draw_order = list(map(int, lines[0].strip().split(',')))

        board = []
        for line in lines[2:]:
            if line == '\n':
                board_obj = Board(board)
                boards.append(board_obj)
                board = []
                continue
            board_row = list(map(int, line.strip().split()))
            board.append(board_row)
 
    game = Game(draw_order, boards)
    score = game.run()
    return score


_runner = execute_game
