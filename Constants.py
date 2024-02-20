from collections import defaultdict

WIDTH = 512
HEIGHT = 512
SQ_SIZE = HEIGHT // 8
MAX_FPS = 15


IMAGES = defaultdict(str)
PIECES = ["bR","bN","bB","bQ","bK","bP","wR","wN","wB","wQ","wK","wP"]


ROW_TO_RANK = {7 : '1', 6 : '2', 5 : '3', 4 : '4',
               3 : '5', 2 : '6', 1 : '7', 0 : '8'}

COL_TO_FILE = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd',
               4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h'}