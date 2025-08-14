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
        
        max_w = 0
        max_b = 99
        for _ in range(4):
            for row in grid:
                j = "".join([str(x) for x in row])
                nw = 1
                while str(c)*nw in j:
                    nw += 1
                max_w = max(max_w, nw-1)
                
                for i in range(1,99):
                    if str(c)+str(bg_color)*i+str(c) in j:
                        max_b = min(max_b, i)  
                if nw>2:break
            grid = [list(row) for row in zip(*grid)]  # Rotate grid 90 degrees

        if max_b == 99:
            max_b = 0
        if color_count[c] == 8 and max_w == 3 and max_b == 0:
            max_b = -3
        if color_count[c] == 5 and max_w == 3 and max_b == 0:
            max_b = -3
        if color_count[c] == 1:
            max_w,max_b=1,-1
        if max_w > 0:
            info.append((c, max_w, max_b))
    
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

    
if __name__ == "__main__":
    input_data = [[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 2, 3, 3, 1, 1, 1, 3, 3, 3, 1, 1, 1, 3, 8, 8, 3],
[3, 3, 2, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 1, 3, 8, 3, 3],
[3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3],
[3, 3, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 3, 3],
[3, 3, 2, 3, 3, 3, 3, 7, 7, 7, 3, 3, 3, 3, 3, 8, 8, 3],
[2, 2, 2, 3, 3, 3, 3, 7, 3, 7, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 1, 3, 7, 7, 7, 3, 3, 3, 1, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 1, 1, 1, 3, 3, 3, 1, 1, 1, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 3],
[3, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 3],
[3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]]

    print(p(input_data))
