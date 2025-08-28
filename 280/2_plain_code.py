def p(g):
    # 4回転させながら同じ処理を行う
    for rotation in range(4):
        # すべてのマスを走査
        for i in range(len(g)):
            for j in range(len(g[0]) - 1):  # 右隣をチェックするため-1
                # g[i][j]==2かつg[i][j+1]==0でなければスキップ
                if g[i][j] != 2 or g[i][j+1] != 0:
                    continue
                
                # g[i][j]の左側に連続してある3の数を数える
                a = 0
                for k in range(j-1, -1, -1):  # 右から左へ
                    if g[i][k] == 3:
                        a += 1
                    else:
                        break  # 3以外が出たら止まる
                
                # g[i-a]~g[i-1]を右端まで3にする
                for row in range(i-a, i):
                    if row >= 0:
                        for col in range(j, len(g[0])):
                            g[row][col] = 3
                
                # g[i+1]~g[i+a]を右端まで3にする  
                for row in range(i+1, i+a+1):
                    if row < len(g):
                        for col in range(j, len(g[0])):
                            g[row][col] = 3
                
                # g[i]を右端まで2にする
                for col in range(j, len(g[0])):
                    g[i][col] = 2
        
        # 90度左回転
        g = [*map(list, zip(*g[::-1]))]
    
    return g