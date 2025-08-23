def p(g):
 h=len(g);w=len(g[0]);R=range;p=0;u=[]
 for r in R(h):
  for c in R(w):
   if p:break
   for s in R(r+1,h+1):
    for t in R(c+1,w+1):
     if all(map(any,x:=[g[i][c:t]for i in R(r,s)]))*all(map(any,zip(*x)))*({1,2}<={*sum(x,[])}):p=x
 for s in 3,2,1:
  H=len(p)*s;W=len(p[0])*s
  for y in R(-H,h):
   for x in R(-W,w):
    if all((p[i//s][j//s]>1)==(w>x+j>-1<y+i<h>g[y+i][x+j]>1)and(y+i,x+j)not in u for i in R(H)for j in R(W)):
     for i in R(H):
      for j in R(W):
       if w>x+j>-1<y+i<h:g[y+i][x+j]=p[i//s][j//s];u+=[(y+i,x+j)]
 return g
