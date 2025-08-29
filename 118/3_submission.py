def p(g):
 h=len(g);w=len(g[0]);R=range;b=[*map(list,g)];t=2;f=lambda y,x:((a:=b[y][x])==2)-2*(a<1)
 while 1:
  B,i,j,t=max((sum(f(a,j)for a in R(i-r,i+r+1)if-1<a<h)+sum(f(i,c)for c in R(j-r,j+r+1)if-1<c<w)-f(i,j)-r/3,i,j,r)for r in(3,2)[:4-t]for i in R(h)for j in R(w))
  if B<1:return g
  for d in R(-t,t+1):
   for y,x in(i+d,j),(i,j+d):g[y][x]+=3*(g[y][x]==5);b[y][x]=0