def p(g):
 h=len(g);w=len(g[0]);R=range
 P=next(x for r in R(h)for c in R(w)for s in R(h,r,-1)for t in R(w,c,-1)if all(map(any,x:=[g[i][c:t]for i in R(r,s)]))*all(map(any,zip(*x)))*({1,2}<={*sum(x,[])}))
 u=[]
 for S in 3,2,1:
  H=len(P)*S;W=len(P[0])*S
  for y in R(-H,h):
   for x in R(-W,w):
    if all((P[i//S][j//S]>1)==(w>x+j>-1<y+i<h>g[y+i][x+j]>1)and(y+i,x+j)not in u for i in R(H)for j in R(W)):
     for i in R(H):
      for j in R(W):
       if w>x+j>-1<y+i<h:g[y+i][x+j]=P[i//S][j//S];u+=[(y+i,x+j)]
 return g
