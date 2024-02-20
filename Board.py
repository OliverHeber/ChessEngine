from Constants import PIECES, WIDTH, HEIGHT, SQ_SIZE, MAX_FPS, IMAGES
import Move

class Board():
    def __init__(self, p) -> None:
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

        self.log_of_moves = []
        self.white_to_play = True

    # Initialise images into variables to avoid repeatedly re-loading
    def init_images(self, p):
        for piece in PIECES:
            IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQ_SIZE, SQ_SIZE))

    # Draws the background colour of the chess board
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
                    # Blit (draw) the piece
                    screen.blit(IMAGES[piece], p.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    # Changes the board state to reflect the given move
    def make_move(self, move: Move):
        # We are moving a piece from a square, so it must then be empty
        self.board[move.start_row][move.start_col] = ".."

        # We are moving a piece to this square, so this piece will be allocated here
        self.board[move.end_row][move.end_col] = move.moved_piece

        # Maintain all moves to undo later
        self.log_of_moves.append(move)

        # Alternate player parity
        self.white_to_play = not self.white_to_play

    
    # Undo a move
    def undo_move(self):

        if self.log_of_moves:
            move = self.log_of_moves.pop()

            self.board[move.start_row][move.start_col] = move.moved_piece
            self.board[move.end_row][move.end_col] = move.captured_piece

            self.white_to_play = not self.white_to_play
        
        else:
            print("No move to undo")
    
    def get_valid_moves(self):
        pass