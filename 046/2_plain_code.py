def p(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Find columns with all zeros to split segments
    zero_columns = []
    for c in range(cols):
        if all(grid[r][c] == 0 for r in range(rows)):
            zero_columns.append(c)
    
    # Create segments
    segments = []
    start = 0
    for end_col in zero_columns + [cols]:
        if start < end_col:
            segment = []
            for r in range(rows):
                segment.append(grid[r][start:end_col])
            segments.append(segment)
        start = end_col + 1
    
    if not segments:
        return [[0] * cols for _ in range(rows)]
    
    # Find all 5s in a segment
    def find_fives_in_segment(segment):
        fives = []
        for r in range(len(segment)):
            for c in range(len(segment[0])):
                if segment[r][c] == 5:
                    fives.append((r, c))
        return fives
    
    # First segment is used as is
    result_segments = [segments[0]]
    
    # Process segments from second onward
    for i in range(1, len(segments)):
        current_segment = [row[:] for row in segments[i]]
        
        # Find rightmost 5 in previous segment
        prev_segment = result_segments[-1]
        prev_fives = find_fives_in_segment(prev_segment)
        prev_right_five = None
        for r, c in prev_fives:
            if c == len(prev_segment[0]) - 1:
                prev_right_five = r
                break
        
        # Find leftmost 5 in current segment
        curr_fives = find_fives_in_segment(current_segment)
        curr_left_five = None
        for r, c in curr_fives:
            if c == 0:
                curr_left_five = r
                break
        
        # Calculate shift amount
        if prev_right_five is not None and curr_left_five is not None:
            shift = prev_right_five - curr_left_five
            
            # Shift the segment
            if shift != 0:
                new_segment = [[0] * len(current_segment[0]) for _ in range(rows)]
                for r in range(rows):
                    new_r = r + shift
                    if 0 <= new_r < rows:
                        new_segment[new_r] = current_segment[r][:]
                current_segment = new_segment
        
        result_segments.append(current_segment)
    
    # Combine segments horizontally
    result = [[] for _ in range(rows)]
    for segment in result_segments:
        for r in range(rows):
            result[r].extend(segment[r])
    
    # Replace 5s with surrounding colors
    def replace_fives(grid):
        rows = len(grid)
        cols = len(grid[0])
        new_grid = [row[:] for row in grid]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 5:
                    # Check surrounding cells
                    neighbors = []
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != 5 and grid[nr][nc] != 0:
                            neighbors.append(grid[nr][nc])
                    
                    if neighbors:
                        new_grid[r][c] = neighbors[0]
                    else:
                        new_grid[r][c] = 0
        
        return new_grid
    
    result = replace_fives(result)
    
    # Remove columns with all zeros
    final_result = [[] for _ in range(rows)]
    for c in range(len(result[0])):
        if not all(result[r][c] == 0 for r in range(rows)):
            for r in range(rows):
                final_result[r].append(result[r][c])
    
    return final_result