def p(g):
 R=range;F=[-2,0,1]+[0]*6;b=eval(str(g));t=2;h=len(g);w=len(g[0])
 while 1:
  B,i,j,t=max((sum(F[b[a][j]]for a in R(i-r,i+r+1)if-1<a<h)+sum(F[b[i][c]]for c in R(j-r,j+r+1)if-1<c<w)-F[b[i][j]]-r/3,i,j,r)for r in(3,2)[:4-t]for i in R(h)for j in R(w))
  if B<1:return g
  for d in R(-t,t+1):
   for y,x in(i+d,j),(i,j+d):g[y][x]+=3*(g[y][x]==5);b[y][x]=0