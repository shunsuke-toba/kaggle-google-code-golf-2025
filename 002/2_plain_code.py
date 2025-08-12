def p(j):
    result = [row[:] for row in j]
    h, w = len(j), len(j[0])
    
    # Use flood fill from boundaries to mark all reachable empty cells
    visited = [[False] * w for _ in range(h)]
    
    def flood_fill(start_r, start_c):
        if visited[start_r][start_c] or j[start_r][start_c] != 0:
            return
        
        stack = [(start_r, start_c)]
        while stack:
            r, c = stack.pop()
            if visited[r][c] or j[r][c] != 0:
                continue
            
            visited[r][c] = True
            
            # Check all 4 directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and j[nr][nc] == 0:
                    stack.append((nr, nc))
    
    # Start flood fill from all boundary positions
    for r in range(h):
        for c in range(w):
            if (r == 0 or r == h-1 or c == 0 or c == w-1):
                flood_fill(r, c)
    
    # Any unvisited 0 cell is enclosed, fill with 4
    for r in range(h):
        for c in range(w):
            if j[r][c] == 0 and not visited[r][c]:
                result[r][c] = 4
    
    return result