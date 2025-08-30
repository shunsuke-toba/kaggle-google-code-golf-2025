def p(g):
 R=range;l=len;H,W=l(g),l(g[0]);p=next(x for r in R(H)for c in R(W)for s in R(H,r,-1)for t in R(W,c,-1)if all(map(any,(x:=[a[c:t]for a in g[r:s]])+[*zip(*x)]))*sum({*sum(x,[])})>2)
 for S in 3,2,1:h,w=l(p)*S,l(p[0])*S;[all(W>x+j>=0<g[y+i][x+j]-1 for i in R(h)for j in R(w)if p[i//S][j//S]>1)and[g[y+i].__setitem__(x+j,-p[i//S][j//S])for i in R(h)for j in R(w)if W>x+j>=0]for y in R(H-h+1)for x in R(1-w,W)]
 return[[*map(abs,r)]for r in g]