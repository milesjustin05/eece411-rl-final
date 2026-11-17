from collections import deque
from simulator import GRID_MAP

# gets the map from the simulator and stores it in rows/columns
grid = [list(row) for row in GRID_MAP]

# stores the amount of rows and columns as well as the possible move directions
ROWS, COLS = len(grid), len(grid[0])
MOVES = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

# breadth-first-search for shortest path to every cell
def bfs(start):
    """Distance from start to every reachable open cell."""
    dist = {start: 0}
    q = deque([start])
    while q:
        r, c = q.popleft()
        for dr, dc in MOVES.values():
            nr, nc = r + dr, c + dc
            if (0 <= nr < ROWS and 0 <= nc < COLS
                    and grid[nr][nc] != "#" and (nr, nc) not in dist):
                dist[(nr, nc)] = dist[(r, c)] + 1
                q.append((nr, nc))
    return dist

# every non-wall cell
open_cells = [(r, c) for r in range(ROWS) for c in range(COLS) if grid[r][c] != "#"]

# full bfs table: bfs_table[a][b] = shortest steps from a to b
bfs_table = {cell: bfs(cell) for cell in open_cells}

'''
find and stores the drop off cells, pick-up cells, and the agent start cells
D: [(1,1), (7,4)]
S: [(1,8), (8,8)]
A: [(4,5)]
'''
key = {}
for r, c in open_cells:
    if grid[r][c] in "ADS":
        key.setdefault(grid[r][c], []).append((r, c))

'''
labels each individual drop off and pickup
D1: (1,1)
D2: (7,4)
S1: (1,8)
S2: (8,8)
A: (4,5)
'''
labels = []
for ch, cells in key.items():
    for i, cell in enumerate(cells):
        labels.append((f"{ch}{i+1}" if len(cells) > 1 else ch, cell))
