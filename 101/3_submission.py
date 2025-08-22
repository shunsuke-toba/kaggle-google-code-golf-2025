def p(g):
 h=len(g);w=len(g[0]);R=range;F=filter;p=0
 for r in R(h):
  for c in R(w):
   if p:break
   for s in R(r+1,h+1):
    for t in R(c+1,w+1):
     if (x:=[g[i][c:t]for i in R(r,s)])==[*map(list,zip(*F(any,zip(*[*F(any,x)]))))]and len({*sum(x,[]),0})>2:p=x;u={(i,j)for i in R(r,s)for j in R(c,t)}
 for s in 3,2,1:
  r=[[p[i//s][j//s]for j in R(len(p[0])*s)]for i in R(len(p)*s)]
  H=len(r);W=len(r[0])
  for y in R(-H,h):
   for x in R(-W,w):
    if all((r[i][j]==2)==(w>x+j>-1<y+i<h>g[y+i][x+j]==2)and(y+i,x+j)not in u for i in R(H)for j in R(W)):
     for i in R(H):
      for j in R(W):
       if w>x+j>-1<y+i<h:g[y+i][x+j]=r[i][j];u|={(y+i,x+j)}
 return g
