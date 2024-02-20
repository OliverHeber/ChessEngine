import Board
from Constants import ROW_TO_RANK, COL_TO_FILE

class Move():
    def __init__(self, start_square: tuple, end_square: tuple, board: Board) -> None:
        # Original position of the piece
        self.start_row, self.start_col = start_square[0], start_square[1]
        # Position the piece will be moved to
        self.end_row, self.end_col = end_square[0], end_square[1]
        
        # Piece at original position
        self.moved_piece = board[self.start_row][self.start_col]
        # Piece (or not) at the target position
        self.captured_piece = board[self.end_row][self.end_col]

        self.move_id = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col

    def __eq__(self, move) -> None:
        if isinstance(move, Move):
            return self.move_id == move.move_id
        return False

    # Returns the start and end square of a move using chess notation
    def get_notated_move(self):
        return COL_TO_FILE[self.start_col] + ROW_TO_RANK[self.start_row] +\
               COL_TO_FILE[self.end_col] + ROW_TO_RANK[self.end_row]
