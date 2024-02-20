from collections import defaultdict
import pygame as p
import Board
from Constants import PIECES, WIDTH, HEIGHT, SQ_SIZE, MAX_FPS, IMAGES

def main():
    # Init pygame and display
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    
    # Create board object
    board = Board.Board(p)

    # Draw initial board without pieces
    board.draw_board(screen, p)

    # Initialise piece images into memory
    board.init_images(p)

    playing = True
    while playing:
        for e in p.event.get():
            if e.type == p.QUIT:
                playing = False
        # Update the pieces on the board
        board.draw_pieces(screen, p)
        clock.tick(MAX_FPS)

        # Update pygame display
        p.display.flip()

if __name__ == "__main__":
    main()