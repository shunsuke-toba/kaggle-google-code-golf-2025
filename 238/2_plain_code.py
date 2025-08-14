def p(grid):
    H, W = len(grid), len(grid[0])
    r1, c1, sz = 0, 0, 0
    for _r1 in range(1,H-1):
        for _c1 in range(1,W-1):
            for _sz in range(2, min(H - _r1, W - _c1) - 1):
                _r2, _c2 = _r1 + _sz, _c1 + _sz
                # 外周が数字で埋まっているか
                if all(grid[_r1-1][c] for c in range(_c1, _c2 + 1)) and \
                   all(grid[_r2+1][c] for c in range(_c1, _c2 + 1)) and \
                   all(grid[r][_c1-1] for r in range(_r1, _r2 + 1)) and \
                    all(grid[r][_c2+1] for r in range(_r1, _r2 + 1)):
                    r1,c1,sz=_r1,_c1,_sz
    
    # 最も数字の多い正方形を探す
    max_count = 0
    r2, c2 = 0, 0
    for _r in range(H - sz):
        for _c in range(W - sz):
            if (_r-sz-1 <= r1 <= _r+sz+1) and (_c-sz-1 <= c1 <= _c+sz+1):
                continue
            nums = []
            for r in range(_r, _r + sz + 1):
                for c in range(_c, _c + sz + 1):
                    if grid[r][c] > 0:
                        nums.append(grid[r][c])
            count = sum((grid[r][c]>0) for r in range(_r, _r + sz + 1) for c in range(_c, _c + sz + 1))
            if count > max_count:
                max_count = count
                r2, c2 = _r, _c
    # 正方形をコピー
    for r in range(sz + 1):
        for c in range(sz + 1):
            grid[r1 + r][c1 + c] = grid[r2 + r][c2 + c]
            grid[r2 + r][c2 + c] = 0
    # 外周の数字を上書き
    for r in range(r1, r1 + sz + 1):
        for c in range(c1, c1 + sz + 1):
            if grid[r][c] == 0:
                continue
            # 4方向の外周までの距離を計算
            up = r - r1
            down = r1 + sz - r
            left = c - c1
            right = c1 + sz - c
            if up < down and up < left and up < right:
                grid[r][c] = grid[r1 - 1][c]
            if down < up and down < left and down < right:
                grid[r][c] = grid[r1 + sz + 1][c]
            if left < up and left < down and left < right:
                grid[r][c] = grid[r][c1 - 1]
            if right < up and right < down and right < left:
                grid[r][c] = grid[r][c1 + sz + 1]

    return [[grid[r][c] for c in range(c1-1, c1 + sz + 2)] for r in range(r1-1, r1 + sz + 2)]