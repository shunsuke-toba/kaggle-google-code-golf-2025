def p(grid):
    # Find the least frequent digit (the target digit)
    from collections import Counter
    flat = sum(grid, [])
    counts = Counter(flat)
    target_digit = min(counts, key=counts.get)
    
    # Count target_digit occurrences in each region
    region_counts = Counter()
    
    # For each background digit, count how many target_digits are in its region
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == target_digit:
                # Find what region this target_digit belongs to by looking at neighbors
                # Check adjacent cells to determine the region
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(row):
                        neighbor = grid[ni][nj]
                        if neighbor != target_digit:
                            region_counts[neighbor] += 1
    
    # Find the background digit with most target_digits in its region
    if region_counts:
        result = max(region_counts, key=region_counts.get)
        return [[result]]
    else:
        return [[target_digit]]