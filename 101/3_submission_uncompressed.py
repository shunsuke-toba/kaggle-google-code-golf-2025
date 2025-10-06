def p(g):
 p=[x for r in range(len(g))for c in range(len(g[0]))for s in range(len(g),r,-1)for t in range(len(g[0]),c,-1)if'1'in str(x:=[a[c:t]for a in g[r:s]])*all(map(max,x+[*zip(*x)]))][0]
 for s in 3,2,1:[all(len(g[0])>c+j>=0<g[r+i][c+j]-1 for i in range(len(p)*s)for j in range(len(p[0])*s)if p[i//s][j//s]>1)and[g[r+i].__setitem__(c+j,-p[i//s][j//s])for i in range(len(p)*s)for j in range(len(p[0])*s)if len(g[0])>c+j>-1]for r in range(len(g)-len(p)*s+1)for c in range(1-len(p[0])*s,len(g[0]))]
 return[[abs(c)for c in r]for r in g]
