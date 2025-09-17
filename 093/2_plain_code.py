# -*- coding: utf-8 -*-

def p(grid):
    """
    解くための手続き:
    - 以下の一連の操作を4回行う
    - 14行見て、各行の0~6列までの0でないマスの個数をxとする
    - 0~6列までを全部0にしたあと6列目から左x列分を5にする
    - 90度回転
    """

    # 90度回転関数
    def rotate_90(g):
        return [list(row) for row in zip(*g[::-1])]

    result = [row[:] for row in grid]

    # 4回繰り返す
    for _ in range(4):
        # 90度回転
        result = rotate_90(result)

        # グレー矩形がない方向ならこのループの処理をスキップ
        if result[0][6] != 5 and result[0][7] != 5:
            continue

        # 各行について処理
        for r in range(14):
            # 0~6列目の0でないマスの個数をカウント
            x = 0
            for c in range(7):
                if result[r][c] != 0:
                    x += 1

            # 0~6列目を全て0にする
            for c in range(7):
                result[r][c] = 0

            # 6列目から左にx列分を5にする
            for i in range(x):
                col = 6 - i
                if col >= 0:
                    result[r][col] = 5

    return result
