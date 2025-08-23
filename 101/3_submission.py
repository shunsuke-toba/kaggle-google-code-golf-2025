def p(g):
 h=len(g);w=len(g[0]);R=range;p=0
 for r in R(h):
  for c in R(w):
   if p:break
   for s in R(r+1,h+1):
    for t in R(c+1,w+1):
     if all(map(any,x:=[g[i][c:t]for i in R(r,s)]))and all(map(any,zip(*x)))and{1,2}<={*sum(x,[])}:p=x;u={(i,j)for i in R(r,s)for j in R(c,t)}
 for s in 3,2,1:
  H=len(p)*s;W=len(p[0])*s
  for y in R(-H,h):
   for x in R(-W,w):
    if all((p[i//s][j//s]==2)==(w>x+j>-1<y+i<h>g[y+i][x+j]==2)and(y+i,x+j)not in u for i in R(H)for j in R(W)):
     for i in R(H):
      for j in R(W):
       if w>x+j>-1<y+i<h:g[y+i][x+j]=p[i//s][j//s];u|={(y+i,x+j)}
 return g
