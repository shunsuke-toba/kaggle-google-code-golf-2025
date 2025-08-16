def p(g):
    h = len(g)
    w = len(g[0]) if h else 0

    visited = [[False]*w for _ in range(h)]

    def dfs(si, sj):
        stack = [(si, sj)]
        visited[si][sj] = True
        while stack:
            i, j = stack.pop()
            for di, dj in ((1,0), (-1,0), (0,1), (0,-1)):
                ni, nj = i+di, j+dj
                if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj] and g[ni][nj] == 8:
                    visited[ni][nj] = True
                    stack.append((ni, nj))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if g[i][j] == 8 and not visited[i][j]:
                cnt += 1
                dfs(i, j)

    # 対角線だけ 8、他は 0 の k×k
    return [[8 if i == j else 0 for j in range(cnt)] for i in range(cnt)]