from collections import defaultdict
import pygame as p
from Board import Board
from Constants import PIECES, WIDTH, HEIGHT, SQ_SIZE, MAX_FPS, IMAGES
from Move import Move

def main():
    
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()    
    board = Board()
    board.init_images(p)
    selected_square = tuple()
    clicked_squares = []
    move_made = False
    valid_moves = board.get_valid_moves()

    playing = True
    while playing:
        # Event queue
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
                else:
                    selected_square = (row, col)
                    clicked_squares.append(selected_square)
                # Once we have two different (row,col) moves selected, make the move on the board 
                if len(clicked_squares) == 2:
                    start_square = clicked_squares[0]
                    end_square = clicked_squares[1]
                    move = Move(start_square, end_square, board.board)
                    print(move.get_notated_move())
                    print(Move((1,1), (2,1), board.board) in valid_moves)
                    if move in valid_moves:
                        board.make_move(move)
                        move_made = True

                    # Made a move, reset
                    selected_square = tuple()
                    clicked_squares = []
            elif e.type == p.KEYDOWN:
                if e.key == p.K_u: # Undo when 'u' is pressed
                    board.undo_move()
                    move_made = True

        if move_made:
            board.get_valid_moves()
            move_made = False

        # Update the board
        board.draw_board(screen, p)
        board.draw_pieces(screen, p)
        clock.tick(MAX_FPS)
        p.display.flip()

        

if __name__ == "__main__":
    main()