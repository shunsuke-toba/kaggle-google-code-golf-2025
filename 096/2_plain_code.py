import re
def p(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    # Find background color (most frequent)
    color_count = [0]*10
    for r in range(rows):
        for c in range(cols):
            color = grid[r][c]
            color_count[color] += 1
    bg_color = color_count.index(max(color_count))

    info = []
    for c in range(10):
        if c == bg_color:
            continue
        c2=str(c)
        
        sub = None
        
        for w in range(2,9):
            for b in range(1,20):
                for _ in range(4):
                    if any(re.search(c2*w+f"[^{c2}]"*b+c2, "".join([str(x) for x in row])) for row in grid):
                        sub = (c, w, b)                     
                    grid = [list(row) for row in zip(*grid[::-1])]  # Rotate grid 90 degrees

        if not sub and color_count[c]==1:
            # If color appears only once, it is a 1x1 square
            sub = (c, 1, -1)
        if not sub and color_count[c]:
            sub = (c, 3, -3)
        
        if sub:info.append(sub)

    
    info.sort(key=lambda x: x[1]*2 + x[2])
    print(info)
    size = info[-1][1] * 2 + info[-1][2]
    res = [[bg_color] * size for _ in range(size)]
    i=0
    while info:
        I=info.pop()
        for _ in range(4):
            for j in range(I[1]):
                res[i][i+j] = I[0]
                res[i+j][i] = I[0]
            # 90度回転
            res = [list(row) for row in zip(*res[::-1])]
        i+=1
    

    return res
