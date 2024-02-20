# Define board dimensions as constants
from collections import defaultdict

WIDTH = 512
HEIGHT = 512
SQ_SIZE = HEIGHT // 8
MAX_FPS = 15

# Define images dictionary and pieces list as constants
IMAGES = defaultdict(str)
PIECES = ["bR","bN","bB","bQ","bK","bP","wR","wN","wB","wQ","wK","wP"]

# Define mapping of ranks to rows
# RANK_TO_ROW = {'1' : 7, '2' : 6, '3' : 5, '4' : 4,
#                '5' : 3, '6' : 2, '7' : 1, '8' : 0}
# ROW_TO_RANK = {v : k for k, v in RANK_TO_ROW.items()}

ROW_TO_RANK = {7 : '1', 6 : '2', 5 : '3', 4 : '4',
               3 : '5', 2 : '6', 1 : '7', 0 : '8'}

# FILE_TO_COL = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3,
#                'e' : 4, 'f' : 5, 'g' : 6, 'h' : 7}
# COL_TO_FILE = {v : k for k, v in FILE_TO_COL.items()}

COL_TO_FILE = {0 : 'a', 1 : 'b', 2 : 'c', 3 : 'd',
               4 : 'e', 5 : 'f', 6 : 'g', 7 : 'h'}

