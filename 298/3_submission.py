def p(j):a=len(j)//2;return[[*map({j[i][i]:j[(t:=(i-1)%a)][t]for i in range(a)}.get,r)]for r in j]
