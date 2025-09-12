def p(g):
 p=[x for r in range(len(g))for c in range(len(g[0]))for s in range(len(g),r,-1)for t in range(len(g[0]),c,-1)if'1'in str(x:=[a[c:t]for a in g[r:s]])*all(map(max,x+[*zip(*x)]))][0]
 for S in 3,2,1:[all(len(g[0])>x+j>=0<g[y+i][x+j]-1 for i in range(len(p)*S)for j in range(len(p[0])*S)if p[i//S][j//S]>1)and[g[y+i].__setitem__(x+j,-p[i//S][j//S])for i in range(len(p)*S)for j in range(len(p[0])*S)if-1<x+j<len(g[0])]for y in range(len(g)-len(p)*S+1)for x in range(1-len(p[0])*S,len(g[0]))]
 return[[*map(abs,r)]for r in g]