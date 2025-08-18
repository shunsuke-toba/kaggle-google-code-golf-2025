def p(grid):
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
            cnt2 = 0
            for dr in range(3):
                row = []
                for dc in range(3):
                    val = grid[r + dr][c + dc]
                    if val == 0:
                        has_zero = True
                    if val != 2:
                        number = val
                    if val == 2:
                        cnt2 += 1
                    row.append(val)
                pattern_3x3.append(row)

            if not has_zero:
                # 時計回りに90度回転したパターンを全て記録する
                for rot in range(4):
                    patterns.append((cnt2, -rot, hash_pattern(pattern_3x3,2), number))
                    pattern_3x3 = rotate_pattern(pattern_3x3)
    patterns.sort(reverse=True)

    # メイン長方形内で3x3領域を探して、パターンで埋める
    for pattern in patterns:
        for r in range(r1, r2 - 1):
            for c in reversed(range(c1, c2 - 1)):

                # 現在の3x3のパターンを取得
                current_pat = hash_pattern([[grid[r + dr][c + dc] for dc in range(3)] for dr in range(3)], 0)
                # パターンと構造比較
                if pattern[2] == current_pat:
                    # パターンの数字を取得
                    number = pattern[3]
                    for dr in range(3):
                        for dc in range(3):
                            if grid[r + dr][c + dc] == 2:
                                grid[r + dr][c + dc] = number
                            elif grid[r + dr][c + dc] == 0:
                                grid[r + dr][c + dc] = 2


    return [[grid[r][c] for c in range(c1, c2 + 1)] for r in range(r1, r2 + 1)]