p=lambda g:(r:=[*dict.fromkeys(g[0])])and([r]if r[1:]else[[c]for c in dict.fromkeys(next(zip(*g)))])
