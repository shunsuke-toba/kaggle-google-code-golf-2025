# -*- coding: utf-8 -*-
def p(grid):
    # グリッドのコピーを作成
    result = [row[:] for row in grid]

    # 4回回転操作を実行
    for _ in range(4):
        # 各行について処理
        for i in range(len(result)):
            # 2のマスかつ次が0のマスを探す
            for j in range(len(result[i]) - 1):
                if result[i][j] == 2:
                    if result[i][j + 1] == 0:
                        # 左右3マスを反転させて入れ替え
                        for k in range(3):
                            result[i][j - 1 - k], result[i][j + 1 + k] = result[i][j + 1 + k], result[i][j - 1 - k]
                    break

        # 90度回転
        result = list(map(list, zip(*result[::-1])))

    return result
