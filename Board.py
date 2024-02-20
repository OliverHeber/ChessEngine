from collections import defaultdict
from Constants import PIECES, WIDTH, HEIGHT, SQ_SIZE, MAX_FPS, IMAGES
from Move import Move

class Board():
    def __init__(self) -> None:
        self.board = [
                ["bR","bN","bB","bQ","bK","bB","bN","bR"],
                ["bP","bP","bP","bP","bP","bP","bP","bP"],
                ["..","..","..","..","..","..","..",".."],
                ["..","..","..","..","..","..","..",".."],
                ["..","..","..","..","..","..","..",".."],
                ["..","..","..","..","..","..","..",".."],
                ["wP","wP","wP","wP","wP","wP","wP","wP"],
                ["wR","wN","wB","wQ","wK","wB","wN","wR"]
            ]
        self.move_function = {'P' : self.get_pawn_moves, 'R' : self.get_rook_moves, 'N' : self.get_knight_moves, 
                              'B' : self.get_bishop_moves, 'Q' : self.get_queen_moves, 'K' : self.get_king_moves}
        self.log_of_moves = []
        self.white_to_play = True

    # Initialise images into variables to avoid repeatedly re-loading
    def init_images(self, p):
        for piece in PIECES:
            IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    # Draws the light/dark squares onto the chess board
    def draw_board(self, screen, p):
        for row in range(8):
            for col in range(8):
                colour = p.Color("gray") if ((row + col) % 2) else p.Color("white")
                p.draw.rect(screen, colour, p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    # Draws the pieces onto the created board
    def draw_pieces(self, screen, p):
        for row in range(8):
            for col in range(8):
                if self.board[row][col] != "..":
                    piece = self.board[row][col]
                    screen.blit(IMAGES[piece], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    # Changes the board state to reflect the given move
    def make_move(self, move: Move):
        # Update current and target square pieces
        self.board[move.start_row][move.start_col] = ".."
        self.board[move.end_row][move.end_col] = move.moved_piece

        # Push all moves to stack for undoing
        self.log_of_moves.append(move)

        self.white_to_play = not self.white_to_play
    
    # Undo a move
    def undo_move(self):
        if self.log_of_moves:
            move = self.log_of_moves.pop()
            self.board[move.start_row][move.start_col] = move.moved_piece
            self.board[move.end_row][move.end_col] = move.captured_piece
            self.white_to_play = not self.white_to_play
    
    def in_bounds(self, row, col) -> bool:
        return (0 <= row <= 7) and (0 <= col <= 7)
    
    def get_valid_moves(self):
        return self.get_all_moves()

    def get_all_moves(self):
        moves = []

        for row in range(8):
            for col in range(8):
                piece_colour, piece_type = self.board[row][col][0], self.board[row][col][1]
                if (self.white_to_play and piece_colour == 'w') or (not self.white_to_play and piece_colour == 'b'):
                    possible = self.move_function[piece_type](row, col)
                    if possible:
                        moves.extend(possible.copy())
        return moves
    
    def get_pawn_moves(self, row, col):
        moves = []
        # White pawn moves
        if self.white_to_play:
            if self.board[row - 1][col] == "..":
                moves.append(Move((row, col), (row - 1, col), self.board))
                if row == 6 and self.board[row - 2][col] == "..":
                    moves.append(Move((row, col), (row - 2, col), self.board))
            if self.in_bounds(row, col - 1):
                if self.board[row - 1][col - 1][0] == 'b':
                    moves.append(Move((row, col), (row - 1, col - 1), self.board))
            if self.in_bounds(row, col + 1):
                if self.board[row - 1][col + 1][0] == 'b':
                    moves.append(Move((row, col), (row - 1, col + 1), self.board))
        # Black pawn moves
        else:
            if self.board[row + 1][col] == "..":
                moves.append(Move((row, col), (row + 1, col), self.board))
                if row == 1 and self.board[row + 2][col] == "..":
                    moves.append(Move((row, col), (row + 2, col), self.board))
            if self.in_bounds(row, col - 1):
                if self.board[row + 1][col - 1][0] == 'w':
                    moves.append(Move((row, col), (row + 1, col - 1), self.board))
            if self.in_bounds(row, col + 1):
                if self.board[row + 1][col + 1][0] == 'w':
                    moves.append(Move((row, col), (row + 1, col + 1), self.board))
        return moves

    def get_rook_moves(self, row, col):
        moves = []
        enemy_colour = 'b' if self.white_to_play else 'w'
        for x, y in [(1,0),(-1,0),(0,1),(0,-1)]:
            for i in range(1, 8):
                end_row, end_col = row + x * i, col + y * i
                if self.in_bounds(end_row, end_col):
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "..":
                        moves.append(Move((row, col), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_colour:
                        moves.append(Move((row, col), (end_row, end_col), self.board))
                        break
                    else:
                        break
                else:
                    break
        return moves

    def get_knight_moves(self, row, col):
        moves = []
        enemy_colour = 'b' if self.white_to_play else 'w'

        for x, y in [(-2, -1),(-2, 1),(-1, -2),(-1, 2),(1, -2),(1, 2),(2, -1),(2, 1)]:
            end_row, end_col = row + x, col + y

            if self.in_bounds(end_row, end_col):
                end_piece = self.board[end_row][end_col]
                if end_piece == "..":
                    moves.append(Move((row, col), (end_row, end_col), self.board))
                elif end_piece[0] == enemy_colour:
                    moves.append(Move((row, col), (end_row, end_col), self.board))
        return moves

    def get_bishop_moves(self, row, col):
        moves = []
        enemy_colour = 'b' if self.white_to_play else 'w'
        for x, y in [(1,1),(1,-1),(-1,1),(-1,-1)]:
            for i in range(1, 8):
                end_row, end_col = row + x * i, col + y * i
                if self.in_bounds(end_row, end_col):
                    end_piece = self.board[end_row][end_col]
                    if end_piece == "..":
                        moves.append(Move((row, col), (end_row, end_col), self.board))
                    elif end_piece[0] == enemy_colour:
                        moves.append(Move((row, col), (end_row, end_col), self.board))
                        break
                    else:
                        break
                else:
                    break
        return moves

    def get_queen_moves(self, row, col):
        moves = []
        moves.append(self.get_bishop_moves(row, col))
        if len(moves) > 0:
            moves.extend(self.get_rook_moves(row, col))
        else:
            moves.append(self.get_rook_moves(row, col))
        return moves
        
    def get_king_moves(self, row, col):
        moves = []
        enemy_colour = 'b' if self.white_to_play else 'w'

        for x, y in [(-1, -1),(-1, 0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)]:
            end_row, end_col = row + x, col + y

            if self.in_bounds(end_row, end_col):
                end_piece = self.board[end_row][end_col]
                if end_piece == "..":
                    moves.append(Move((row, col), (end_row, end_col), self.board))
                elif end_piece[0] == enemy_colour:
                    moves.append(Move((row, col), (end_row, end_col), self.board))
        return moves
