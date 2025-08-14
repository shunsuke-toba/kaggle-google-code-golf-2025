def p(grid):
    n = 16
    # 左上から順に走査し、最初に見つけた3×3の0領域を探す
    for r in range(n - 2):
        for c in range(n - 2):
            if grid[r][c] == 0:
                # この3×3領域と点対称な位置の3×3領域を取得
                # 中心は (7.5, 7.5) なので点対称な位置は (15-r-i, 15-c-j)
                result = []
                for i in range(3):
                    row = []
                    for j in range(3):
                        sym_r = 15 - (r + i)
                        sym_c = 15 - (c + j)
                        row.append(grid[sym_r][sym_c])
                    result.append(row)
                return result