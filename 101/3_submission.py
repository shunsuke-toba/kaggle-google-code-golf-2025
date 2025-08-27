def p(g):
 R=range;l=len;H=l(g);W=l(g[0])
 P=next(x for r in R(H)for c in R(W)for s in R(H,r,-1)for t in R(W,c,-1)if all(map(any,(x:=[a[c:t]for a in g[r:s]])+[*zip(*x)]))*sum({*sum(x,[])})>2)
 for S in 3,2,1:
  h=l(P)*S;w=l(P[0])*S;[all((P[i//S][j//S]>1)==(W>x+j>-1<y+i<H>g[y+i][x+j]>1)for i in R(h)for j in R(w))and[W>x+j>-1<y+i<H and g[y+i].__setitem__(x+j,-P[i//S][j//S])for i in R(h)for j in R(w)]for y in R(-h,H)for x in R(-w,W)]
 return[[*map(abs,r)]for r in g]
