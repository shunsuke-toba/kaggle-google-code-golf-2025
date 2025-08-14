def p(grid):
    def solve(grid, reverse_r, reverse_c):
        H = len(grid)
        W = len(grid[0])
        
        # 最大の2で囲まれた長方形を見つける
        max_rect = None
        max_area = 0
        
        for r1 in range(H):
            for c1 in range(W):
                for r2 in range(r1 + 2, H):
                    for c2 in range(c1 + 2, W):
                        # 外周が全て2かチェック
                        all_2 = True
                        # 上下の辺
                        for c in range(c1, c2 + 1):
                            if grid[r1][c] != 2 or grid[r2][c] != 2:
                                all_2 = False
                                break
                        if not all_2:
                            continue
                        
                        # 左右の辺
                        for r in range(r1, r2 + 1):
                            if grid[r][c1] != 2 or grid[r][c2] != 2:
                                all_2 = False
                                break
                        
                        if all_2:
                            area = (r2 - r1 + 1) * (c2 - c1 + 1)
                            if area > max_area:
                                max_area = area
                                max_rect = (r1, c1, r2, c2)

        def hash_pattern(pattern, target_number):
            """パターンをハッシュ化する。"""
            hash_value = 0
            for r in range(3):
                for c in range(3):
                    if pattern[r][c] == target_number:
                        hash_value += 1 << (r * 3 + c)
            return hash_value
        def rotate_pattern(pattern):
            """パターンを90度回転させる。"""
            return [[pattern[2 - c][r] for c in range(3)] for r in range(3)]
        
        r1, c1, r2, c2 = max_rect

        # 3x3パターンを収集（外側の領域から、非2要素を含むもの）
        patterns = []
        for r in range(H - 2):
            for c in range(W - 2):
                # max_rectの範囲と重複しない3x3領域
                if r >= r1-2 and r + 2 <= r2 and c >= c1-2 and c + 2 <= c2:
                    continue
                # 0が含まれない3x3領域で、かつ2以外の要素も含む
                has_zero = False
                pattern_3x3 = []
                number = 0
                for dr in range(3):
                    row = []
                    for dc in range(3):
                        val = grid[r + dr][c + dc]
                        if val == 0:
                            has_zero = True
                        if val != 2:
                            number = val
                        row.append(val)
                    pattern_3x3.append(row)

                if not has_zero:
                    # 時計回りに90度回転したパターンを全て記録する
                    for _ in range(4):
                        patterns.append((hash_pattern(pattern_3x3,2), number))
                        pattern_3x3 = rotate_pattern(pattern_3x3)
        
        d = 1,0,-1,0,1
        # メイン長方形内で3x3領域を探して、パターンで埋める
        range_r = range(r1, r2 - 1)
        if reverse_r:
            range_r = range(r2 - 1, r1 - 1, -1)
        range_c = range(c1, c2 - 1)
        if reverse_c:
            range_c = range(c2 - 1, c1 - 1, -1)
        for r in range_r:
            for c in range_c:

                # 3*3領域の外部に0がつながっていないことをチェックする
                ok = True
                #上
                if grid[r][c] == 0 or grid[r][c+1] == 0 or grid[r][c+2] == 0:
                    if r > 0 and (grid[r-1][c] == 0 or grid[r-1][c+1] == 0 or grid[r-1][c+2] == 0):
                        ok = False
                #下
                if grid[r+2][c] == 0 or grid[r+2][c+1] == 0 or grid[r+2][c+2] == 0:
                    if r + 3 < H and (grid[r+3][c] == 0 or grid[r+3][c+1] == 0 or grid[r+3][c+2] == 0):
                        ok = False
                #左
                if grid[r][c] == 0 or grid[r+1][c] == 0 or grid[r+2][c] == 0:
                    if c > 0 and (grid[r][c-1] == 0 or grid[r+1][c-1] == 0 or grid[r+2][c-1] == 0):
                        ok = False
                #右
                if grid[r][c+2] == 0 or grid[r+1][c+2] == 0 or grid[r+2][c+2] == 0:
                    if c + 3 < W and (grid[r][c+3] == 0 or grid[r+1][c+3] == 0 or grid[r+2][c+3] == 0):
                        ok = False
                if not ok:
                    continue

                # 現在の3x3のパターンを取得
                current_pat = hash_pattern([[grid[r + dr][c + dc] for dc in range(3)] for dr in range(3)], 0)
                # パターンと構造比較
                for pattern in patterns:
                    if pattern[0] == current_pat:
                        # パターンの数字を取得
                        number = pattern[1]
                        for dr in range(3):
                            for dc in range(3):
                                if grid[r + dr][c + dc] == 2:
                                    grid[r + dr][c + dc] = number
                                elif grid[r + dr][c + dc] == 0:
                                    grid[r + dr][c + dc] = 2
                        break

        # 0が残っていないかチェック
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if grid[r][c] == 0:
                    return None

        return [[grid[r][c] for c in range(c1, c2 + 1)] for r in range(r1, r2 + 1)]
    
    revc_list = (False, True)
    if len(grid) != 24: revc_list = (True, False)
    for reverse_r in (False, True):
        for reverse_c in revc_list:
            result = solve(grid, reverse_r, reverse_c)
            if result is not None:
                return result
    return None