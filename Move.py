import Board
from Constants import ROW_TO_RANK, COL_TO_FILE

class Move():
    def __init__(self, start_square: tuple, end_square: tuple, board: Board) -> None:
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = end_square[0]
        self.end_col = end_square[1]
        self.moved_piece = board[self.start_row][self.start_col]
        self.captured_piece = board[self.end_row][self.end_col]
    
    def get_notated_move(self):
        return COL_TO_FILE[self.start_col] + ROW_TO_RANK[self.start_row] +\
               COL_TO_FILE[self.end_col] + ROW_TO_RANK[self.end_row]