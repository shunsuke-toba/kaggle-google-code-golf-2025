def p(g):n=len(g);r=range(n);t=[v and c.count(v)for c,v in zip(zip(*g),g[-1])];g+=[[0]*n]*n;return[[g[i+t[c]][c]for c in r]for i in r]
