# Define board dimensions as constants
from collections import defaultdict

WIDTH = 512
HEIGHT = 512
SQ_SIZE = HEIGHT // 8
MAX_FPS = 15

# Define images dictionary and pieces list as constants
IMAGES = defaultdict(str)
PIECES = ["bR","bN","bB","bQ","bK","bP","wR","wN","wB","wQ","wK","wP"]
