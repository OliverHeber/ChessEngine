from collections import defaultdict
import pygame as p
from Board import Board
from Constants import PIECES, WIDTH, HEIGHT, SQ_SIZE, MAX_FPS, IMAGES
from Move import Move

def main():
    # Init pygame and display
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    
    # Create board object
    board = Board(p)

    # Initialise piece images into memory
    board.init_images(p)

    # Maintain last selected square by the user
    selected_square = tuple()

    # Maintain list of last up to 2 player clicks
    clicked_squares = []

    playing = True
    while playing:
        for e in p.event.get():
            if e.type == p.QUIT:
                playing = False
            elif e.type == p.MOUSEBUTTONDOWN:
                mouse_position = p.mouse.get_pos() # location of mouse
                row, col = mouse_position[1] // SQ_SIZE, mouse_position[0] // SQ_SIZE # board (row, col)
                # Selected a previously selected square: deselect
                if selected_square == (row, col):
                    selected_square = ()
                    clicked_squares = []
                # Selected a different square from the previous click
                else:
                    selected_square = (row, col)
                    clicked_squares.append(selected_square)
                
                if len(clicked_squares) == 2:
                    start_square = clicked_squares[0]
                    end_square = clicked_squares[1]
                    move = Move(start_square, end_square, board.board)
                    print(move.get_notated_move())
                    board.make_move(move)
                    selected_square = tuple()
                    clicked_squares = []

        # Update the pieces and board on the board
        board.draw_board(screen, p)
        board.draw_pieces(screen, p)
        clock.tick(MAX_FPS)

        # Update pygame display
        p.display.flip()

if __name__ == "__main__":
    main()